# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:16:46 2021

@author: srcdo
"""

#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

 # Pins for Motor Driver Inputs 
Motor1A = 20
Motor1B = 21
Motor2A = 26
Motor2B = 19

import serial
uart_channel = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
data1=" "
data=" "
 
			# GPIO Numbering
GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor2B,GPIO.OUT)
	
def forwards():
	# Going forwards
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	time.sleep(5)
def backwards():
 	# Going backwards
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	time.sleep(5)
def Stop():	
	# Stop
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
def right():
	# Going right
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	time.sleep(5)
def left():
	# Going left
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	time.sleep(5)

def destroy():	
	GPIO.cleanup()



 
if __name__ == '__main__':
    try:
        while True:
            data = uart_channel.read(1)
            data = data.decode('utf-8')
            data1+=str(data)
            print (data1)
            if (data1 == ' 1'):
                        GPIO.output(Motor1A,GPIO.LOW)
                        GPIO.output(Motor1B,GPIO.HIGH)
                        GPIO.output(Motor2A,GPIO.HIGH)
                        GPIO.output(Motor2B,GPIO.LOW)
            if (data1 == ' 2'):
                        GPIO.output(Motor1A,GPIO.HIGH)
                        GPIO.output(Motor1B,GPIO.LOW)
                        GPIO.output(Motor2A,GPIO.LOW)
                        GPIO.output(Motor2B,GPIO.HIGH)
            if (data1 == ' 3'):
                        GPIO.output(Motor1A,GPIO.LOW)
                        GPIO.output(Motor1B,GPIO.HIGH)
                        GPIO.output(Motor2A,GPIO.LOW)
                        GPIO.output(Motor2B,GPIO.LOW)
            if (data1 == ' 4'):
                        GPIO.output(Motor1A,GPIO.LOW)
                        GPIO.output(Motor1B,GPIO.LOW)
                        GPIO.output(Motor2A,GPIO.HIGH)
                        GPIO.output(Motor2B,GPIO.LOW)
            if (data1 == ' 5'):
                        GPIO.output(Motor1A,GPIO.LOW)
                        GPIO.output(Motor1B,GPIO.LOW)
                        GPIO.output(Motor2A,GPIO.LOW)
                        GPIO.output(Motor2B,GPIO.LOW)
            uart_channel.flush()
            data=" "
            data1=" "

           
                    
            
        
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
