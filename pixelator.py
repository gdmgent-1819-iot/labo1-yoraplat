from sense_hat import SenseHat
import time
import random
sense = SenseHat()



"""
x = 0

while x <= 64:

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    print(x)
    x = x + 1
    
"""

sense.clear()
z = 0
x = 0
y = 0

while True:
    for z in range(64):
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        if z == 63:
            z = 0
            x = 0
            y = 0
            sense.clear()
            sense.set_pixel(x, y , [r, g , b])
            print("x: {}, y: {}, z: {}".format(x,y,z))


        elif z <= 64:        
            if x < 8:
                sense.set_pixel(x, y , [r, g , b])
                x = x + 1
                # x < 8
                
            elif x == 8:
                x = 0
                # x = 8 -> x = 0
                
                if y < 8:
                    
                    y = y + 1
                    sense.set_pixel(x, y , [r, g , b])
                    x = x + 1
                elif y == 8:
                    y = 0
            print("x: {}, y: {}, z: {}".format(x,y,z))
            time.sleep(0.1)

    # Geen easing
