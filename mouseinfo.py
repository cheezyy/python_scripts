#! python3
# mouseinfo.py - Display the mouse current position & color code of pixel under cursor
# Chad Meadowcroft 2018 - Adapted from https://automatetheboringstuff.com/

import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        pixelColour = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColour[0]).rjust(3)
        positionStr += ', ' + str(pixelColour[1]).rjust(3)
        positionStr += ', ' + str(pixelColour[2]).rjust(3) + ')'

        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)   # Deletes the previous coordinates
except KeyboardInterrupt:
    print('\nDone')