"""File contains unittests for finite state machine"""

import unittest

from keypad.finite_state_machine.finite_state_machine import FiniteStateMachine
from keypad.finite_state_machine.rule import (
    STATES, Rule, signal_is_anything, signal_is_digit)
from keypad.mock_agent import MockAgent


class MyTestCase(unittest.TestCase):
    """Tests for finite state machine"""

    def setUp(self):
        """Setup run before each test"""
        self.first_state = STATES.INIT
        self.second_state = STATES.READ
        self.end_state = STATES.END

        self.agent = MockAgent()
        self.fsm = FiniteStateMachine(self.agent)
        self.rule = Rule(
            self.first_state,
            signal_is_digit,
            self.second_state,
            self.agent.init_passcode_entry,
        )

        self.rule2 = Rule(
            self.second_state,
            signal_is_digit,
            self.end_state,
            self.agent.init_passcode_entry,
        )

    def test_add_rule(self):
        """Test add rule"""
        first_length = len(self.fsm._rule_list)
        self.fsm.add_rule(self.rule)
        second_length = len(self.fsm._rule_list)
        self.assertTrue((second_length - first_length) == 1)

    def test_get_next_signal(self):
        """Test that fsm fetches signal from agent"""
        self.fsm._get_next_signal()
        self.assertTrue(self.fsm._current_signal == "5")

    def test_apply_rule(self):
        """Test apply rule"""
        self.fsm._current_state = self.first_state
        self.fsm._current_signal = "5"

        self.assertTrue(self.fsm._apply_rule(self.rule))
        self.assertFalse(self.fsm._apply_rule(self.rule2))

    def test_fire_rule(self):
        """Tests fire rule"""
        self.fsm._fire_rule(self.rule)
        self.assertEqual(self.fsm._current_state, self.second_state)

    def test_run_rules(self):
        """Tests the iteration of rules"""
        self.fsm._current_signal = "5"
        self.fsm.add_rule(self.rule2)
        self.fsm._run_rules()

        self.fsm._current_signal = "*"
        self.assertRaises(Exception, self.fsm._run_rules)

    def test_main_loop(self):
        """Test the main loop"""
        self.fsm.add_rule(self.rule2)
        self.fsm.main_loop()


if __name__ == "__main__":
    unittest.main()
