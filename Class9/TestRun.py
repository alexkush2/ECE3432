#!/usr/bin/env python

import DriveCar
import time

car = DriveCar()
car.setSpeed(0.2)
car.setSteering(0.15)

try:
    while True:
        time.sleep(0.5)
except(KeyboardInterrupt,SystemExit):
    car.setSpeed(0.15)
    car.setSteering(0.15)