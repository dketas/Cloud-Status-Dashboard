# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file and install dependencies
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY app/ .

# Expose the port your Flask app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]
