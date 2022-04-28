# Complete project details at https://RandomNerdTutorials.com

def web_page():
  if led.value() == 1:  //確定LED腳位為高電位或低電位
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  // 建立socket
s.bind(('', 80)) //與socket結合  //port可改，但須確定沒重複使用port
s.listen(5)//檢查用戶端連線 最多允許5個連線請求

while True:
  conn, addr = s.accept() //接受連線請求 //conn=socket  addr=ip port
  print('Got a connection from %s' % str(addr)) //列印ip port
  request = conn.recv(1024)  //recv = 接收用戶端請求 
  request = str(request) //(request)轉換字串 //初始使用byte資料形式
  print('Content = %s' % request) 
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')  //send 回應給用戶端
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')     //一定要2個/n 結束
  conn.sendall(response)
  conn.close()  //關閉socket
