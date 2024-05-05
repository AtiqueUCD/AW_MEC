
'''
#!/usr/bin/env python3
# ipc_server.py

import socket

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)
print("Server >> Starting server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Decode the bytes to string, split it, and convert to floats
            float_data = list(map(float, data.decode().split()))

            # Print each float value
            print("Received floats:")
            for value in float_data:
                print(value)

            # Compute the mean of the received float data
            mean_value = sum(float_data) / len(float_data) if float_data else 0
            print("Mean of received floats:", mean_value)

            # Send the mean value back to the client
            conn.sendall(str(mean_value).encode())
'''
#!/usr/bin/env python3
# ipc_server.py

import socket

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)
print("Server >> Starting server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Decode the bytes to string, split it, and convert to floats
            float_data = list(map(float, data.decode().split()))

            if float_data:
                # Print each float value
                print("Received floats:")
                for value in float_data:
                    print(value)

                # Compute the mean of the received float data
                mean_value = sum(float_data) / len(float_data)

                # Compute the standard deviation
                variance = sum((x - mean_value) ** 2 for x in float_data) / len(float_data)
                std_dev = variance ** 0.5

                # Compute the median
                sorted_data = sorted(float_data)
                n = len(sorted_data)
                mid = n // 2
                if n % 2 == 0:
                    median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2
                else:
                    median_value = sorted_data[mid]

                print("Mean of received floats:", mean_value)
                print("Standard deviation of received floats:", std_dev)
                print("Median of received floats:", median_value)

                # Prepare the result string
                result = f"Mean: {mean_value}, Std Dev: {std_dev}, Median: {median_value}"
            else:
                result = "No data received."

            # Send the result back to the client
            conn.sendall(result.encode())

