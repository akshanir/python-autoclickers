from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import * 

replaybtn = (959, 408)
dinosaur = (702, 433)
def restartGame():
    pyautogui.click(replaybtn)
    print("I just clicked play")

def image_grab():
    box = (dinosaur[0]+55, dinosaur[1], dinosaur[0] + 90      , dinosaur[1] + 5)
    image = ImageGrab.grab(box)
    grayImage =ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')  

time.sleep(4)
restartGame()

while True:
        if(image_grab() != 422):     
            pressSpace()
            time.sleep(0.1)


