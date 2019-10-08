"""File contains unittests for Rule class"""

import unittest

from keypad.finite_state_machine.rule import Rule


class MyTestCase(unittest.TestCase):
    """Tests for Rule"""

    trigger_state = 'INIT'
    new_state = 'READ'
    action = 'placeholder'
    trigger_signal = '@'

    def test_rule_init(self):
        """Test the init method and getters"""

        self.assertRaises(
            Exception,
            Rule,
            self.action,
            self.trigger_signal,
            self.new_state,
            self.action)

        self.assertRaises(
            Exception,
            Rule,
            self.trigger_state,
            self.trigger_signal,
            self.action,
            self.action)

        rule = Rule(
            self.trigger_state,
            self.trigger_signal,
            self.new_state,
            self.action)

        self.assertEqual(self.new_state, rule.get_new_state())
        self.assertEqual(self.action, rule.get_action())

    def test_match(self):
        """Test the match method of Rule"""

        rule = Rule(
            self.trigger_state,
            self.trigger_signal,
            self.new_state,
            self.action)

        self.assertTrue(rule.match(self.trigger_state, self.trigger_signal))
        self.assertFalse(rule.match(self.new_state, self.trigger_signal))
        self.assertFalse(rule.match(self.new_state, self.action))


if __name__ == '__main__':
    unittest.main()
