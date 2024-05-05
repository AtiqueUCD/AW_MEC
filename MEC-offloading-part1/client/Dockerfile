# Start with the Ubuntu base image
FROM ubuntu:latest

# Install Python3 and other necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copy files into the image's '/client/' folder
COPY ipc_client_2.py /client/
COPY data.csv /client/

# Set '/client/' as the working directory
WORKDIR /client/

# Execute the Python script
CMD ["python3", "ipc_client_2.py"]
