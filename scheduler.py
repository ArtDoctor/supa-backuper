import os
import time
import subprocess
from datetime import datetime


def get_interval() -> int:
    try:
        interval = int(os.environ.get('INTERVAL_HOURS', 1))
        return interval * 3600  # Convert hours to seconds
    except ValueError:
        print("Invalid interval value. Please provide a valid integer.")
        exit(1)


def manage_backups(folder: str, limit: int = 5) -> None:
    backups = sorted(
        [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))],
        key=lambda x: os.path.getctime(os.path.join(folder, x))
    )

    while len(backups) > limit:
        oldest_backup = backups.pop(0)
        os.remove(os.path.join(folder, oldest_backup))
        print(f"Deleted oldest backup: {oldest_backup}")


def run_backup(url: str, name: str) -> None:
    try:
        if name[-4:] != '.sql':
            name += '.sql'
        folder = os.getenv('BACKUP_FOLDER')
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_name = f"{timestamp}_{name}"
        path = os.path.join(folder, backup_name)
        subprocess.run(f'pg_dump --schema="public" {url} > {path}', shell=True, check=True)
        print(f"Success: '{backup_name}'")
        manage_backups(folder)
    except subprocess.CalledProcessError as e:
        print(f"Failed to backup '{name}'. Error: {e}")


def run_backups(urls: str, names: str) -> None:
    urls = urls.split(',')
    names = names.split(',')

    for url, name in zip(urls, names):
        run_backup(url, name)


def main():
    dbs = os.getenv('SUPA_URLS')
    names = os.getenv('SUPA_NAMES')

    interval = get_interval()

    while True:
        run_backups(dbs, names)
        time.sleep(interval)


if __name__ == "__main__":
    main()
