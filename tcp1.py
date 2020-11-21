import socket
import time
  
HOST = ''
PORT = 8001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((HOST, PORT)) 
sock.listen(5) 
while True: 
    connection,address = sock.accept()
    print ('IP Address：'+ str(address))
    # print(connection.recv(1024))
    try: 
        connection.settimeout(10)
        buf = connection.recv(1024)
        print(buf.decode())
        
    except Exception as e:
        print("Error:", e)
        # print ('time out')
    connection.close()