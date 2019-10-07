from RPiSim.GPIO import GPIO


class Keypad:
    ROW_PINS = [18, 23, 24, 25]
    COLUMN_PINS = [17, 22, 27]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for rp in Keypad.ROW_PINS:
            GPIO.setup(rp, GPIO.OUT)
        for cp in Keypad.COLUMN_PINS:
            GPIO.setup(cp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
