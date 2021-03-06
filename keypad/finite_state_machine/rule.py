"""File contains the rule class used in finite_state_machine functions for trigger signal and the
legal states"""
from keypad import constants


class STATES:
    """The legal states for the finite state machine"""

    INIT = "INIT"
    READ = "READ"
    VERIFY = "VERIFY"
    ACTIVE = "ACTIVE"
    READ2 = "READ2"
    READ3 = "READ3"
    END = "END"
    TIME = "TIME"
    LED = "LED"
    LOGOUT = "LOGOUT"


class Rule:
    """The rule objects that are checked and fired in the finite_state_machine. The _trigger_signal
    is a function that returns true for the signals that trigger the rule"""

    _trigger_state = None
    _trigger_signal = None
    _new_state = None
    _action = None

    def __init__(self, trigger_state: str, trigger_signal, new_state: str, action=None):
        if not hasattr(STATES, trigger_state) or not hasattr(STATES, new_state):
            raise ValueError("ILLEGAL STATE CHOSEN")

        self._trigger_state = trigger_state
        self._trigger_signal = trigger_signal
        self._new_state = new_state
        self._action = action

    def match(self, state: str, signal: str) -> bool:
        """Checks if the rule fires on the given state and symbol"""
        if self._trigger_state == state and self._trigger_signal(signal):
            return True
        return False

    @property
    def new_state(self) -> str:
        """Gets the next state"""
        return self._new_state

    @property
    def action(self):
        """Gets the action"""
        return self._action

    @property
    def trigger_signal(self):
        """Gets the trigger signal"""
        return self._trigger_signal


def signal_is_digit(signal: str) -> bool:
    """Checks if the signal is a digit"""
    return 48 <= ord(signal) <= 57


def signal_is_anything(signal: str) -> bool:
    """Always returns true, as long as signal isn't empty"""
    if signal:
        return True
    return False


def signal_is_asterisk(signal: str) -> bool:
    """Returns true if signal is asterisk"""
    if signal == "*":
        return True
    return False


def signal_is_square(signal: str) -> bool:
    """Returns true if signal is square"""
    if signal == "#":
        return True
    return False


def signal_is_override(signal: str) -> bool:
    """ Returns true if signal is the override_signal """
    if signal == constants.OVERRIDE_SIGNAL_PASSWORD_ACCEPTED:
        return True
    return False
