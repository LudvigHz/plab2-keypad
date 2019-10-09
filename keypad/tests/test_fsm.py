"""File contains unittests for finite state machine"""

import unittest

from keypad.finite_state_machine.finite_state_machine import FiniteStateMachine
from keypad.finite_state_machine.rule import Rule, signal_is_anything
from keypad.mock_agent import MockAgent


class MyTestCase(unittest.TestCase):
    """Tests for finite state machine"""

    def setUp(self):
        """Setup run before each test"""
        self.agent = MockAgent()
        self.fsm = FiniteStateMachine(self.agent)
        self.rule = Rule('INIT', signal_is_anything, 'READ', self.agent.init_passcode_entry)
        self.rule2 = Rule('READ', signal_is_anything, 'READ', self.agent.init_passcode_entry)

    def test_add_rule(self):
        """Test add rule"""
        first_length = len(self.fsm._rule_list)
        self.fsm._add_rule(self.rule)
        second_length = len(self.fsm._rule_list)
        self.assertTrue((second_length - first_length) == 1)

    def test_get_next_signal(self):
        """Test that fsm fetches signal from agent"""
        self.fsm._get_next_signal()
        self.assertTrue(self.fsm._current_signal == '5')

    def test_apply_rule(self):
        """Test apply rule"""
        self.fsm._current_state = 'INIT'
        self.fsm._current_signal = '5'

        self.assertTrue(self.fsm._apply_rule(self.rule))
        self.assertFalse(self.fsm._apply_rule(self.rule2))

    def test_fire_rule(self):
        """Tests fire rule"""


if __name__ == '__main__':
    unittest.main()
