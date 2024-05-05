# Start with the Ubuntu base image
FROM ubuntu:latest

# Install Python3 and necessary networking tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Add the server Python script to the image's '/server/' folder
# Ensure ipc_server_2.py is in the build context
ADD ipc_server_2.py /server/

# Set '/server/' as the working directory
WORKDIR /server/

# Expose port 9898 on the container to allow communication to/from the server
EXPOSE 9898

# Command to run the server script, assuming it's executable and using the correct path
CMD ["python3", "/server/ipc_server_2.py"]
