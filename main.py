import pyautogui
from pymsgbox import *
names = []
codes = []
colours = open("basic colours.txt", "r").readlines()
for colour in range(len(colours)):
    colours[colour]=colours[colour].rstrip("\n")
print(colours)


screen = pyautogui.screenshot()
pixel = screen.getpixel(pyautogui.position())
alert(text=str(pixel), title ="Colour", button="Ok")
