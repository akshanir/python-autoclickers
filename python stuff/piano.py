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
time.sleep(1)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(600, 630)[0] == 0:
        click(600, 630)
    if pyautogui.pixel(500, 650)[0] == 0:
        click(500, 650)
    if pyautogui.pixel(430, 607)[0] == 0:
        click(430, 607)
    if pyautogui.pixel(350, 620)[0] == 0:
        click(350, 620)
    print(win32api.GetCursorPos())


