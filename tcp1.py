from multiprocessing import Process
 
import socket
 
def handle_client(client_socket):
    """客户请求处理"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print('request data:', request_data)
 
    # 构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Sever: My server\r\n'
    response_body = 'hello word!'
    response_data = response_start_line + response_headers + '\r\n' +response_body
    print('response data:', response_data)
 
    # 发送响应数据
    client_socket.send(bytes(response_data,'utf-8'))
    # client_socket.close()

    test(client_socket)

def test(client_socket):
    client_socket.send(bytes("01 03 00 00 00 02 c4 0b",'utf-8'))
    request_data = client_socket.recv(1024)
    print('request data:', request_data)
    client_socket.close()

def main():
    """主函数"""
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(('',8001))
    server_socket.listen(10)
 
    while True:
        # 客户请求接收开启进程
        client_socket,client_address = server_socket.accept()
        print("[%s,%s]用户连接上了" % client_address)
 
        handle_client_process = Process(target=test,args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
 
if __name__ == '__main__':
    main()

