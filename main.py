from dataclasses import dataclass
import pyautogui
from time import sleep

### CONSTANTS

@dataclass
class Position:
    x: int
    y: int

SAUDA = Position(1415, 197)
BOOMERANG = Position(1428, 288)
SNIPER = Position(1429, 413)

### HELPER FUNCTIONS

def buyTopR():
    pyautogui.moveTo(1281, 422)
    pyautogui.click()
    sleep(.25)

def buyTopL():
    pyautogui.moveTo(267, 408)
    pyautogui.click()
    sleep(.25)

def buyMidR():
    pyautogui.moveTo(1270, 545)
    pyautogui.click()
    sleep(.25)

def buyMidL():
    pyautogui.moveTo(280, 534)
    pyautogui.click()
    sleep(.25)

def buyBotR():
    pyautogui.moveTo(1278, 634)
    pyautogui.click()
    sleep(.25)

def buyBotL():
    pyautogui.moveTo(280, 678)
    pyautogui.click()
    sleep(.25)

def startLevel():
    pyautogui.moveTo(1508, 839)
    pyautogui.click()
    sleep(.1)
    pyautogui.click()

### MAP1
def playMap1():
    startLevel()
    placeSaudaMap1()
    sleep(150)
    placeBoomerangMap1()
    sleep(130)
    placeSniperMap1()

def placeSaudaMap1():
    pyautogui.moveTo(SAUDA.x, SAUDA.y)
    pyautogui.click()
    pyautogui.moveTo(255, 241)
    pyautogui.click()

def placeBoomerangMap1():
    pyautogui.moveTo(BOOMERANG.x, BOOMERANG.y)
    pyautogui.click()
    pyautogui.moveTo(245, 181)
    pyautogui.click()
    pyautogui.click()
    sleep(.5)
    buyBotR()
    buyBotR()
    buyTopR()
    buyTopR()
    buyTopR()
    buyTopR()
    sleep(.2)
    pyautogui.moveTo(245, 181)
    pyautogui.click()

def placeSniperMap1():
    pyautogui.moveTo(SNIPER.x, SNIPER.y)
    pyautogui.click()
    pyautogui.moveTo(181, 739)
    pyautogui.click()
    pyautogui.click()
    sleep(.5)
    buyBotR()
    buyBotR()
    buyTopR()
    buyTopR()
    buyTopR()
    buyTopR()
    sleep(.2)
    pyautogui.moveTo(181, 739)
    pyautogui.click()

### MAP2

def playMap2():
    startLevel()
    placeSaudaMap2()
    placeBoomerangMap2()
    sleep(20)
    placeBoomerangMap2_2()
    sleep(40)
    placeSniperMap2()
    sleep(30)
    upgradeBoomerangMap2()
    sleep(90)
    upgradeSniperMap2()

def placeSaudaMap2():
    pyautogui.moveTo(SAUDA.x, SAUDA.y)
    pyautogui.click()
    pyautogui.moveTo(329, 162)
    pyautogui.click()

def placeBoomerangMap2():
    pyautogui.moveTo(BOOMERANG.x, BOOMERANG.y)
    pyautogui.click()
    pyautogui.moveTo(1065, 748)
    pyautogui.click()
    pyautogui.click()
    sleep(20)
    buyBotL()
    buyBotL()
    buyTopL()
    sleep(10)
    buyTopL()
    sleep(20)
    buyTopL()
    pyautogui.moveTo(1065, 748)
    pyautogui.click()

def placeBoomerangMap2_2():
    pyautogui.moveTo(BOOMERANG.x, BOOMERANG.y)
    pyautogui.click()
    pyautogui.moveTo(245, 163)
    pyautogui.click()
    pyautogui.click()
    sleep(10)
    buyBotR()
    buyBotR()
    sleep(10)
    buyTopR()
    buyTopR()
    sleep(20)
    buyTopR()
    pyautogui.moveTo(245, 163)
    pyautogui.click()

def placeSniperMap2():
    pyautogui.moveTo(SNIPER.x, SNIPER.y)
    pyautogui.click()
    pyautogui.moveTo(702, 448)
    pyautogui.click()
    pyautogui.click()
    buyTopL()
    buyTopL()
    buyMidL()
    buyMidL()

def upgradeBoomerangMap2():
    pyautogui.moveTo(1065, 748)
    pyautogui.click()
    buyTopL()
    pyautogui.moveTo(1065, 748)
    pyautogui.click()

def upgradeSniperMap2():
    pyautogui.moveTo(702, 448)
    pyautogui.click()
    buyTopL()
    buyTopL()
    pyautogui.moveTo(702, 448)
    pyautogui.click()

### MAIN

def main():
    sleep(3)
    #playMap1()
    playMap2()

main()