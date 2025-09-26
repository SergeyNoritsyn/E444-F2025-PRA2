# Use Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /E444-F2025-PRA2

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files
COPY . .

CMD ["flask", "--app", "hello",  "run", "--host=0.0.0.0"]