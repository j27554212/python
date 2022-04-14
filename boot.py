relay gpio5  
relay gpio12  
relay gpio13  
relay gpio15
ON-1 OFF-0
------------           
# Complete project details at https://RandomNerdTutorials.com  

try:
  import usocket as socket  //設定為socket  
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'    //ASUSLAB  
password = 'REPLACE_WITH_YOUR_PASSWORD' //ASUSASUS  

station = network.WLAN(network.STA_IF) //設定網卡  

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)  //控制LED GPIO2為控制腳位    GPIO2=D4  
