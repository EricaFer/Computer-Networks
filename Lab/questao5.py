import socket
#Exemplo end-to-end de um cliente TCP
def UDPclient(host,port):
    udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address = (host,port)

    encoded_msg = f'Hello, world! From {host}:{port}'.encode('utf-8')

    status = udp_client.sendto(encoded_msg,server_address)

    if status > 0:
        data = udp_client.recv(1024)

        print(f'Saida:  {data.decode("utf-8")}')
         
    udp_client.close()