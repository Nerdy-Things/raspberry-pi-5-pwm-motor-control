import time

from pwm_control import PwmControl
from pwm_control import Channel

class MotorHandler:
    _motor_forward = Channel.GPIO_12
    _motor_backward= Channel.GPIO_13

    _pwm_control = PwmControl()

    def init(self):
        self._pwm_control.init(channel=self._motor_forward)
        self._pwm_control.init(channel=self._motor_backward)

    def set(self, x, y):
        if y > 0: 
            self._pwm_control.set(channel=self._motor_forward, value=y)
            self._pwm_control.set(channel=self._motor_backward, value=0)
        elif y < 0:
            self._pwm_control.set(channel=self._motor_forward, value=0)
            self._pwm_control.set(channel=self._motor_backward, value=abs(y))
        else:
            self._pwm_control.set(channel=self._motor_forward, value=y)
            self._pwm_control.set(channel=self._motor_backward, value=y)

    def stop(self):
        self._pwm_control.set(channel=self._motor_forward, value=0)
        self._pwm_control.set(channel=self._motor_backward, value=0)
