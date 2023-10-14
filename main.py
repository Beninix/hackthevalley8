import pyautogui
from pymsgbox import *
screen = pyautogui.screenshot()
pixel = screen.getpixel(pyautogui.position())
alert(text=str(pixel), title ="Color", button="Ok")
