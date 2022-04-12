import argparse
import time

import pyautogui

#Parse the inputed argument
parser = argparse.ArgumentParser(description='Muonline clicker')
parser.add_argument('clickcount', type=int, help='The clickcount param is required.')
args = parser.parse_args()
print(f"Click count to be executed: {args.clickcount}")

if args.clickcount <= 0 or args.clickcount > 100000:
    parser.error("pos_arg cannot be larger than 100k or less than 1")

time.sleep(2)
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(f'Windows viewport: {screenWidth}x{screenHeight}')

currentMouseX, currentMouseY = pyautogui.position()
print(f'Mouse Initial Position: {currentMouseX}x{currentMouseY}')

pyautogui.click('unique_button.png') 

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(currentMouseX, currentMouseY + 220) 
for cnt in range(1, args.clickcount):
    pyautogui.mouseDown()
    pyautogui.mouseUp()
