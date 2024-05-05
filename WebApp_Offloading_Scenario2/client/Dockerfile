FROM python:3.9-slim
WORKDIR /docker_scenario4
# Install Python packages needed for the Flask app
RUN pip install --no-cache-dir Flask requests

# Copy the Python script
COPY client.py .

# Copy the templates directory
COPY templates/ templates/

# Expose the port that the client will run on
EXPOSE 80

# Command to run the Flask application
CMD ["python", "client.py"]
