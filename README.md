# Supabase Backup Scheduler

For some reason simple pg_dump solutions didn't work for me, so I wrote my own.  
This project is a Python script that runs Supabase database backups at specified intervals using Docker. The script ensures that no more than (some amount) backups are stored, deleting the oldest backups when the limit is exceeded.

## Features

- Runs backups for multiple databases at specified intervals.
- Stores backups in a specified folder.
- Maintains only the N most recent backups.

## Requirements

- Docker
- Python 3.x

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/backup-scheduler.git
   cd backup-scheduler

2. Clone template.env to .env
3. Specify your variables like amount of backups, urls and names in `1,2,3` format.
4. Run the python script/dockerfile/docker compose.