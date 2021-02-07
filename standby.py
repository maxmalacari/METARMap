#!/usr/bin/python3

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 50, brightness=0.005)

pixels[36] = (0,255,0)
pixels.show()

print("Standby")
