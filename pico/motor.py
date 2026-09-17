from servo import Servo
from time import sleep_ms

#bell = Servo(pin_id=20)

class Ringer(Servo):
    def __init__(self, pin_id = 19):
        super().__init__(pin_id)
        self.calibration(1.0, 2.0, 1.5, 0, 180)

    def ring(self, count=1, strike_angle=170, rest_angle=0, delay_ms=500):
        """Ring the bell count times by striking and returning to rest position, then detaching."""
        assert delay_ms >= 0, "Delay must not be negative"
        assert count >= 1, "Count must be at least 1"

        for _ in range(count):
            self.angle(strike_angle)
            sleep_ms(delay_ms)
            self.angle(rest_angle)
            sleep_ms(delay_ms)
        self.detach()

