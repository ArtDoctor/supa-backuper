# Use a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install pg_dump
RUN apt-get update && apt-get install -y postgresql-client

# Copy the Python script into the container
COPY scheduler.py /app/

# Run the Python script
CMD ["python", "scheduler.py"]
