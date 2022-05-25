from socketconf import createSocket
# nao deixar fechar com um leilao ativo
udp = createSocket()
msg = "" #Xìnxī
customers = [] # client, name, wonqt
itens = []
sellers = []
print("************ Leilão do xavier ********************")
while msg != "fechar":
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode()
    print(cliente, msg)
    if msg == "isOpen":
        udp.sendto("True".encode(), cliente)
    if msg == "close":
        for client in customers:
            udp.sendto("close".encode(), cliente)
            exit(1)
            
udp.close()
