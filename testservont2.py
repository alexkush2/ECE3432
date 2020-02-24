# test no threading
from rpiHAT import ServoNT
import time
import sys

s=ServoNT(channel=1, freq=94.5)
t=ServoNT(channel=2, freq=94.5)
s.pulse(float(sys.argv[2]))
t.pulse(float(sys.argv[1]))

try:
    while True:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    s.pulse(0.15)
    t.pulse(0.15)
