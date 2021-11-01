import time
from pymata4 import pymata4  # installed pymata4

triggerPin = 11
echoPin = 12
ledPin = 13
board = pymata4.Pymata4()

def the_callback(data):
    print("distance:", data[2], "cm")
    if data[2] <= 6:
        board.digital_write(13, 1)
    else:
        board.digital_write(13, 0)

board.set_pin_mode_sonar(triggerPin, echoPin, the_callback)
board.set_pin_mode_digital_output(ledPin)

while True:
    try:
        time.sleep(1)
        board.sonar_read(triggerPin)
    except Exception:
        board.shutdown()
