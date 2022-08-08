import socket

def UDPserver(host,port):
    udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address = (host,port)

    udp_server.bind(server_address)

    # enquanto estou recebendo dados:
    while 1:
        data,address = udp_server.recvfrom(1024)
        if not data:
            break

        decoded = data.decode('utf-8')
        expected_msg = f'Hello, world! From {host}:{port}'

        if decoded == expected_msg:
            encode_msg = 'Sucesso'
            print('Servidor recebeu a mensagem correta')

        else:
            encode_msg = 'Erro'
            print('Servidor nao recebeu a mensagem correta')

        # Echo service
        udp_server.sendto(encode_msg.encode('utf-8'),address)
         
    udp_server.close()