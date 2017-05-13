# Write a script that detects and prints out your monitor resolution.

# Mac

import AppKit
print 
[(screen.frame().size.width, screen.frame().size.height)
    for screen in AppKit.NSScreen.screens()]


# Windows
# from screeninfo import get_monitors

# w = get_monitors()[0].width
# h = get_monitors()[0].height
# print ('Width: %d, Height: %d') %(w,h)