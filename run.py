import time

import pyautogui

time.sleep(2)
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(f'Windows viewport: {screenWidth}x{screenHeight}')

currentMouseX, currentMouseY = pyautogui.position()
print(f'Mouse Initial Position: {currentMouseX}x{currentMouseY}')

pyautogui.click('unique_button.png') # Find where button.png appears on the screen and click it.

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(currentMouseX, currentMouseY + 220) 
for cnt in range(1,10):
    pyautogui.mouseDown()
    pyautogui.mouseUp()
