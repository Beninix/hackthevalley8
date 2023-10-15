import pyautogui
from pymsgbox import *
import keyboard

def dist(point1, point2):
    total = 0
    for i in range(3):
        total += (point1[i]-point2[i])**2
    return total

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
    #Convert to int
    for j in range(3):
        codes[i][j]=int(codes[i][j])
while(True):
    keyboard.wait("a")
    #Color checking
    screen = pyautogui.screenshot()
    pixel = screen.getpixel(pyautogui.position())

    #Match color code to color name
    closest = 0 #Index of closest
    closestDist = dist(pixel, codes[0])
    print(pixel)
    for i in range(len(codes)):
        newDist = dist(pixel,codes[i])
        if(newDist<closestDist):
            closestDist = newDist
            closest = i
    alert(text=str(names[closest]), title ="Colour", button="Ok")
