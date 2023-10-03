# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import random
import time

import board
import displayio
import framebufferio
import rgbmatrix

displayio.release_displays()

MATRIX = rgbmatrix.RGBMatrix(
    width=32,
    height=32,
    bit_depth=3,
    rgb_pins=[board.R0, board.G0, board.B0, board.R1, board.G1, board.B1],
    addr_pins=[board.ROW_A, board.ROW_B, board.ROW_C, board.ROW_D],
    clock_pin=board.CLK,
    latch_pin=board.LAT,
    output_enable_pin=board.OE,
)

# Associate matrix with a Display to use displayio features
DISPLAY = framebufferio.FramebufferDisplay(MATRIX, auto_refresh=False, rotation=0)

# Load BMP image, create Group and TileGrid to hold it
FILENAME = "bmp/2.bmp"


BITMAP = displayio.OnDiskBitmap(FILENAME)
TILEGRID = displayio.TileGrid(
    BITMAP,
    pixel_shader=BITMAP.pixel_shader,
    tile_width=BITMAP.width,
    tile_height=BITMAP.height,
)

GROUP = displayio.Group()
GROUP.append(TILEGRID)
DISPLAY.show(GROUP)
DISPLAY.refresh()

# Nothing interactive, just hold the image there
while True:
    pass
