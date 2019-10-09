"""File contains unittests for Rule class"""

import unittest

from keypad.finite_state_machine.rule import (STATES, Rule, signal_is_anything,
                                              signal_is_asterisk,
                                              signal_is_digit,
                                              signal_is_square)


class MyTestCase(unittest.TestCase):
    """Tests for Rule"""

    trigger_state = STATES.INIT
    new_state = STATES.READ
    action = "placeholder"
    trigger_signal = signal_is_digit
    signal = "5"
    signal2 = "*"

    def test_signal_is_digit(self):
        """Tests the trigger signal function"""
        self.assertTrue(signal_is_digit("0"))
        self.assertTrue(signal_is_digit("9"))
        self.assertFalse(signal_is_digit("a"))

    def test_signal_is_anything(self):
        """Tests the trigger signal function"""
        self.assertTrue(signal_is_anything("a"))
        self.assertFalse(signal_is_anything(""))

    def test_signal_is_asterisk(self):
        """Tests the trigger signal function"""
        self.assertTrue(signal_is_asterisk("*"))
        self.assertFalse(signal_is_asterisk("#"))

    def test_signal_is_square(self):
        """Tests the trigger signal function"""
        self.assertTrue(signal_is_square("#"))
        self.assertFalse(signal_is_square("*"))

    def test_rule_init(self):
        """Test the init method and getters"""

        self.assertRaises(
            Exception,
            Rule,
            self.action,
            self.trigger_signal,
            self.new_state,
            self.action,
        )

        self.assertRaises(
            Exception,
            Rule,
            self.trigger_state,
            self.trigger_signal,
            self.action,
            self.action,
        )

        rule = Rule(
            self.trigger_state, self.trigger_signal, self.new_state, self.action
        )

        self.assertEqual(self.new_state, rule.get_new_state())
        self.assertEqual(self.action, rule.get_action())

    def test_match(self):
        """Test the match method of Rule"""

        rule = Rule(self.trigger_state, signal_is_digit, self.new_state, self.action)

        self.assertTrue(rule.match(self.trigger_state, self.signal))
        self.assertFalse(rule.match(self.new_state, self.signal))
        self.assertFalse(rule.match(self.new_state, self.action))
        self.assertFalse(rule.match(self.trigger_state, self.signal2))


if __name__ == "__main__":
    unittest.main()
