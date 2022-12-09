import os,sys,random,time,datetime, pytz
import RPi.GPIO as GPIO

def updateTime(): 
    hour = datetime.datetime.now(pytz.timezone('US/Eastern')).hour
    min = datetime.datetime.now(pytz.timezone('US/Eastern')).minute

def getDate():
    wDay = dt.weekday()      

def mon():
    GPIO.output(Relay[0], GPIO.LOW)
    time.sleep(5)
    GPIO.output(Relay[0], GPIO.HIGH)
    time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
                    
def tue():
    GPIO.output(Relay[1], GPIO.LOW)
    time.sleep(5)
    GPIO.output(Relay[1], GPIO.HIGH)
    time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)

    
def wed():
    GPIO.output(Relay[2], GPIO.LOW)
    time.sleep(5)
    GPIO.output(Relay[2], GPIO.HIGH)
    time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)

    
def thur():
    GPIO.output(Relay[3], GPIO.LOW)
    time.sleep(5)
    GPIO.output(Relay[3], GPIO.HIGH)
    time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)

    
def fri():
    GPIO.output(Relay[4], GPIO.LOW)
    time.sleep(5)
    GPIO.output(Relay[4], GPIO.HIGH)
    time.sleep(6)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[7], GPIO.LOW)
    time.sleep(3)
    GPIO.output(Relay[6], GPIO.LOW)
    time.sleep(1.5)
    GPIO.output(Relay[6], GPIO.HIGH)
    time.sleep(120)
    GPIO.output(Relay[7], GPIO.HIGH)
    time.sleep(5)
    GPIO.output(Relay[5], GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay[5], GPIO.HIGH)

    
    
if __name__ == "__main__":
    Relay = [5, 6, 13, 16, 19, 20, 21, 26]

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in range(0,8):
        GPIO.setup(Relay[i], GPIO.OUT)
        
    a = True
    while a == True:
        getDate()
        updateTime()        
        if wDay == 0 and hour == 6 and min == 5:
            mon()
            time.sleep(82800)
        elif wDay == 1 and hour == 6 and min == 5:
            tue()
            time.sleep(82800)
        elif wDay == 2 and hour == 6 and min == 5:
            wed()
            time.sleep(82800)
        elif wDay == 3 and hour == 6 and min == 5:
            thur()
            time.sleep(82800)
        elif wDay == 4 and hour == 6 and min == 5:            
            fri()
            time.sleep(82800) 
