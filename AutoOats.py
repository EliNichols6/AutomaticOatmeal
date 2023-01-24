#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os,sys,random,time
import RPi.GPIO as GPIO
from datetime import datetime
from pytz import timezone
import Temperature
import Fan


def getpid():
    return os.getpid() 
def execute(weekday):
    GPIO.output(Relay[weekday], GPIO.LOW)
    #GPIO.output(Relay[1], GPIO.LOW)
    Temperature.read_temp(decimals = 1, sleeptime = 5)
    #time.sleep(5)
    GPIO.output(Relay[weekday], GPIO.HIGH)
    #GPIO.output(Relay[1], GPIO.HIGH)
    Temperature.read_temp(decimals = 1, sleeptime = 4)
    #time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    Temperature.read_temp(decimals = 1, sleeptime = 2)
    #time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    Temperature.read_temp(decimals = 1, sleeptime = 5)
    #time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    Temperature.read_temp(decimals = 1, sleeptime = 3)
    #time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    Temperature.read_temp(decimals = 1, sleeptime = 1.5)
    #time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    Temperature.read_temp(decimals = 1, sleeptime = 120)
    #time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    Temperature.read_temp(decimals = 1, sleeptime = 5)
    #time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    Temperature.read_temp(decimals = 1, sleeptime = 2)
    #time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)  
    

if __name__ == "__main__":
    #global pid
    #pid = os.getpid()
    #value = temp.read_temp()
    #print(value)
    # Establishes Relays 1-8 (1 is 5, 2 is 6, 3 is 13, etc.)
    Relay = [5, 6, 13, 16, 19, 20, 21, 26]
    # Set up Relays, Iterate through each relay to set them up and set output to high
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in range(0,8):
        GPIO.setup(Relay[i], GPIO.OUT)
        GPIO.output(Relay[i], GPIO.HIGH)
        
    a = True
    while a == True:
        # Check Date and Time for EST
        tz = timezone('EST')
        datetime.now(tz) 
        hour = datetime.now(tz).hour
        minute = datetime.now(tz).minute
        dt = datetime.now()
        wDay = dt.weekday()
        # Checks Day, Time, and Minute to execute daily function
        if wDay == 0 and hour == 22 and minute == 45:
            #mon()
            execute(wDay)
            time.sleep(86160)
        elif wDay == 1 and hour == 6 and minute == 5:
            #tue()
            execute(wDay)
            time.sleep(86160)
        elif wDay == 2 and hour == 5 and minute == 40:
            #wed()
            execute(wDay)
            time.sleep(86160)
        elif wDay == 3 and hour == 6 and minute == 5:
            #thur()
            execute(wDay)
            time.sleep(86160)
        elif wDay == 4 and hour == 6 and minute == 5:            
            #fri()
            execute(wDay)
            time.sleep(258960) 
