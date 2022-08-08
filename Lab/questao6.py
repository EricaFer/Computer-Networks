import socket
import re

def UDPserver(host, port):
    global udpd
    
    udpd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address = (host,port)

    udpd.bind(server_address)

    # enquanto estou recebendo dados:
    while 1:
        data,address = udpd.recvfrom(1024)

        if not data:
            break

        password = data.decode('utf-8')
        pattern = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,32}$"

        result = re.match(pattern,password)

        if result:
            msg = 'Senha valida.'

        else:
            msg = 'Senha inválida!'

        udpd.sendto(msg.encode('utf-8'),address)
         
    udpd.close()