import pyautogui
from pymsgbox import *
import keyboard

def dist(point1, point2):
    '''
    Calculates 3D Euclidian distance (without sqrt)
    Parameters:
        point1(int[]): First point
        point2(int[]): Second point
    Returns:
        distance(int)
    '''
    total = 0
    for i in range(3):
        total += (point1[i]-point2[i])**2
    return total

#Initialize
names = []
codes = []

#Open config
config = open("config.txt", "r").readlines()

#Set the activation key
key = config[1].split("=")[1].strip()

#Detailed Colours
if(config[0].split("=")[1].strip()=="Yes"):
    colours = open("detailed colours.txt", "r").readlines()
    print("YIPEEE")    
#Basic Colours
else:
    colours = open("basic colours.txt", "r").readlines()
    
#Open and read colour definitions
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

#Colour checking
while(True):
    keyboard.wait(key)
    #Read the pixel the mouse is at
    screen = pyautogui.screenshot()
    pixel = screen.getpixel(pyautogui.position())
    #Match color code to color name
    closest = 0 #Index of closest
    closestDist = dist(pixel, codes[0])
    #Check which colour is the closest
    for i in range(len(codes)):
        newDist = dist(pixel,codes[i])
        if(newDist<closestDist):
            closestDist = newDist
            closest = i
    #Send the message
    alert(text=str(names[closest]), title ="Colour", button="Ok")
