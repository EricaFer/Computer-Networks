import socket

#Exemplo end-to-end de um cliente TCP
def TCPclient(host,port):
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client.connect((host,port))

    encoded_msg = f'Hello, world! From {host}:{port}'.encode('utf-8')

    status = tcp_client.send(encoded_msg)
    if status > 0:
        data = tcp_client.recv(1024)
        
    print('Saida: Sucesso')

    tcp_client.close()