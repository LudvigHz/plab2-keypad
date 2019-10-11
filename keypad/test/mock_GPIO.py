"""Mock mudule for GPIO. Used for tests"""

BCM = "BCM"
IN = "IN"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"
PUD_DOWN = "PUD_DOWN"

HIGH_PINS = []


def setmode(mode):
    """Mock GPIO.setmode"""
    if mode == BCM:
        return True
    raise ValueError("Invalid mode")


def setup(pin, value, *args, **kwargs):
    """Mock GPIO.setup"""
    if value not in [IN, OUT]:
        raise ValueError("Invalid setting. Must be GPIO.IN or GPIO.OUT")
    return True


def output(pin, value):
    """Mock GPIO.output"""
    if not isinstance(pin, int):
        raise ValueError("Invalid value. Must be an integer")
    if value not in [LOW, HIGH]:
        raise ValueError("Invalid value. Must be GPIO.LOW or GPIO.HIGH")
    return True


def input(pin):
    """Mock GPIO.input"""
    if not isinstance(pin, int):
        raise ValueError("Invalid value. Must be an integer")
    if pin in HIGH_PINS:
        return HIGH
    return LOW


def set_pin_high(pin):
    """ Set pin as high """
    HIGH_PINS.append(pin)


def set_pin_low(pin):
    """ Set pin as high """
    if pin in HIGH_PINS:
        HIGH_PINS.remove(pin)
