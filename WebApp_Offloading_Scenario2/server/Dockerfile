# Use a slim version of Python 3
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /docker_scenario4

# Install Python packages needed for the Flask app and image processing
RUN pip install --no-cache-dir Flask Pillow requests

# Copy the Flask application code into the container
COPY ./server.py .

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "server.py"]
