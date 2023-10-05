import socket

# Define the server address (IP and port)
server_ip = 'your_server_ip'  # Replace with your actual server IP address
server_port = 5000  # Replace with the port you want to use

def send_coords_to_server(coords):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))

    # Convert the coordinates to a string format and send to the server
    data_to_send = ",".join(map(str, coords))
    client_socket.send(data_to_send.encode('utf-8'))

    # Receive a response from the server (might be an acknowledgment or the transformed coordinates)
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode('utf-8')}")

    # Close the client socket
    client_socket.close()

# Assuming you've already obtained the coords as in the previous code:
coords = moveToRandomLocation(robotA)
send_coords_to_server(coords)