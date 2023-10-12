import socket
import sys
# sys.path.append(r'C:\Users\Lukas Homann\PycharmProjects\RoboticsLab3\FANUC-Ethernet_IP_Drivers\src')
# sys.path.append('../FANUC-Ethernet_IP_Drivers_Gates/src')
# sys.path.append('.../fanuc-ethernet_ip_drivers/src')
sys.path.append(r'C:\\Users\\Wes\\Documents\\GitHub\\fanuc_ethernet_ip_drivers\\src')

from robot_controller import robot

#Wifi ngrobot5G
#Password 86624107Bb

#Global Constants
drive_path = '172.29.208.124' #Beaker
sleep_time = 0.5

# Define the server address (IP and port)
# server_ip = '172.29.208.79'  # Replace with your actual server IP address
server_ip = '0.0.0.0'  # Replace with your actual server IP address
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

    crx10 = robot()

# # Assuming you've already obtained the coords as in the previous code:
# coords = moveToRandomLocation(robotA)
# send_coords_to_server(coords)