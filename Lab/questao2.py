from base64 import encode
import socket

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
    conn,_ = tcp_server.accept()

    # enquanto estou recebendo dados:
    while 1:
        data = conn.recv(1024)
        if not data:
            break

        decoded = data.decode('unicode_escape')

        expected_msg = f'Hello, world! From {host}:{port}'

        if decoded == expected_msg:

            encode_msg = 'Sucesso'

            print('Servidor recebeu a mensagem correta')

        else:
            encode_msg = 'Erro'

            print('Servidor nao recebeu a mensagem correta')

        # Echo service
        conn.sendall(encode_msg.encode('unicode_escape'))
    
    conn.close()