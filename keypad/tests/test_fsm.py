"""File contains unittests for finite state machine"""

import unittest

from keypad.finite_state_machine.finite_state_machine import FiniteStateMachine
from keypad.kpc_agent import KPCAgent


class MyTestCase(unittest.TestCase):
    """Tests for finite state machine"""

    def test_init(self):
        agent = KPCAgent
        fsm = FiniteStateMachine(agent)
        fsm.main_loop()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
