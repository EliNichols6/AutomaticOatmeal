import os,sys,random,time,datetime
import RPi.GPIO as GPIO

Relay = [5, 6, 13, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for i in range(0,8):
    GPIO.setup(Relay[i], GPIO.OUT)

# Monday = 0, Sunday = 6
def getDate():
    wDay = dt.weekday()
def getTime():
    dTime = datetime.now()

dt = datetime.now()
  

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

    a = True
    while a == True:
        getDate()
        
        if wDay == 0:
            mon()
        elif wDay == 1:
            tue()
        elif wDay == 2:
            wed()
        elif wDay == 3:
            thur()
        elif wDay == 4:            
            fri()      

   

