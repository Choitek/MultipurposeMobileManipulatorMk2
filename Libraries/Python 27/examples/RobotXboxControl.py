'''
This is an example that maps robot motions
to an XBOX 360 controller (Wired works best.)

The basic controls are as follows:
  Left Stick controls left arm.
  Right Stick controls right arm.
  D-Pad controls wheeled mobile base.
  
To control the grippers:
  Left Bumper moves all attached left grippers.
  Right Bumper moves all attached left grippers.
'''

# Import all libraries
from MMM import MMM   #Make sure you have pyserial 27 installed! https://pypi.python.org/pypi/pyserial/2.7
import pygame         #Make sure you have pyGame installed! http://www.pygame.org/download.shtml
import XboxController #Make sure you have XboxController.py in the same folder.
import time
import sys

#--------------INITIALIZATION------------------#
#Change 'COM3' to your COM Port. This is something like "/dev/ttyACM0" on Linux and Mac.
#If you don't know what your COM Port is, plug in the USB to the Arduino Mega 2560 and
#follow the instructions in this link: https://www.arduino.cc/en/Guide/Troubleshooting#toc1
mmm = MMM('COM3') 

#give some time to connect.
time.sleep(2)              

# Function to run on another thread:
def updateRobot():
  while True:
    mmm.clampAll();  
    mmm.update();
    time.sleep(0.05);
    mmm.parseData();

#begin thread to update continuously:
thread = threading.Thread(target=updateRobot, args=())
thread.daemon = True            
thread.start()

#-----------------XBOX360 Controller----------------#
# Setup Xbox360 controller. 
xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.3,
    scale = 1,
    invertYAxis = False)

# Begin Xbox Controller.
xboxCont.start()

# Continuously respond to Xbox360 Controller Input
while(True):
  
  # Quit when pressing back button
  if(xboxCont.BACK):
    xboxCont.stop()
    mmm.ser.close()
    quit()
  
  # reset pose with start
  if(xboxCont.START):
    mmm.reset()
  
  # Control Wheels with DPAD
  (horizontal,vertical) = xboxCont.DPAD
  mmm.leftWheel = (-horizontal + vertical) * 255
  mmm.rightWheel = (horizontal + vertical) * 255
  
  # Boost with A
  if(xboxCont.A):
    mmm.leftWheel = 255
    mmm.rightWheel = 255
  
  # Left Thumbstick
  if(xboxCont.LEFTTHUMB):
    # Control Arm 
    mmm.leftArm -= xboxCont.LTHUMBY*50
  else:
    # Control Shoulder
    mmm.leftShoulder += xboxCont.LTHUMBX*3
    # Control Elbow
    mmm.leftElbow -= xboxCont.LTHUMBY*3
  
  # Right Thumbstick
  if(xboxCont.RIGHTTHUMB):
    # Control Arm 
    mmm.rightArm -= xboxCont.RTHUMBY*50
  else:
    # Control Shoulder
    mmm.rightShoulder -= xboxCont.RTHUMBX*3
    # Control Elbow
    mmm.rightElbow -= xboxCont.RTHUMBY*3
  
  # Activate Left Gripper
  if(xboxCont.LB):
    mmm.setLeftGrippers(180,180,180,180,180)
  else:
    mmm.setLeftGrippers(0,0,0,0,0)
    
  # Activate Right Gripper
  if(xboxCont.RB):
    mmm.setRightGrippers(180,180,180,180,180)
  else:
    mmm.setRightGrippers(0,0,0,0,0)
  
  # Clamp all values to be safe
  mmm.clampAll()  
  
  
  