# Use Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files
COPY . .

CMD ["python", "hello.py"]