"""Mock mudule for GPIO. Used for tests"""

BCM = "BCM"
IN = "IN"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"


def setmode(mode):
    """Mock GPIO.setmode"""
    if mode == BCM:
        return True
    raise ValueError("Invalid mode")


def setup(pin, value):
    """Mock GPIO.setup"""
    if value not in [IN, OUT]:
        raise ValueError("Invalid setting. Must be GPIO.IN or GPIO.OUT")
    return True


def output(pin, value):
    """Mock GPIO.output"""
    if value not in [LOW, HIGH]:
        raise ValueError("Invalid value. Must be GPIO.LOW or GPIO.HIGH")
    return True


def input(pin):
    """Mock GPIO.input"""
    return 1
