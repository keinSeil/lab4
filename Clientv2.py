import socket
import sys
sys.path.append(r'C:\\Users\\Wes\\Documents\\GitHub\\fanuc_ethernet_ip_drivers\\src')

from robot_controller import robot
import time

#Wifi ngrobot5G
#Password 86624107Bb

#Global Constants
drive_path = '172.29.208.124' #Beaker
sleep_time = 0.5

# Define the server address (IP and port)
server_ip = '172.29.208.79'  # Replace with your actual server IP address
server_port = 5000  # Replace with the port you want to use

def send_coords_to_server(coords):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    # client_socket.connect(('0.0.0.0', server_port))
    client_socket.connect((server_ip, server_port))

    # Convert the coordinates to a string format and send to the server
    data_to_send = ",".join(map(str, coords))

    client_socket.send(data_to_send.encode('utf-8'))
    # Receive a response from the server (might be an acknowledgment or the transformed coordinates)
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode('utf-8')}")

    # Close the client socket
    client_socket.close()



#!/usr/bin/env python3
"""! @python program for FANUC robot control"""

# IMPORTANT: Ensure the "ROS2-EIP_MAINV2".tp program is running on the teaching pendant

# Global Constants
drive_path = '172.29.209.124' # Beaker
ts = .7 # Wait time
yo = 0 # offset for y. (+) brings tool toward bunsen

#Functions
def joint_move(crx10, joint_pose, ts):
    crx10.set_pose(joint_pose)  # Step 1: Set Robot Pose using six joint angles
    crx10.start_robot()   # Step 2: Start Robot Movement
    time.sleep(ts)        # Step 3: Sleep for Specified Time

def cart_move(crx10, cart_pose, ts):
    crx10.send_coords(cart_pose)
    crx10.start_robot()
    time.sleep(ts)

pose0 = [92.87217712402344,18.125370025634766,-41.355613708496094,0.8590555787086487,-49.22829055786133,-63.55329132080078]
cpose0 = [110.77, 670, -102.758, 180, 0, 30]
cpose1 = [108.6, 683.57, -203.44, 179.48, -1.247, 31.896] # v3
pose2 = [45.07453155517578,45.947452545166016,-8.966269493103027,1.5336558818817139,-80.24510192871094,-16.003690719604492]
pose3 = [40.18388366699219,57.8693733215332,-16.98442268371582,-1.184096097946167,-71.86784362792969,-12.543599128723145]
cpose3 = [940, 670, -202, 180, 0, 30]
pose4 = [91.7227554321289,17.42302131652832,-39.61912155151367,1.3989849090576172,-51.0536994934082,25.9] # v2
pose5 = [90.66902923583984,18.180810928344727,-41.12506103515625,-2.7863874435424805,-48.007633209228516,-148.91787719726562] # Rotate 90
# pose6 = [88.79205322265625,24.91090202331543,-50.50844192504883,-6.881253242492676,-38.27078628540039,35]
cpose6 = [81.85, 623.62, -201.349, -176.997, -3.332, 118.347]


