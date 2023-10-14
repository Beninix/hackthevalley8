import pyautogui
screen = pyautogui.screenshot()
pixel = screen.getpixel(pyautogui.position())

print(pixel)
