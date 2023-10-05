import socket

# Define the server address (IP and port)
server_ip = '129.101.119.223'  # Replace with your actual server IP address
server_port = 5000  # Replace with the port you want to use

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (maximum 1 connection in this example)
server_socket.listen(1)
print(f"Server listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

# Send a response to the client
response = "Hello from the server!"
client_socket.send(response.encode('utf-8'))

# Close the client and server sockets
client_socket.close()
server_socket.close()