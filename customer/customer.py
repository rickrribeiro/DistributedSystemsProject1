import socket
import sys
sys.path.append('../')
# from enums import Options
# from timeout import timeout

HOST = '127.0.0.1'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

itemList = []

try:
    udp.sendto("isOpen-comprador".encode(), dest)
    msg, cliente = udp.recvfrom(1024)
except:
    print("O leilão está fechado! Volte mais tarde!!")
    exit(1)

print(msg, cliente)


print('Para sair digite sair\n')
msg=''
while msg != 'sair':
    print("1. Listar leilões com lance e comprados")
    print("2. Listar todos os leilões em aberto")
    print("3. Lance")
    print("digite 'sair' para sair")
    msg = input()
    if msg == "1":
        udp.sendto("list".encode(), dest) #mudar pq ta igual ao do vendedo
        msg, cliente = udp.recvfrom(1024)
    elif msg == "2":
        udp.sendto("listall".encode(), dest) #mudar pq ta igual ao do vendedo
        msg, cliente = udp.recvfrom(1024)
        print(msg.decode())
    elif msg == "3":
        print("Digite o id do artigo: ", end="")
        idx = int(input())
        print("Digite o valor do lance: ", end="")
        lance = int(input())
        udp.sendto(f'lance,{idx},{lance}'.encode(), dest)
        msg, cliente = udp.recvfrom(1024)
        print(msg.decode())
    elif msg == "sair":
        udp.sendto(f'sair'.encode(), dest)
        break
    else:
        print("Não entendi!")
    
udp.close()