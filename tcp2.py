# from flask import Flask, render_template, request
# import random, socket, threading

# #tcp server
# TCP_IP = '127.0.0.1'
# TCP_PORT = 8001
# BUFFER_SIZE  = 20

# def launchServer():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind((TCP_IP, TCP_PORT))
#     s.listen(1)

#     print('waiting for connection')
#     conn, addr = s.accept()

#     print ('Connection address:', addr)


# #flask app
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':    
#         if request.form['submit'] == 'button1':
#             conn.send(b'button1') 
#             return "Random number between 1 and 10:  " + str(random.randint(1,10))
#         elif request.form['submit'] == 'button2':
#             conn.send(b'button1')
#             return "Random number between 11 and 1000:  " + str(random.randint(11,1000))
#         else:
#             pass

#     if request.method == 'GET':
#         return '''
#         <title>What would you like to do?</title>
#         <form action="" method="post">
#         <br><br>
#         <input type="submit" name="submit" value="button1">
#         <br><br>
#         <input type="submit" name="submit" value="button2">
#         </form>
#         '''

# if __name__ == "__main__":
#     app.run(debug=True)
#     t = threading.Thread(target=launchServer)
#     t.daemon = True
#     t.start()




from socketserver import BaseRequestHandler, TCPServer

#继承BaseRequestHandler这个base class，并重定义handle()
class EchoHandler(BaseRequestHandler): 
    def handle(self): 
        print('Got connection from', self.client_address) 
       
        #self.request is the TCP socket connected to the client
        while True: 
            #8192代表每次读取8192字节
            msg = self.request.recv(1024) 
            if not msg: 
                break 
            self.request.send(msg)

if __name__ == '__main__': 
    #第一对参数是（host, port）
    serv = TCPServer(('', 8001), EchoHandler)       
    serv.serve_forever()