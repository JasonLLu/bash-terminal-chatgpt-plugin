# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Set the build argument for the GitHub token
ARG GITHUB_TOKEN

# Install Git and other dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable for the GitHub token
ENV GITHUB_TOKEN=$GITHUB_TOKEN

# Expose the port that the application listens on
EXPOSE 5003

# Start the application
CMD ["python", "main.py"]
