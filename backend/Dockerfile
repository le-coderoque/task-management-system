# Use an official Python runtime as a parent image
FROM python:3.10

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt && \
    pip install --upgrade pip

# Install netcat
RUN apt update && apt install -y netcat-openbsd

# Copy project
COPY ./task_manager .
COPY ./entrypoint.sh .

# Make sure entrypoint.sh is executable
RUN chmod +x /app/entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
