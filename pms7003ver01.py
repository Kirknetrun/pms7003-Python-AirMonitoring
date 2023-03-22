#!/usr/bin/env python
# coding: utf-8

# In[25]:


import matplotlib.pyplot as plt
from pms7003 import Pms7003Sensor, PmsSensorException
import time, datetime 
from datetime import datetime
import sys


# In[35]:


#################listy z danymi powietrza
pm2d5_data = []
#################
pm10_data = []
#################
pm1_data = []


# In[40]:


#koloruje tekst na czerwono za pomoca kodu ANSI
def print_red(text):
    print("\033[91m {}\033[00m" .format(text))


# In[45]:


#koloruje tekst na niebiesko za pomoca kodu ANSI
def print_blue(text):
    print("\033[94m {}\033[00m" .format(text))


# In[41]:


#podaje natezenie pylu pm2.5 i informuje przekroczenie norm
def pm2d5_writer():
    natezenie_pm25 = data_sensor['pm2_5']
    pm2d5_data.append(natezenie_pm25)
    if natezenie_pm25 <= 25:
        print("Natezenie pylu PM2.5: {} µg/m3 --- Natezenie w dopuszczalnej normie".format(natezenie_pm25))
    else:
        print_red("Natezenie pylu PM2.5: {} µg/m3 --- Natezenie ponad dopuszczalna norme!!!".format(natezenie_pm25))

# In[42]:


#podaje natezenie pylu pm10 i informuje przekroczenie norm
def pm10_writer():
    natezenie_pm10 = data_sensor['pm10']
    pm10_data.append(natezenie_pm10)
    if natezenie_pm10 <= 50:
        print("Natezenie pylu PM10: {} µg/m3 --- Natezenie w dopuszczalnej normie".format(natezenie_pm10))
    elif natezenie_pm10 <= 200:
        print_red("Natezenie pylu PM10: {} µg/m3 --- Natezenie ponad dopuszczalna norme".format(natezenie_pm10))
    elif natezenie_pm10 <= 300:
        print_red("Natezenie pylu PM10: {} µg/m3 --- Natezenie w stanie krytycznym".format(natezenie_pm10))


# In[43]:


#podaje natezenie pylu pm1 i informuje przekroczenie norm
def pm1_writer():
    natezenie_pm1 = data_sensor['pm1_0']
    pm1_data.append(natezenie_pm1)
    if natezenie_pm1 <= 50:
        print("Natezenie pylu PM1.0: {} µg/m3 --- Natezenie w dopuszczalnej normie".format(natezenie_pm1))
    else:
        print_red("Natezenie pylu PM1.0: {} µg/m3 --- Natezenie ponad dopuszczalna norme!!!".format(natezenie_pm1))


# In[54]:

#Glowna czesc programu
counter = 0

while True:
    sensor = Pms7003Sensor('/dev/ttyUSB0') #czyta port
    data_sensor = sensor.read()
    now = datetime.now() #czyta czas z systemu
    date_time = now.strftime("%Y-%m-%d %H:%M:%S") #nadaje format czytanemu czasowi
    
    try:
        print_blue("__________________________________________________________________________")
        
        print_blue(date_time)
        pm2d5_writer()
        pm10_writer()
        pm1_writer()
        
        
        counter += 1
        
        if counter % (5*60/3) == 0: #warunek ktory tworzy wykres co okolo 5 minut
            plt.plot(pm2d5_data, label = 'pm2_5') #tworzy wykres zlisty z danymi
            plt.plot(pm10_data, label = 'pm10')
            plt.plot(pm1_data, label = 'pm1_0')
            
            plt.ylabel('Natezenie pylkow w µg/m3')
            plt.ylim(0, 100)
            
            plt.xlabel('Czas')
            
            plt.legend()
            plt.show()
            pm2d5_data = []
            pm10_data = []
            pm1_data = []
            
            
        with open('dane_jakosci.txt', 'a') as p: #tworzy plik i zapisuje tam dane powietrza
            original = sys.stdout
            sys.stdout = p
            
            print("pm2.5: {} µg/m3 | {}".format(data_sensor['pm2_5'], date_time))
            print("pm10: {} µg/m3 | {}".format(data_sensor['pm10'], date_time))
            print("pm1_0: {} µg/m3 | {}".format(data_sensor['pm1_0'], date_time))
            
            sys.stdout = original
        
    
        time.sleep(3) #interwal czasowy pomiaru
    
    except PmsSensorException:
        print('Problem z lacznoscia czujnika!!!')

# In[ ]:




