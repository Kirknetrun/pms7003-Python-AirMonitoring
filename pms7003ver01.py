import matplotlib.pyplot as plt
from pms7003 import Pms7003Sensor, PmsSensorException
import time, datetime 
from datetime import datetime
import sys

################# Air data lists
pm2d5_data = []
#################
pm10_data = []
#################
pm1_data = []


#colors text red using ANSI code
def print_red(text):
    print("\033[91m {}\033[00m" .format(text))


#colors text blue using ANSI code
def print_blue(text):
    print("\033[94m {}\033[00m" .format(text))


#gives the intensity of pm2.5 dust and informs the exceedance of norms
def pm2d5_writer():
    natezenie_pm25 = data_sensor['pm2_5']
    pm2d5_data.append(natezenie_pm25)
    if natezenie_pm25 <= 25:
        print("Dust intesity PM2.5: {} µg/m3 --- Intensity acceptable".format(natezenie_pm25))
    else:
        print_red("Dust intesity PM2.5: {} µg/m3 --- Intensity unacceptable".format(natezenie_pm25))


#gives the intensity of pm10 dust and informs the exceedance of norms
def pm10_writer():
    natezenie_pm10 = data_sensor['pm10']
    pm10_data.append(natezenie_pm10)
    if natezenie_pm10 <= 50:
        print("Dust intesity PM10: {} µg/m3 --- Intensity acceptable".format(natezenie_pm10))
    elif natezenie_pm10 <= 200:
        print_red("Dust intesity PM10: {} µg/m3 --- Intensity unacceptable".format(natezenie_pm10))
    elif natezenie_pm10 <= 300:
        print_red("Dust intesity PM10: {} µg/m3 --- Fatal Intensity".format(natezenie_pm10))

        

#gives the intensity of pm1.0 dust and informs the exceedance of norms
def pm1_writer():
    natezenie_pm1 = data_sensor['pm1_0']
    pm1_data.append(natezenie_pm1)
    if natezenie_pm1 <= 50:
        print("Dust intesity PM1.0: {} µg/m3 --- Intensity acceptable".format(natezenie_pm1))
    else:
        print_red("Dust intesity PM1.0: {} µg/m3 --- Intensity unacceptable".format(natezenie_pm1))



counter = 0

while True:
    sensor = Pms7003Sensor('/dev/ttyUSB0') #read the USB port
    data_sensor = sensor.read()
    now = datetime.now() #read the system time
    date_time = now.strftime("%Y-%m-%d %H:%M:%S") #format the time which was read
    
    try:
        print_blue("__________________________________________________________________________")
        
        print_blue(date_time)
        pm2d5_writer()
        pm10_writer()
        pm1_writer()
        
        
        counter += 1
        
        if counter % (5*60/3) == 0: #do the action about every 5 minutes
            plt.plot(pm2d5_data, label = 'pm2_5') #crates the chart 
            plt.plot(pm10_data, label = 'pm10')
            plt.plot(pm1_data, label = 'pm1_0')
            
            plt.ylabel('dust intesity in µg/m3')
            plt.ylim(0, 100)
            
            plt.xlabel('time')
            
            plt.legend()
            plt.show()
            pm2d5_data = []
            pm10_data = []
            pm1_data = []
            
            
        with open('dane_jakosci.txt', 'a') as p: #creates the file and write there air data
            original = sys.stdout
            sys.stdout = p
            
            print("pm2.5: {} µg/m3 | {}".format(data_sensor['pm2_5'], date_time))
            print("pm10: {} µg/m3 | {}".format(data_sensor['pm10'], date_time))
            print("pm1_0: {} µg/m3 | {}".format(data_sensor['pm1_0'], date_time))
            
            sys.stdout = original
        
    
        time.sleep(3) #time interval
    
    except PmsSensorException:
        print('Connection problem!!!')

# In[ ]:




