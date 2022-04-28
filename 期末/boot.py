relay gpio5  
relay gpio12  (紅)    
relay gpio13  (綠)    
relay gpio15  (藍)    
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

station.active(True)  //查詢網卡是否啟動
station.connect(ssid, password) //(名稱,密碼)

while station.isconnected() == False: //(網卡是否連線)
  pass //(false)為不動作

print('Connection successful') //連線成功
print(station.ifconfig())  //列印得到的ip

led = Pin(2, Pin.OUT)  //控制LED GPIO2為控制腳位    GPIO2=D4  
