from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# 590 500
# 690 500
# 780 500
# 870 500

x = [791, 951, 1111]
RedColor = (221, 68, 51)
WhiteColor = (221, 68, 51)
y = 570

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def SuperClick(x1, y1, x2, y2):
    while pyautogui.pixel(x1, y1) == RedColor:
        y1 = y1 + 2
    y1 = y1 + 1
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.SetCursorPos((x2, y2))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def cal(n, pos, whereto, extra):
    if n == 1:
        SuperClick(x[pos], y, x[whereto], y)
        return
    cal(n-1, pos, extra, whereto)
    SuperClick(x[pos], y, x[whereto], y)
    cal(n-1, extra, whereto, pos)
    return

yes = True

while keyboard.is_pressed('q') == False:
    if(keyboard.is_pressed('w') == True):
        #print(pyautogui.pixel(x[0], y))
        cal(7, 0, 2, 1)
        yes = False
