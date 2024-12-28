# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
