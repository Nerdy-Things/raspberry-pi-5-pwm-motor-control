import time

from pwm_control import PwmControl
from pwm_control import Channel

channels: list[Channel] = [
    Channel.GPIO_12, 
    Channel.GPIO_13,
    Channel.GPIO_18,
    Channel.GPIO_19,
]

pwm_control = PwmControl()

print("Set control")
for channel in channels: 
    pwm_control.init(channel=channel)

print("Set 100%")
pwm_control.set(Channel.GPIO_12, 50)
pwm_control.set(Channel.GPIO_13, 0)
# pwm_control.set(Channel.GPIO_18, 100)
# pwm_control.set(Channel.GPIO_19, 100)
time.sleep(3)

print("Set 0%")
pwm_control.set(Channel.GPIO_12, 0)
pwm_control.set(Channel.GPIO_13, 0)
# pwm_control.set(Channel.GPIO_18, 0)
# pwm_control.set(Channel.GPIO_19, 0)