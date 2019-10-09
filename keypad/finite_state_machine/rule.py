"""File contains the rule class used in finite_state_machine"""


# The legal states
STATES = ["INIT", "READ", "VERIFY", "ACTIVE", "READ2", "READ3", "END"]


class Rule:
    """The rule objects that are checked and fired in the finite_state_machine"""

    _trigger_state = None
    _trigger_signal = None
    _new_state = None
    _action = None

    def __init__(self, trigger_state: str, trigger_signal: str, new_state: str, action):
        if trigger_state not in STATES or new_state not in STATES:
            raise Exception("ILLEGAL STATE CHOSEN")

        self._trigger_state = trigger_state
        self._trigger_signal = trigger_signal
        self._new_state = new_state
        self._action = action

    def match(self, state: str, signal: str) -> bool:
        """Checks if the rule fires on the given state and symbol"""
        if self._trigger_state == state and self._trigger_signal == signal:
            return True
        return False

    def get_new_state(self) -> str:
        """Gets the next state"""
        return self._new_state

    def get_action(self):
        """Gets the action"""
        return self._action
