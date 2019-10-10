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
    1: {"in": 20, "out": 21},
    2: {"in": 21, "out": 20},
    3: {"in": 21, "out": 19},
    4: {"in": 19, "out": 21},
    5: {"in": 19, "out": 20},
    6: {"in": 20, "out": 19},
}


class LEDBoard:
    """
    Class for controlling the 6 LEDs
    """

    def __init__(self, pins=GPIO_PINS):
        self.charlieplexer = Charlieplexer(pins)

    def setup(self):
        """Setup the led board. REQUIRED"""
        GPIO.setmode(GPIO.BCM)

    def light_led(self, led_number, seconds=None):
        """Light LED nr <led_number>. Optional param seconds"""
        self.charlieplexer.enable_single(led_number)
        if seconds:
            time.sleep(seconds)
            self.turn_off_all_leds()

    def turn_off_all_leds(self):
        """Turn off all leds"""
        self.charlieplexer.disable_all()

    def flash_all_leds(self, seconds, speed=0.5):
        """Flash all LEDs for <time> seconds. Optional param speed (lower is faster)"""
        start = time.time()
        while time.time() - start < seconds:
            self.charlieplexer.enable_all(speed)
            time.sleep(speed)

    def twinkle_all_leds(self, seconds, *args, **kwargs):
        """Twinkle all LEDs for <time> seconds in order. Optional param speed (lower is faster)"""
        speed = kwargs.get("speed", 0.3)
        order = kwargs.get("order", list(range(1, 7)))
        start = time.time()
        while time.time() - start < seconds:
            for led in order:
                self.light_led(led)
                time.sleep(speed)

    def start_up_sequence(self):
        """Start the start-up sequence"""
        for i, j in range(3, 0, -1), range(4, 7):
            self.charlieplexer.enable_multiple([i, j], 0.2)
        self.flash_all_leds(2, 0.1)

    def shut_down_sequence(self):
        """Start the shut-down sequence"""
        order = list(range(1, 7))
        for i in range(4):
            self.twinkle_all_leds(order)
            order.reverse()
