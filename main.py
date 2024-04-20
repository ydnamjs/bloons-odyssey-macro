from dataclasses import dataclass
import pyautogui
from time import sleep

### CONSTANTS

NUMTIMES = 2

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

def startOdyssey():
    pyautogui.moveTo(1464, 802)
    pyautogui.click()
    sleep(.5)
    pyautogui.click()
    sleep(5)

def completeLevel():
    pyautogui.moveTo(699, 657)
    pyautogui.click()
    sleep(5)

def startNext():
    pyautogui.moveTo(1464, 802)
    pyautogui.click()
    sleep(5)

def finishOdyssey():
    pyautogui.moveTo(804, 707)
    pyautogui.click()
    sleep(5)
    pyautogui.moveTo(804, 704)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(1464, 802)
    pyautogui.click()
    sleep(2)

### MAP1
def playMap1():
    startLevel()
    placeSaudaMap1()
    sleep(150)
    placeBoomerangMap1()
    sleep(130)
    placeSniperMap1()
    sleep(10)
    completeLevel()

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
    sleep(30)
    completeLevel()

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

### MAP3

def playMap3():
    startLevel()
    placeSaudaMap3()
    placeBoomerangMap3()
    sleep(75)
    placeSniperMap3()
    sleep(40)
    completeLevel()

def placeSaudaMap3():
    pyautogui.moveTo(SAUDA.x, SAUDA.y)
    pyautogui.click()
    pyautogui.moveTo(989, 401)
    pyautogui.click()

def placeBoomerangMap3():
    pyautogui.moveTo(BOOMERANG.x, BOOMERANG.y)
    pyautogui.click()
    pyautogui.moveTo(985, 492)
    pyautogui.click()
    pyautogui.click()
    buyBotL()
    sleep(15)
    buyBotL()
    sleep(40)
    buyTopL()
    buyTopL()
    buyTopL()
    sleep(100)
    buyTopL()
    pyautogui.moveTo(985, 492)
    pyautogui.click()

def placeSniperMap3():
    pyautogui.moveTo(SNIPER.x, SNIPER.y)
    pyautogui.click()
    pyautogui.moveTo(605, 402)
    pyautogui.click()
    pyautogui.click()
    buyTopR()
    buyTopR()
    buyTopR()
    buyMidR()
    buyMidR()
    sleep(50)
    buyTopR()
    pyautogui.moveTo(605, 402)
    pyautogui.click()

### MAIN

def main():
    sleep(5)

    for i in range(0, NUMTIMES):
        startOdyssey()
        sleep(5)
        playMap1()
        startNext()
        sleep(5)
        playMap2()
        startNext()
        sleep(5)
        playMap3()
        finishOdyssey()

main()