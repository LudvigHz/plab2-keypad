""" Module the keypad tests """

import unittest

import keypad.test.mock_GPIO as GPIO
from keypad.keypad import Keypad


class KeypadTestCase(unittest.TestCase):
    """ Tests for keypad """

    def setUp(self):
        super().setUp()
        self.keypad = Keypad()

    def test_setup(self):
        """ Test that the keypad has been set up correctly """
        self.assertEqual(self.keypad.SYMBOLS[(18, 17)], "1")
        self.assertEqual(self.keypad.SYMBOLS[(18, 27)], "3")
        self.assertEqual(self.keypad.SYMBOLS[(25, 22)], "0")

    def test_do_polling(self):
        """ Test that polling method works as expected """

        poll_result = self.keypad.do_polling()
        self.assertEqual(None, poll_result)
        GPIO.set_pin_high(17)
        poll_result = self.keypad.do_polling()
        self.assertEqual("1", poll_result)
        GPIO.set_pin_low(17)

    def test_get_next_signal(self):
        """ Test get next signal method """
        GPIO.set_pin_high(27)
        result = self.keypad.get_next_signal()
        self.assertEqual("3", result)


if __name__ == "__main__":
    unittest.main()
