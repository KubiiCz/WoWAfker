from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(10)

while True:
    keyboard.press('w')
    time.sleep(3)
    keyboard.release('w')
    keyboard.press('s')
    time.sleep(5)
    keyboard.release('s')