# pms7003-Python-AirMonitoring
Monitoring air quality with a sensor microcomputer using pms7003 with RaspberryPi and python script

This is my last year project where I used a Raspberry Pi microcomputer with an air quality sensor, PMS7003. The sensor is being operated with a script written in Python. I used a Raspberry Pi 3B+ with the PMS7003 Plant Tower attached with an IDC PMS7003 adapter using a microUSB cable.

In this project, I wanted to monitor air quality, alarm the user if the dust intensity is above the norms, collect the data in a text file, and create a chart from the detected data (using Matplotlib.pyplot). The chart-creating data part is not polished and finished yet!

Every function and crucial part is commented in code.

When you are using the Pms7003Sensor() object form pms7003 sensor library it is crucial to give corret port name to read the data later in my example it is '/dev/ttyUSB0' because im using the USB port on microcomputer:

    sensor = Pms7003Sensor('/dev/ttyUSB0')

There is possibility to connect via other ports so i thought it would be good to mention

In Addition i wrote a simple shell scrip which boot the Python script in .sh file named 'run_pms7003.sh': 

    #!/bin/bash
    python pms7003ver01.py

and added permissions in console by typing:

    chmod +x run_pms7003ver01.sh


