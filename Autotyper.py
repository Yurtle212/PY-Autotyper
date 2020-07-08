import time
import random
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()  # Create the controller
Phrase = input("What do you want me to type? ")
enter = input("Press enter after? (Y/N) ")
print("Typing will start in 5 seconds")

time.sleep(5)

def type_string_with_delay(string):
    for character in string:
        keyboard.type(character)
        delay = random.uniform(0.05, 0.1)
        time.sleep(delay)

type_string_with_delay(Phrase)
if enter.lower() == "y":
    keyboard.press(Key.enter)
    time.sleep(0.1)
    keyboard.release(Key.enter)
