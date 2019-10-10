"""Module containing utilities"""
import os
from time import time

DEBUG = os.environ.get("DEBUG") == "true"

if DEBUG:
    from RPiSim.GPIO import GPIO
else:
    import RPi.GPIO as GPIO


class Charlieplexer:
    """
    Utility class for interacting with the charlieplexed LED board
    """

    def __init__(self, pins):
        self._pins = pins
        self._available_pins = {i["in"] for i in pins.values()}

    def enable_single(self, pin):
        """Enable a single pin on the charlieplexed board"""
        inpin = self._pins[pin]["in"]
        outpin = self._pins[pin]["out"]
        ignorepin = [i for i in list(self._available_pins) if i not in {inpin, outpin}][
            0
        ]
        GPIO.setup(ignorepin, GPIO.IN)
        GPIO.setup(outpin, GPIO.OUT)
        GPIO.setup(inpin, GPIO.OUT)
        GPIO.output(inpin, GPIO.LOW)
        GPIO.output(outpin, GPIO.HIGH)

    def disable_all(self):
        """Disable all pins by setting then to IN"""
        for pin in self._available_pins:
            GPIO.setup(pin, GPIO.IN)

    def enable_all(self, seconds):
        """Hacky method for enabling all pins for a given time"""
        start = time()
        while time() - start < seconds:
            for pin in self._pins.keys():
                self.enable_single(pin)
        self.disable_all()  # reset state
