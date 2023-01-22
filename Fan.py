#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import time
from gpiozero import CPUTemperature

#cpu = CPUTemperature()
#print(cpu.temperature)
def Fan_Function():
    fan_off = 'sudo uhubctl -l 1-1 -p 2 -a off'
    fan_on = 'sudo uhubctl -l 1-1 -p 2 -a on'
    os.system(fan_off)
    while True:
        cpu = CPUTemperature()
        print(cpu.temperature)
        time.sleep(3)
        if cpu.temperature > 60:
            os.system(fan_on)
            print(cpu.temperature)
        if cpu.temperature < 40:
            os.system(fan_off)
            print(cpu.temperature)
    
if __name__ == "__main__":
        Fan_Function()