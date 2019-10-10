"""
Module containing LEDBoard controller class
"""
import time

from keypad.utils import Charlieplexer

try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO

GPIO_PINS = {
    1: {"in": 21, "out": 20},
    2: {"in": 20, "out": 21},
    3: {"in": 21, "out": 19},
    4: {"in": 19, "out": 21},
    5: {"in": 20, "out": 19},
    6: {"in": 19, "out": 20},
}


class LEDBoard:
    """
    Class for controlling the 6 LEDs
    """

    def __init__(self, pins=GPIO_PINS):
        self.charlieplexer = Charlieplexer(pins)

    def setup(self):
        GPIO.setmode(GPIO.BCM)

    def light_led(self, led_number):
        """Light LED nr <led_number>"""
        self.charlieplexer.enable_single(led_number)

    def flash_all_leds(self, seconds, speed=0.5):
        """Flash all LEDs for <time> seconds. Optional param speed (lower is faster)"""
        start = time.time()
        while time.time() - start < seconds:
            self.charlieplexer.enable_all(speed)
            time.sleep(speed)

    def twinkle_all_leds(self, seconds, speed=0.3):
        """Twinkle all LEDs for <time> seconds in order. Optional param speed (lower is faster)"""
        start = time.time()
        while time.time() - start < seconds:
            for led in range(1, 7):
                self.light_led(led)
                time.sleep(speed)
