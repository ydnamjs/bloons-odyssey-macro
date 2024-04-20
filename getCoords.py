import pyautogui
from time import sleep

def getCoords():
    for i in range(0, 10):
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX, " ", currentMouseY)
        sleep(.5)

getCoords()