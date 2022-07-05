#Take screenshot and save an image file with timestamp and GUID as a filename
import time 
import pyautogui
import uuid
myScreenshot = pyautogui.screenshot()
myGUID = str(uuid.uuid4())
myFilename ='/home/pi/Documents/'+time.strftime("%U%m%d-%H%M%S"+myGUID+'.jpg')

print(myGUID)
print(myFilename)

myScreenshot.save(myFilename)
