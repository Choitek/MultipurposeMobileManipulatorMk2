'''
The RobotCommander is an example script that takes 
continuous user input in the form of 4 commands:
  [L] rotates left 90 degrees.
  [R] rotates right 90 degrees.
  [F] moves the robot forward.
  [B] moves the robot backward.
  
With the program running, type in chains of 
letters to make the robot follow sequences.
The robot will say which direction it is 
moving with the Customizable Robot Face open.
'''

# Import all libraries
from MMM_Speaker import Speaker   #Make sure you have pyOSC installed! https://pypi.python.org/pypi/pyOSC
from MMM import MMM               #Make sure you have pyserial 27 installed! https://pypi.python.org/pypi/pyserial/2.7
import threading
import time
import sys

#--------------INITIALIZATION------------------#
#Change 'COM3' to your COM Port. This is something like "/dev/ttyACM0" on Linux and Mac.
#If you don't know what your COM Port is, plug in the USB to the Arduino Mega 2560 and
#follow the instructions in this link: https://www.arduino.cc/en/Guide/Troubleshooting#toc1
mmm = MMM('COM3') 
speaker = Speaker()

#give some time to connect.
time.sleep(5)              

# Function to run on another thread:
def updateRobot():
  while True:
    mmm.clampAll();  
    mmm.update();
    time.sleep(0.1);
    mmm.parseData();

#begin thread to update continuously:
thread = threading.Thread(target=updateRobot, args=())
thread.daemon = True            
thread.start()
#----------------------------------------------#

# initial pose
mmm.setWheelVelocity(0,0)
mmm.rotateShoulders(100,100)
mmm.rotateElbows(-60,-60)
mmm.extendArms(0,0)
mmm.setLeftGrippers(0,0,0,0,0)
mmm.setRightGrippers(0,0,0,0,0)

# defined variables
rot90 = 2.25 # time to rotate 90
d12 = 2      # time to move 12 inches

# usage info
print("Welcome to the robot commander.\n")
print("To make the robot move, type in commands in this format:\n")
print("[L] rotates left 90 degrees.")
print("[R] rotates right 90 degrees.")
print("[F] moves the robot forward.")
print("[B] moves the robot backward.\n")

# Continuously ask for input
while(True):
  commands = raw_input("Type Commands and press Enter.")

  for i in xrange(len(commands)):
    command = commands[i].upper()
    if(command == 'L'): # rotate left
      speaker.speak("Rotating left.");
      mmm.setWheelVelocity(.18,-.18)
      time.sleep(rot90)
    elif(command == 'R'): # rotate right
      speaker.speak("Rotating right.");
      mmm.setWheelVelocity(-.18,.18)
      time.sleep(rot90)
    elif(command == 'F'): # move forward
      speaker.speak("Moving forward.");
      mmm.setWheelVelocity(.18,.18)
      time.sleep(rot90)
    elif(command == 'B'): # move backward
      speaker.speak("Moving backward.");
      mmm.setWheelVelocity(-.18,-.18)
      time.sleep(rot90)
    elif(command == 'Q'): # quit
      mmm.ser.close()
      quit()  

  # stop the robot when done parsing commands      
  mmm.setWheelVelocity(0,0)
  mmm.update()
  
