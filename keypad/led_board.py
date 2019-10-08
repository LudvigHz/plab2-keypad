"""
Module containing LEDBoard controller class
"""
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    from RPiSim.GPIO import GPIO


class LEDBoard:
    """
    Class for controlling the 6 LEDs
    """

    GPIO_PINS = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def __init__(self, pins={}):
        self.GPIO_PINS = LEDBoard.GPIO_PINS.update(pins)

    def setup(self):
        GPIO.setmode(GPIO.BCM)

    def light_led(self, led_number):
        """Light LED nr <led_number>"""
        for pin in [pin for led, pin in self.GPIO_PINS if led != led_number]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        GPIO.setup(self.GPIO_PINS[led_number], GPIO.OUT)
        GPIO.output(self.GPIO_PINS[led_number], GPIO.HIGH)

    def light_all_leds(self):
        """Turn all LEDs on"""
        for pin in self.GPIO_PINS.items():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def turn_off_all_leds(self):
        """Turn all LEDs off"""
        for pin in self.GPIO_PINS.items():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def flash_all_leds(self, seconds):
        """Flash all LEDs for <time> seconds"""
        start = time.time()
        while time.time() - start < seconds:
            self.light_all_leds()
            time.sleep(0.5)  # Can be tweaked
            self.turn_off_all_leds()
            time.sleep(0.5)

    def twinkle_all_leds(self, seconds):
        """Twinkle all LEDs for <time> seconds in order"""
        start = time.time()
        while time.time() - start < seconds:
            for led in self.GPIO_PINS.keys():
                self.light_led(led)
                time.sleep(0.3)  # Can be tweaked
