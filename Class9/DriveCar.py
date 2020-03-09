#!/usr/bin/env python

from rpiHAT import ServoNT

class driveCar:
    def __init__(self, freq=94.5, motor_c=1, steer_c=2):
        self.freq = freq
        self.motor = ServoNT(motor_c, self.freq)
        self.steer = ServoNT(steer_c, self.freq)

    def setSteering(self, val=0.15):
        self.steer.pulse(val)

    def setSpeed(self, val=0.15):
        self.motor.pulse(val)