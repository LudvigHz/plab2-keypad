""" Module for keypad class """
import os
from time import sleep

DEBUG = os.environ.get("DEBUG") == "true"

if DEBUG:
    from RPiSim.GPIO import GPIO
else:
    import RPi.GPIO as GPIO


class Keypad:
    """ Class for checking if a key is pressed and passing characters along to the agent"""

    ROW_PINS = [18, 23, 24, 25]
    COLUMN_PINS = [17, 22, 27]
    SYMBOLS = {
        (18, 17): "1",
        (18, 22): "2",
        (18, 27): "3",
        (23, 17): "4",
        (23, 22): "5",
        (23, 27): "6",
        (24, 17): "7",
        (24, 22): "8",
        (24, 27): "9",
        (25, 17): "*",
        (25, 22): "0",
        (25, 27): "#",
    }

    def __init__(self):
        self.setup()

    def setup(self):
        """ Setup pins for use of the keypad """
        GPIO.setmode(GPIO.BCM)
        for row_pin in Keypad.ROW_PINS:
            GPIO.setup(row_pin, GPIO.OUT)
        for column_pin in Keypad.COLUMN_PINS:
            GPIO.setup(column_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        """ Poll the keypad for a signal """

        for row_pin in Keypad.ROW_PINS:
            GPIO.output(row_pin, GPIO.HIGH)
            for column_pin in Keypad.COLUMN_PINS:
                count = 0
                # Check if high 20 times in a row to avoid noise
                for i in range(20):
                    if GPIO.input(column_pin) == GPIO.HIGH:
                        count += 1
                    sleep(0.002)
                if count == 20:
                    return Keypad.SYMBOLS[(row_pin, column_pin)]

            GPIO.output(row_pin, GPIO.LOW)
        return None

    def get_next_signal(self):
        """ Poll until a key is pressed """

        key_pressed = None
        while key_pressed is None:
            key_pressed = self.do_polling()
        return key_pressed
