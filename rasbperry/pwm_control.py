from rpi_hardware_pwm import HardwarePWM
from enum import Enum

frequency = 20000

class AlreadyStartedException(Exception):
    pass

class ChannelNotFoundException(Exception):
    pass

class OutOfBoundsException(Exception):
    pass

class Channel(Enum):
    GPIO_12 = 0
    GPIO_13 = 1

class PwmControl:
    _pwms = {}

    def init(self, channel: Channel):
        if channel in self._pwms:
            raise AlreadyStartedException("Already initialized.")
        else:
            print(f"Init {channel}")
            pwm = HardwarePWM(pwm_channel=channel.value, hz=frequency, chip=2)
            pwm.start(0)
            self._pwms[channel] = pwm

    def set(self, channel: Channel, value: int):
        pwm = self._pwms[channel]
        if not pwm:
            raise ChannelNotFoundException("Channel not found. Did you init it first?")
        value = min(value, 100)
        value = max(value, 0)
        print(f"Set {channel} {value}")
        pwm.change_duty_cycle(value)

    def stop(self, channel: Channel):
        pwm = self._pwms[channel]
        if not pwm:
            raise ChannelNotFoundException("Channel not found. Should it be stopped?")