def main():
    """! Main program entry"""
       

    ## Initiializing Parameters
    # Create new robot object
    crx10 = robot(drive_path)
    crx10.set_speed(180)  # Setting speed up to 250mm/s
    
    # Start the main loop (Line 2)
    loops = 1
    while(loops <= 1):
        
        try:
            CurPosList = crx10.get_coords()
            coords = CurPosList
            # print(coords)

            send_coords_to_server(coords)


            # # Open gripper
            # crx10.gripper("open")
            # time.sleep(ts)

            # ### Home Position ### cpose0
            # crx10.send_coords(110.77, 672, -102.758, 180, 0, 30) # Move to just above the die
            # crx10.start_robot()
            # time.sleep(ts)
            # # cpose1
            # crx10.send_coords(108.6, 673, -203.44, 180, 0, 30) # x,y,z,w,p,r
            # crx10.start_robot()
            # time.sleep(ts)

            # # Close gripper
            # crx10.gripper("close") #4
            # time.sleep(ts)

            # # Move and place die
            # # Brings the die to a point just above the prox sensors to avoid potential collisions with the robot gripper
            # crx10.set_pose(pose2) # 5
            # crx10.start_robot()
            # time.sleep(ts)

            # # Sets the dice on the conveyer belt
            # # crx10.set_pose(pose3) # 6
            # crx10.send_coords(940, 672, -202, 180, 0, 30)
            # crx10.start_robot()
            # time.sleep(ts)

            # # Place die on conveyor belt by opening the gripper
            # crx10.gripper("open") # 7
            # time.sleep(ts)

            # ## 8-16 ###
            # # Turn on conveyer belt (see FANUCRegisterDefinitions for more info)
            # crx10.conveyor('forward') # 8
            # # crx10.conveyor('stop') # 8

            # ### 17-... ###
            # crx10.set_pose(pose0) # 17 Returns to just above the dice's location using linear motion along the conveyor belt's length
            # # crx10.start_robot(blocking=False) # MAYBE WILL CAUSE PROBLEMS
            # crx10.start_robot() 
            # time.sleep(ts)
            
        
            # # Check if the proximity sensor has been tripped
            # while True: # 9-15
            #     # Read the right proximity sensor
            #     right_sensor_value = crx10.conveyor_proximity_sensor("right")
            #     # Check if the sensor returns a '1'
            #     if right_sensor_value == 1:
            #         # print("Right proximity sensor detected an object!")
            #         break  # Exit the loop
            #     # time.sleep(0.05)


            # print("Broke out of loop")
            # crx10.conveyor('stop') # 16
            # time.sleep(ts)

            # # cpose1: Grab dice
            # # crx10.send_coords(108.6, 670, -203.44, 179.48, -1.247, 31.896) # cpose1 (grab dice)
            # crx10.send_coords(119, 673, -203.44, 180, 0, 30) # cpose1 (grab dice)
            # crx10.start_robot()
            # time.sleep(ts)

            # crx10.gripper("close") # 18 Close gripper
            # time.sleep(ts)

            # # cpose1-2: Lift straight up
            # crx10.send_coords(119, 673, -100, 180, 0, 30) # Increase z by 100
            # crx10.start_robot()
            # time.sleep(ts)

            # crx10.write_joint_offset(6, 90)
            # crx10.start_robot()
            # time.sleep(ts)

            # # cpose6: Lowers the dice back down slightly above cpose1 to avoid force sensor trips
            # crx10.send_coords(75.8, 615.8, -203, 180, 0, 120) 
            # crx10.start_robot()
            # time.sleep(ts)

            # crx10.gripper("open") # 22 Opens gripper
            # time.sleep(ts)
            
            # # cpose6-2: Lifts straight up to avoid disturbing dice
            # crx10.send_coords(81.85, 610, -101, 180, 0, 120) 
            # crx10.start_robot()
            # time.sleep(ts)

            # # Rotate back to home
            # # crx10.set_pose(pose0) # 23
            # crx10.send_coords(119, 673, -102.758, 180, 0, 30)
            # crx10.start_robot()
            # time.sleep(ts)

            # # Clap your hands
            # crx10.gripper("close") # 18 Close gripper
            # time.sleep(.4)
            # crx10.gripper("open") # 22 Opens gripper
            # time.sleep(.4)
            # crx10.gripper("close") # 18 Close gripper
            # time.sleep(.4)
            # crx10.gripper("open") # 22 Opens gripper
            # time.sleep(.4)

            loops += 1
            print(loops)
        except KeyboardInterrupt:
            print("Shutting down conveyor and attempting to open gripper")
            crx10.conveyor('stop')
            time.sleep(ts)
            crx10.gripper("open")
            time.sleep(ts)
            loops += 1
            print(loops)
            print("done")


if __name__=="__main__":
    main()






# Assuming you've already obtained the coords as in the previous code:
# coords = moveToRandomLocation(robotA)
# send_coords_to_server(coords)