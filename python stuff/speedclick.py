from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#590 500
#690 500
#780 500
#870 500
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if(keyboard.is_pressed('w') == True):
        click(800, 500)



