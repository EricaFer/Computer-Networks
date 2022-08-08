import socket

def TCPserver(host, port):
    global tcpd
    
    #Instanciando um servidor socket (ECO)
    tcpd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #'Vincula o servio a uma porta de servidor local'
    tcpd.bind((host,port))

    #autoriza o servio TCP sendo criado a atender as conexões
    # com a porta e IP vinculados anteriormente 
    tcpd.listen()

    #para aceitar uma conexão de um cliente TCP externo'
    # e começar a tratar uma mensagem encaminhada, faça:
    # addr = address de origem (cliente)
    conn,_ = tcpd.accept()

    #enquanto estou recebendo dados:
    while 1:

        data = conn.recv(1024)

        if not data:
            break 
        
        data_decoded = list(data.decode('unicode_escape'))

        count_dict = {}
        lista = []

        for i in range(0,len(data_decoded)):

            x = data_decoded[i]

            if (data_decoded[i] == data_decoded[i-1]) and (i != 0):

                count_dict[x] +=1

            else:
                count_dict[x] = 1

            try:
                if data_decoded[i] != data_decoded[i+1]:

                    lista.append((x,count_dict[x]))

            except IndexError as e:

                lista.append((x,count_dict[x]))

        new_list = [x+str(y) for x,y in lista]
        
        formated_str = ''.join(new_list)        
        
        # Echo service
        conn.sendall(formated_str.encode('unicode_escape'))
    
    conn.close()


