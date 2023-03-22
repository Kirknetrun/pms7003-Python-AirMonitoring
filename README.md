# pms7003-Python-AirMonitoring
Monitoring air quality with a sensor microcomputer using pms7003 with RaspberryPi and python script

This is my last year project where I used a Raspberry Pi microcomputer with an air quality sensor, PMS7003. The sensor is being operated with a script written in Python. I used a Raspberry Pi 3B+ with the PMS7003 Plant Tower attached with an IDC PMS7003 adapter using a microUSB cable.

In this project, I wanted to monitor air quality, alarm the user if the dust intensity is above the norms, collect the data in a text file, and create a chart from the detected data (using Matplotlib.pyplot). The chart-creating data part is not polished and finished yet!

In Addition i wrote a simple shell scrip which boot the Python script in .sh file named 'run_pms7003.sh' and added permissions in console by typing:

    chmod +x run_pms7003ver01.sh


Every function and crucial part is commented in code.
