from sense_hat import SenseHat
import random
sense = SenseHat()

sense.clear()
rb = random.randint(0, 160)
gb = random.randint(0, 160)
bb = random.randint(0, 160)


rt = random.randint(160, 255)
gt = random.randint(160, 255)
bt = random.randint(160, 255)

sense.show_message('Hello! We are New Media Development :)', text_colour=[rt, gt, bt], back_colour=[rb, gb, bb])
