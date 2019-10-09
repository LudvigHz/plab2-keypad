"""File contains a mock agent to test fsm"""


class MockAgent:
    """Used to test fsm"""

    def init_passcode_entry(self):
        """Power up"""
        print('Power up')

    def get_next_signal(self) -> str:
        """Returns next signal to fsm"""
        return '5'
