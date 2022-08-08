import socket
from threading import Thread
import threading

# instanciando um Socket TCP
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#IP do domínio de destino
host = 

# porta numérica do serviço de destino
port = 234

# estabelecendo uma conexão com um serviço TCP externo
tcp_client.connect((host,port))

# encaminhando uma mensagem para o serviço de destino
# status, # de elementos enviados, cada caracter é um, cada 1 vale 12 bytes
status = tcp_client.send(b'Hello, world')

# se o b n funcionar 
msg = 'Hello, world'

# Usar isso ou isso
bin_msg = msg.encode('utf8')
bin_msg = bytearray(msg,'utf8')

# Recebendo os dados e imprimindo
if status >0:
    data = tcp_client.recv(1024)
    print('Received',repr(data))

#Exemplo end-to-end de um cliente TCP
def TCPclient(host,port):
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client.connect((host,port))

    status = tcp_client.send(b'Hello, world')
    if status > 0:
        data = tcp_client.recv(1024)
        #print ('Received',repr(data))

    tcp_client.close()

def TCPserver(host,port):

    # Instanciando um servidor socket (ECO)
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #Vincula o servio a uma porta de servidor local
    tcp_server.bind((host,port))

    # autoriza o servio TCP sendo criado a atender as conexões
    # com a porta e IP vinculados anteriormente 
    tcp_server.listen()

    # para aceitar uma conexão de um cliente TCP externo
    # e começar a tratar uma mensagem encaminhada, faça:
    # addr = address de origem (cliente)
    conn,addr = tcp_server.accept()

    # enquanto estou recebendo dados:
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf8'))
        # Echo service
        conn.sendall(data)
    
    conn.close()

#####################    UDP   ##################################

#Exemplo end-to-end de um cliente TCP
def UDPclient(host,port):
    udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address = (host,port)

    status = udp_client.sendto(b'Hello, world!',server_address)

    if status > 0:
        data = udp_client.recv(1024)
        print ('Received',repr(data))
         
    udp_client.close()

def UDPserver(host,port):
    udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address = (host,port)

    udp_server.bind(server_address)

    # enquanto estou recebendo dados:
    while 1:
        data,address = udp_server.recvfrom(1024)
        if not data:
            break
        print(repr(data))
        # Echo service
        udp_server.sendto(data,address)
         
    udp_server.close()

def TCPConcurrentServer(host,port):
    tcp_cServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = (host,port)
    tcp_cServer.listen()

    def threadedConn(conn):
        while True:
            #data received from client
            data = conn.recv(1024)
            if not data:
                print('Bye')
                break
            print('Received from client:',repr(data))
            # reverse the given string from client
            data = data[::-1]
            # send back reversed string to client
            conn.send(data)
        # connection closed
        conn.close()

    while 1:
        conn, addr = tcp_cServer.accept()
        if conn:
            print('Connected to: ', addr[0],':',addr[1])
            #Start  a new thread and return its identifier
            cThread = threading.Thread(target=threadedConn,args=(conn,))
            cThread.start()
    tcp_cServer.close()

