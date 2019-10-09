class KPCAgent:
    """The agent communicating with the finite state machine, keypad and led board"""

    def init_passcode_entry(self):
        """ Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED
        Board"""

    def get_next_signal(self) -> str:
        """ Return the override-signal, if it is non-blank; otherwise query the keypad for the next
        pressed key"""

    def _verify_login(self):
        """Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override-signal and light the leds appropriately"""

    def _validate_passcode_change(self):
        """Check that the new passcode is legal, if so update passcode_file, light leds
        appropriately"""

    def _light_one_led(self):
        """Light led according to led_id and led_duration"""

    def _flash_leds(self):
        """Flash all leds"""

    def _twinkle_leds(self):
        """Twinkle all leds"""

    def exit_action(self):
        """Play the "power down" lighting sequence"""
