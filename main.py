import pyautogui
from pymsgbox import *

#Initialize
names = []
codes = []
#Open and read file
colours = open("basic colours.txt", "r").readlines()
for i in range(len(colours)):
    #Clean endline markers
    colours[i]=colours[i].rstrip("\n")
    #Break string into desired data
    temp = colours[i].split("|")
    #Assign data to 2 parallel arrays
    names.append(temp[0])
    codes.append(temp[1].strip("()").split(","))
print(codes)
#Color checking
screen = pyautogui.screenshot()
pixel = screen.getpixel(pyautogui.position())

#Match color code to color name
closest = 0 #Index of closest
closestDist = pixel

print(pixel)
alert(text=str(pixel), title ="Colour", button="Ok")
