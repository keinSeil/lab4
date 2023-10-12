import socket
import random
import os
import sys

sys.path.append('../')



current_directory = os.getcwd()
print(current_directory)



# Define the server's port (since we're not specifying an IP, it'll default to localhost)
server_port = 5000

cpose1 = [] # Designated Location
cpose2 = [] # Over the conveyor belt
cpose3 = [] # Away from the ranomization area

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (defaults to localhost since we're omitting the IP)
client_socket.connect(('172.29.208.79', server_port))

def send_coords_to_server(coords):
    # Convert the coordinates to a string format and send to the server
    data_to_send = ",".join(map(str, coords))
    client_socket.send(data_to_send.encode('utf-8'))

    # Receive a response from the server (might be an acknowledgment or the transformed coordinates)
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode('utf-8')}")

# Sample code to obtain and send coords (you'd replace this with your actual method of obtaining coords)
coords = (100, 150, 200)  # Replace with the actual coordinates
send_coords_to_server(coords)

#Step1
crx10.send_coords(cpose1)
crx10.gripper("close")

#Step2
x_offset = random.uniform(-5, 5)
y_offset = random.uniform(-5, 5)
z_offset = random.uniform(-10, 10)
offsets = [x_offset, y_offset, z_offset]
# w_offset = random.uniform(3.5)
# p_offset = random.uniform(-3)
# r_offset = random.uniform(7)
random_pose = #Enter Cpose2 + offsets
crx10.send_coords(random_pose)

#Step 3
send_coords_to_server(offsets)

#Step4 (introduce loop?)
response = client_socket.recv(1024)
if response != "gripper_closed":
    print("Error: Unexpected signal from Robot B!")
    
#Step5
crx10.gripper("open")
crx10.send_coords(cpose3)
message = "gripper_open"
client_socket.send(message.encode('utf-8'))

#Step 6
new_offsets = client_socket.recv(1024)
#implement Method to add offsets correctly

#Step7
new_random_pose = # cpose2 + new offsets
crx10.send_coords(new_random_pose)
crx10.gripper("close")
message = "gripper_closed"
client_socket.send(message.encode('utf-8'))
response = client_socket.recv(1024)
if response != "gripper_open":
    print("Error: Unexpected signal from Robot B!")

#Step8
crx10.send_coords(cpose1)
crx10.gripper("open")

#Step9
#Implement loop

# Close the client socket
client_socket.close()

# import socket
# import sys
# # sys.path.append(r'C:\Users\Lukas Homann\PycharmProjects\RoboticsLab3\FANUC-Ethernet_IP_Drivers\src')
# # sys.path.append('../FANUC-Ethernet_IP_Drivers_Gates/src')
# # sys.path.append('.../fanuc-ethernet_ip_drivers/src')
# # sys.path.append(r'C:\\Users\\Wes\\Documents\\GitHub\\fanuc_ethernet_ip_drivers\\src')

# from robot_controller import robot

# #Wifi ngrobot5G
# #Password 86624107Bb

# #Global Constants
# drive_path = '172.29.208.124' #Beaker
# sleep_time = 0.5

# # Define the server address (IP and port)
# # server_ip = '172.29.208.79'  # Replace with your actual server IP address
# server_ip = '0.0.0.0'  # Replace with your actual server IP address
# server_port = 5000  # Replace with the port you want to use

# def send_coords_to_server(coords):
#     # Create a socket object
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Connect to the server
#     client_socket.connect((server_ip, server_port))

#     # Convert the coordinates to a string format and send to the server
#     data_to_send = ",".join(map(str, coords))
#     client_socket.send(data_to_send.encode('utf-8'))

#     # Receive a response from the server (might be an acknowledgment or the transformed coordinates)
#     response = client_socket.recv(1024)
#     print(f"Received response: {response.decode('utf-8')}")

#     # Close the client socket
#     client_socket.close()

#     crx10 = robot()

# # # Assuming you've already obtained the coords as in the previous code:
# # coords = moveToRandomLocation(robotA)
# # send_coords_to_server(coords)