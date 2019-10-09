"""File contains a mock agent to test fsm"""


class MockAgent:
    """Used to test fsm"""

    def init_passcode_entry(self, signal: str):
        """Power up"""
        print("Power up")

    def get_next_signal(self) -> str:
        """Returns next signal to fsm"""
        return "5"

    def exit_action(self):
        """Exit fsm and application"""
        print('k bye')
