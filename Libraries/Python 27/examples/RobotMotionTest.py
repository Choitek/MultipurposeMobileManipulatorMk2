'''
The Robot Motion Test is a simple diagnostic test to see whether all motors are working properly.
'''

# Import all libraries
from MMM import MMM #Make sure you have pyserial 27 installed! https://pypi.python.org/pypi/pyserial/2.7
import threading
import time
import sys

#--------------INITIALIZATION------------------#
#Change 'COM3' to your COM Port. This is something like "/dev/ttyACM0" on Linux and Mac.
#If you don't know what your COM Port is, plug in the USB to the Arduino Mega 2560 and
#follow the instructions in this link: https://www.arduino.cc/en/Guide/Troubleshooting#toc1
mmm = MMM('COM3') 

#give some time to connect.
time.sleep(4)              

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

# 1. Go to Initial Pose.
mmm.setWheelVelocity(0,0)
mmm.rotateShoulders(100,100)
mmm.rotateElbows(-60,-60)
mmm.extendArms(0,0)
mmm.setLeftGrippers(0,0,0,0,0)
mmm.setRightGrippers(0,0,0,0,0)
time.sleep(2)

###-----------SHOULDERS------------###
# 2. Rotate shoulders out. (ranges from 0 degrees to 120 degrees)
mmm.rotateShoulders(0,0)
time.sleep(2)
# 3. Rotate shoulders in.
mmm.rotateShoulders(120,120)
time.sleep(2)
# 4. Rotate shoulders to middle. 
mmm.rotateShoulders(100,100)

###-----------ELBOWS------------###
# 5. Move elbows up (ranges from -60 degrees to 60 degrees)
mmm.rotateElbows(60,60)
time.sleep(2)
# 6. Cross elbows up and down once.
mmm.rotateElbows(-30,30)
time.sleep(1)
# 7. Cross elbows up and down twice.
mmm.rotateElbows(30,-30)
time.sleep(1)
# 8. Cross elbows up and down thrice.
mmm.rotateElbows(-30,30)
time.sleep(1)
# 9. Move elbows down 
mmm.rotateElbows(-60,-60)
time.sleep(1)

###-----------WHEELS------------###
# 10. Turn Left. (ranges from -0.18 degrees to 0.18 meters/second)
mmm.setWheelVelocity(-.18,.18)
time.sleep(2.5)
# 11. Turn Right.
mmm.setWheelVelocity(.18,-.18)
time.sleep(5)
# 12. Turn Left.
mmm.setWheelVelocity(-.18,.18)
time.sleep(2.5)
# 13. Move Forward.
mmm.setWheelVelocity(.18,.18)
time.sleep(2)
# 14. Move Backward.
mmm.setWheelVelocity(-.18,-.18)
time.sleep(2)
# 15. Stop.
mmm.setWheelVelocity(0,0)
time.sleep(1)

###-----------GRIPPERS------------###
# 10. Open all grippers (ranges from 0 degrees to 180 degrees)
mmm.setLeftGrippers(180,180,180,180,180)
mmm.setRightGrippers(180,180,180,180,180)
time.sleep(2)
# 10. Close all grippers
mmm.setLeftGrippers(0,0,0,0,0)
mmm.setRightGrippers(0,0,0,0,0)
time.sleep(2)

# Finish the motion test.
mmm.setWheelVelocity(0.0,0.0)
time.sleep(1)

# Close the connection.
mmm.ser.close()
quit()   









