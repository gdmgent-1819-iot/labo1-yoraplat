from sense_hat import SenseHat
import time
sense = SenseHat()

S = [255, 204, 102]  # Skin
B = [0, 120, 255]    # Blue
R = [255,0 ,0]       # Red
O = [0, 0, 0]        # White


mario = [
O, O, O, R, R, O, O, O,
O, O, O, S, S, O, O, O,
O, O, R, B, O, O, O, O,
O, S, O, B, R, S, O, O,
O, O, O, B, O, O, O, O,
O, O, O, B, B, O, O, O,
O, O, B, O, B, O, O, O,
O, O, S, O, S, O, O, O
]

mario_jump = [
O, O, O, S, S, O, O, O,
O, O, R, B, O, O, O, O,
O, S, O, B, R, S, O, O,
O, O, O, B, O, O, O, O,
O, O, O, B, B, O, O, O,
O, O, B, O, B, O, O, O,
O, O, S, O, S, O, O, O,
O, O, O, O, O, O, O, O,
]

sense.clear()
sense.set_pixels(mario)


while True: # Always true == infinite loop
    event = sense.stick.wait_for_event()
    if event.direction == 'up' and event.action == "pressed":
       sense.clear()
       sense.set_pixels(mario_jump)
       time.sleep(0.5)
       sense.set_pixels(mario)
            
        
