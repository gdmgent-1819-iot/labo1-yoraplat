from sense_hat import SenseHat
import random
import time

sense = SenseHat()
x = 0
y = 0

speed = int(input('Speed (s): '))
colour_r = int(input('R: '))
colour_g = int(input('G: '))
colour_b = int(input('B: '))



def loop():
    while True:
        
        sense.clear()

        for y in range(0, 7):
            
            ranX = random.randint(0, 3)
            dotX = random.randint(0, 1)
            if dotX == 1:
                sense.set_pixel(ranX, y, [colour_r, colour_g, colour_b])
                sense.set_pixel(7 - ranX, y, [colour_r, colour_g, colour_b])
        y = y + 1
        time.sleep(speed)

loop()



"""
    for y in range(0, 8):
        ranY = random.randint(0, 4)
        dotY = random.randint(0, 1)
        if dotY == 1:
            sense.set_pixel(x, ranY, [255, 0, 0])
"""

