#!/usr/bin/env python3
# ipc_client.py

'''import socket
import csv

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898  # The port used by the server

# Read data from a CSV file
values = []

print("Client >> Reading the data from CSV file...")
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(row[0])  # Assuming each value is in the first column of each row

# Check if we have at least 50 values
if len(values) < 50:
    raise ValueError("Not enough data in CSV file; expected at least 50 values")

# Select first 50 values for sending
data_to_send = ' '.join(values[:50]).encode()
print("Client >> Sending the data to server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data_to_send)
    # Receive data from the server
    data = s.recv(1024)
    # Decode the received data and convert to float
    mean_received = float(data.decode())
print("Client >> Data sent successfully!!!")
print('Received mean:', mean_received)'''

#!/usr/bin/env python3
# ipc_client.py

import socket
import csv

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898  # The port used by the server

# Read data from a CSV file
values = []

print("Client >> Reading the data from CSV file...")
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(row[0])  # Assuming each value is in the first column of each row

# Check if we have at least 50 values
if len(values) < 50:
    raise ValueError("Not enough data in CSV file; expected at least 50 values")

# Select first 50 values for sending
data_to_send = ' '.join(values[:50]).encode()
print("Client >> Sending the data to server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data_to_send)
    # Receive data from the server
    data = s.recv(1024)
    # Decode the received data
    response = data.decode()
    # Expecting the response to be in the format "Mean: X, Std Dev: Y, Median: Z"
    parts = response.split(', ')
    mean_received = float(parts[0].split(': ')[1])
    std_dev_received = float(parts[1].split(': ')[1])
    median_received = float(parts[2].split(': ')[1])
print("Client >> Data sent successfully!!!")
print('Received mean:', mean_received)
print('Received standard deviation:', std_dev_received)
print('Received median:', median_received)

