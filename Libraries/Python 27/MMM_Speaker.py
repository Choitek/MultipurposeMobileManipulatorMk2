#Import Libraries
import OSC



# The Speaker Class that connects to the
# Customizable Robot Face Module.
class Speaker:
  # Initializes an OSC connection to the Speaker
  def __init__(self):
    self.client = OSC.OSCClient()
    self.client.connect(('127.0.0.1',2000))
  # Sends an OSC Message containing the text
  def speak(self,textToSpeak):
    oscMessage = OSC.OSCMessage()
    oscMessage.setAddress("/speech")
    oscMessage.append(textToSpeak)
    self.client.send(oscMessage) 