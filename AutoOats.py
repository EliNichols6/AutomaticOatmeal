#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os,sys,random,time
import RPi.GPIO as GPIO
from datetime import datetime, timedelta
from pytz import timezone
import Temperature
import Fan

def grabTimes():
    global mHour 
    global mMin
    global tHour
    global tMin
    global wHour
    global wMin
    global thHour
    global thMin
    global fHour
    global fMin
    url = "http://192.168.100.150:81/schedule_data"
    response = requests.get(url)
    data_dict = json.loads(response.text)
    #del data_dict["schedule_dictionary"]
    #print(response.text)
    #print(type(data_dict))
    #print(data_dict["schedule_dictionary"])
    mHour = data_dict["schedule_dictionary"]["Monday"]["hour"]
    mMin = data_dict["schedule_dictionary"]["Monday"]["minute"]
    tHour = data_dict["schedule_dictionary"]["Tuesday"]["hour"]
    tMin = data_dict["schedule_dictionary"]["Tuesday"]["minute"]
    wHour = data_dict["schedule_dictionary"]["Wednesday"]["hour"]
    wMin = data_dict["schedule_dictionary"]["Wednesday"]["minute"]
    thHour = data_dict["schedule_dictionary"]["Thursday"]["hour"]
    thMin = data_dict["schedule_dictionary"]["Thursday"]["minute"]
    fHour = data_dict["schedule_dictionary"]["Friday"]["hour"]
    fMin = data_dict["schedule_dictionary"]["Friday"]["minute"]

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
    
def endDay1():
    eastern = pytz.timezone('US/Eastern')
    today = datetime.datetime.now(eastern)
    end_of_day = today.replace(hour=23, minute=59, second=0, microsecond=0)
    delta = (end_of_day - today).total_seconds()
    print(today, end_of_day, delta)
    time.sleep(delta)

# Check Date and Time for EST
def updateTime():
    global hour
    global minute
    tz = timezone('EST')
    datetime.now(tz) 
    hour = datetime.now(tz).hour
    minute = datetime.now(tz).minute
    dt = datetime.now()
    wDay = dt.weekday()

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
        updateTime()
        grabTimes()
        # Checks Day, Time, and Minute to execute daily function
        if wDay == 0:
            if hour == mHour and minute == mMin:
                #mon()
                execute(wDay)
                endDay1()
            else:
                time.sleep(30)
                updateTime()
                grabTimes()
        elif wDay == 1:
            if hour == tHour and minute == tMin:
                #tue()
                execute(wDay)
                endDay1()
            else:
                time.sleep(30)
                updateTime()
                grabTimes()
        elif wDay == 2:
            if hour == wHour and minute == wMin:
                #wed()
                execute(wDay)
                endDay1()
            else:
                time.sleep(30)
                updateTime()
                grabTimes()
        elif wDay == 3:
            if hour == thHour and minute == thMin:
                #thur()
                execute(wDay)
                endDay1()
            else:
                time.sleep(30)
                updateTime()
                grabTimes()
        elif wDay == 4:
            if hour == fHour and minute == fMin:
                #fri()
                execute(wDay)
                endDay1()
            else:
                time.sleep(30)
                updateTime()
                grabTimes()