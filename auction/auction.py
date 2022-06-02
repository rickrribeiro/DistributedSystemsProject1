import socket


HOST = ''             
PORT = 5000    
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
# nao deixar fechar com um leilao ativo
# udp = createSocket()
msg = "" 
customers = [] # client, name, wonqt
sellers = []
itensAbertos = [] # id, nome, vendedor, lance, customer
itensFechados = []# id, nome, vendedor, lance, customer
qtItens = 0
print("************ Leilão do xavier ********************")
while msg != "fechar":
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode()
    print(cliente, msg)
    if "isOpen" in msg:
        tp = msg.split("-")[1]
        if tp == "vendedor":
            sellers.append(cliente)
        else:
            customers.append(cliente)
        udp.sendto("True".encode(), cliente)
    elif msg == "close":
        for client in customers:
            udp.sendto("close".encode(), cliente)
        for client in sellers:
            udp.sendto("close".encode(), cliente)
        exit(1)
    elif msg == "listall":
        itens = ""
        for item in itensAbertos:
            itens+=f'id:{item[0]}\nnome:{item[1]}\nvendedor:{item[2]}\nlance:{item[3]}\ncomprador:{item[4]}\nestado: Aberto\n'
        udp.sendto(itens.encode(), cliente) 
    elif msg == "list":
        itens = ""
        for item in itensAbertos:
            if item[2] == cliente or item[4] == cliente:
                itens+=f'id:{item[0]}\nnome:{item[1]}\nvendedor:{item[2]}\nlance:{item[3]}\ncomprador:{item[4]}\nestado: Aberto\n'
        for item in itensFechados:
            if item[2] == cliente or item[4] == cliente:
                itens+=f'id:{item[0]}\nnome:{item[1]}\nvendedor:{item[2]}\nlance:{item[3]}\ncomprador:{item[4]}\nestado: Fechado\n'     
        udp.sendto(itens.encode(), cliente)    
    elif "add," in msg:
        data = msg.split(",")
        qtItens += 1
        itensAbertos.append([qtItens,data[1],cliente, data[2],""])
        udp.sendto("Itemadicionado!".encode(), cliente)
    elif "remove," in msg:
        #botar verificação se é o vendedor q criou
        data = msg.split(",")
        aux = ""
        for item in itensAbertos:
            if str(item[0]) == str(data[1]):
                aux = item
                itensAbertos.remove(item)
                break
        if aux =="":
            udp.sendto("Item não encontrado!".encode(), cliente)
        else:
            itensFechados.append(aux)
            udp.sendto("Item fechado!".encode(), cliente)
    elif "lance," in msg: #lance,{idx},{lance}
        data = msg.split(",")
        foi = 0
        for i in range(len(itensAbertos)):
            if str(itensAbertos[i][0]) == str(data[1]):
                if int(str(itensAbertos[i][3])) < int(str(data[2])): # POG pq tava bugando
                    itensAbertos[i][3] = int(str(data[2]))
                    itensAbertos[i][3] = cliente
                    udp.sendto("Lance registrado!".encode(), cliente)
                else:
                    udp.sendto("O lance precisa ser maior que o lance atual!".encode(), cliente)
                foi =1
                break
        if foi == 0:
            udp.sendto("Item não encontrado!".encode(), cliente)
                
                    
    else:
        udp.sendto("Não entendi!".encode(), cliente)


udp.close()
