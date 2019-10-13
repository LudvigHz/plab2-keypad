"""File contains the KPC agent"""
from functools import reduce

from keypad import constants
from keypad.finite_state_machine.rule import signal_is_digit
from keypad.keypad import Keypad
from keypad.led_board import LEDBoard


class KPCAgent:
    """The agent communicating with the finite state machine, keypad and led board"""

    def __init__(self):
        self._password_file = "pwd.txt"

        self.led_board = LEDBoard()
        self.led_board.setup()
        self.keypad = Keypad()
        self.override_signal = ""
        self._current_password = []
        self._password = self._get_password_from_file()
        self._temp_password = []

        self._led_id = None
        self._led_dur = None

    def init_passcode_entry(self, *args):
        """ Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED
        Board"""
        self._current_password = []
        self.led_board.start_up_sequence()
        self.override_signal = ""

    def get_next_signal(self) -> str:
        """ Return the override-signal, if it is non-blank; otherwise query the keypad for the next
        pressed key"""
        symbol = self.keypad.get_next_signal()
        if self.override_signal != "":
            return self.override_signal
        return symbol

    def append_password(self, char: str):
        """ Append a char to the current password """
        self._current_password.append(char)

    def verify_login(self, *args):
        """Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override-signal and light the leds appropriately"""
        current_password_as_string = convert_list_to_string(self._current_password)
        if current_password_as_string == self._password:
            self.override_signal = constants.OVERRIDE_SIGNAL_PASSWORD_ACCEPTED
            self._twinkle_leds()
        else:
            self.override_signal = constants.OVERRIDE_SIGNAL_PASSWORD_DECLINED

    def compare_new_passwords(self, *args):
        """ Check that the new passwords match """
        if self._current_password == self._temp_password:
            self.update_passcode_file()
            # TODO add signal to show user if passwords were equal

    def cache_first_password(self, *args):
        """ Cache first password in order to compare passwords later """
        self._temp_password = self._current_password
        self._current_password = []

    def _validate_passcode_change(self, *args):
        """Check that the new passcode is legal, if so update passcode_file, light leds
        appropriately"""

        if len(self._current_password) < 4:
            return
        for char in self._current_password:
            if not signal_is_digit(char):
                return
        self.update_passcode_file()

    def fully_activate_agent(self, *args):
        """ Complete login and activate all functionality """
        # TODO add functionality to this method if it is supposed to do something

    def reset_agent(self, *args):
        """ Resets agent to initial state """
        self.override_signal = ""
        self._current_password = []

    def update_passcode_file(self, *args):
        """ Update passcode file with the new passcode """
        self._write_password_to_file(convert_list_to_string(self._current_password))

    def _get_password_from_file(self, *args):
        """Gets the password from the password file"""
        with open(self._password_file) as file:
            pwd = file.readline()
        return pwd

    def _write_password_to_file(self, pwd):
        """Write password to file"""
        with open(self._password_file) as file:
            file.seek(0)
            file.write(pwd)
            file.truncate()

    def _light_one_led(self):
        """Light led according to led_id and led_duration"""
        self.led_board.light_led(self._led_id, self._led_dur)

    def _flash_leds(self, seconds=3):
        """Flash all leds"""
        self.led_board.flash_all_leds(seconds)

    def _twinkle_leds(self, seconds=3):
        """Twinkle all leds"""
        self.led_board.twinkle_all_leds(seconds)

    def exit_action(self):
        """Play the "power down" lighting sequence"""
        self.led_board.shut_down_sequence()


def convert_list_to_string(list_of_strings):
    """ Convert a list of strings to a complete string """
    return reduce(lambda a, b: a + b, list_of_strings)
