import os,sys,random,time,datetime

# Monday = 0, Sunday = 6
def getDate():
    wDay = dt.weekday()


# Function that powers on the water
def wtr_powerOn():
    print("Powering on")


def water_d0():
    print("Water D0")

def oat_drop():
    print("Dropping oats")
  
# Function for monday - Executes wtr_powerOn, water_d0, and oat_drop on monday
def mon():
    print("Executed")
    
def tue():
    print("Executed")
    
def wed():
    print("Executed")
    
def thur():
    print("Executed")
    
def fri():
    print("Executed")
    
    
if __name__ == "__main__":
#sleeps for one day
    time.sleep(86400)

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
    

    wtr_powerOn()
    water_d0()
    oat_drop()
    # Wait 24 hours then repeat above
    
