from sense_hat import SenseHat
import random
import time

sense = SenseHat()


x = 0

letters = ["N", "M", "D"]

for x in range(0,3):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sense.show_letter(letters[x], text_colour=[r, g, b])
    x = x + 1
    time.sleep(0.5)
    sense.clear()


