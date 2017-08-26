import machine
import time

p2=machine.Pin(2)
pwm2=machine.PWM(p2)
pwm2.freq(1)
pwm2.duty(512)
