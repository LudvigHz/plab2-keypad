"""File contains the KPC agent"""
from keypad.keypad import Keypad
from keypad.led_board import LEDBoard


class KPCAgent:
    """The agent communicating with the finite state machine, keypad and led board"""

    def __init__(self):
        self.led_board = LEDBoard()
        self.led_board.setup()
        self.keypad = Keypad()
        self._current_sequence = []
        self.is_authenticated = False

        self._led_id = None
        self._led_dur = None

    def init_passcode_entry(self):
        """ Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED
        Board"""
        self._current_sequence = []
        self.led_board.start_up_sequence()

    def get_next_signal(self) -> str:
        """ Return the override-signal, if it is non-blank; otherwise query the keypad for the next
        pressed key"""
        symbol = self.keypad.get_next_signal()
        self._current_sequence.append(symbol)
        if not self.is_authenticated:
            self._verify_login()
        if self.is_authenticated:
            return "Y"  # TODO add constant for override
        return symbol

    def _verify_login(self):
        """Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override-signal and light the leds appropriately"""

    def _validate_passcode_change(self):
        """Check that the new passcode is legal, if so update passcode_file, light leds
        appropriately"""

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
