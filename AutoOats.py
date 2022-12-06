import os,sys,random,time,datetime

# Monday = 0, Sunday = 6
def getDate():
    wDay = dt.weekday()
def getTime():
    dTime = datetime.now()

dt = datetime.now()

# Function that powers on the water
def wtr_powerOn():
    # Open Relay 6, delay 2 sec, close Relay 6
    print("Powering on")
    

def water_d0():
    # Open Relay 7, delay 2 sec, close Relay 7
    print("Water D0")

def oat_drop(day):
    # Add 1 to day so you get it correlated to D1, D2, D3, etc.
    day += 1
    
    for x in range(1,5):
        if x == day:            
            # Open Relay for that day
        
    
        
   
    print("Dropping oats")
  
# Function for monday - Executes wtr_powerOn, water_d0, and oat_drop on monday
def mon():
    oat_drop(wDay)
    time.sleep(6)
    wtr_powerOn()
    time.sleep(5)
    water_d0()
    time.sleep(120)
    wtr_powerOn()
    print("Executed")
    #sleeps for one day 
    time.sleep(86400)

    
def tue():
    oat_drop(wDay)
    time.sleep(6)
    wtr_powerOn()
    time.sleep(5)
    water_d0()
    time.sleep(120)
    wtr_powerOn()
    print("Executed")
    #sleeps for one day 
    time.sleep(86400)

    
def wed():
    oat_drop(wDay)
    time.sleep(6)
    wtr_powerOn()
    time.sleep(5)
    water_d0()
    time.sleep(120)
    wtr_powerOn()
    print("Executed")
    #sleeps for one day 
    time.sleep(86400)

    
def thur():
    oat_drop(wDay)
    time.sleep(6)
    wtr_powerOn()
    time.sleep(5)
    water_d0()
    time.sleep(120)
    wtr_powerOn()
    print("Executed")
    #sleeps for one day 
    time.sleep(86400)

    
def fri():
    oat_drop(wDay)
    time.sleep(6)
    wtr_powerOn()
    time.sleep(5)
    water_d0()
    time.sleep(120)
    wtr_powerOn()
    print("Executed")
    #sleeps for three days
    time.sleep(259200)

    
    
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

   
    

    #wtr_powerOn()
    #water_d0()
    #oat_drop(wDay)
    # Wait 24 hours then repeat above
    
