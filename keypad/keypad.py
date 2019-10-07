from EmulatorGUI import GPIO


class Keypad:
    ROW_PINS = [18, 23, 24, 25]
    COLUMN_PINS = [17, 22, 27]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)


