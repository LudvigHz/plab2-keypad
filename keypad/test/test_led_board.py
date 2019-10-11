"""Tests for led_board"""
import time
import unittest

from keypad.led_board import LEDBoard


class LEDBoardTestCase(unittest.TestCase):
    """Test case for LEDBoard and charlieplexer"""

    def setUp(self):
        self.led_board = LEDBoard()
        self.led_board.setup()

    def test_led_board_light_single(self):
        """
        The led board should be able to enable a single LED with all params
        """
        self.led_board.light_led(1)

    def test_led_board_light_single_illegal(self):
        """
        The led board should give an exception when trying to enable an illegal led
        """
        self.assertRaises(KeyError, self.led_board.light_led, 0)
        self.assertRaises(KeyError, self.led_board.light_led, 7)

    def test_led_board_light_led_timed(self):
        """
        The led board should light an led for a given time
        """
        start = time.time()
        self.led_board.light_led(1, 5)
        self.assertAlmostEqual(time.time() - start, 5, delta=0.2)

    def test_led_board_light_multiple(self):
        """
        The led_board should light multiple leds
        """
        self.led_board.light_multiple_leds([1, 2, 3, 4])
        self.assertRaises(KeyError, self.led_board.light_multiple_leds, [0, 1, 7])
        start = time.time()
        self.led_board.light_multiple_leds([1, 2, 3], 5)
        self.assertAlmostEqual(time.time() - start, 5, delta=1)

    def test_led_board_twinkle(self):
        """
        The led_board should twinkle the leds.
        The time should be the same regardless of speed
        """
        start = time.time()
        self.led_board.twinkle_all_leds(5)
        self.assertAlmostEqual(time.time() - start, 5, delta=1)

        start = time.time()
        self.led_board.twinkle_all_leds(5, speed=0.8)
        self.assertAlmostEqual(time.time() - start, 5, delta=1)

    def test_led_board_flash(self):
        """
        The led_board should flash all the leds.
        The time should be the same regardless of speed
        """
        start = time.time()
        self.led_board.flash_all_leds(5)
        end = time.time()
        self.assertAlmostEqual(end - start, 5, delta=1)

        start = time.time()
        self.led_board.flash_all_leds(5, speed=0.8)
        end = time.time()
        self.assertAlmostEqual(end - start, 5, delta=1)
