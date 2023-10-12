import socket
#from robot_controller import robot
#import sys

#Global Constants
drive_path = '172.29.209.123' #Bunsen
sleep_time = 0.5

# Define server details
server_port = 5000

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', server_port))
server_socket.listen(1)
print("Server listening for incoming connections...")

while True:
    # Wait for a connection from a client (Computer A)
    client_socket, client_address = server_socket.accept()

    # Receive the data (coords) sent from the client
    data = client_socket.recv(1024).decode('utf-8')
    received_coords = tuple(map(int, data.split(',')))

    # Here, you would send the translated_coords to Robot B
    # But for now, let's just send an acknowledgment back to the client
    ack_message = "Coordinates received and processed!"
    client_socket.send(ack_message.encode('utf-8'))

    # Close the connection to the client
    client_socket.close()