import socket
import sys
sys.path.append('../')
from enums import Options
from timeout import timeout

HOST = '127.0.0.1'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

itemList = []

try:
    udp.sendto("isOpen".encode(), dest)
    msg, cliente = udp.recvfrom(1024)
except:
    print("O leilão está fechado! Volte mais tarde!!")
    exit(1)

print(msg, cliente)
print("Digite seu email: ")
email = input()

print('Para sair digite sair\n')
msg=''
while msg != 'sair':
    print("1. Listar")
    print("2. Lance")
    print("3. Itens comprados")
    msg = input()
    if msg == "1":
        udp.sendto("list".encode(), dest) #mudar pq ta igual ao do vendedo
        msg, cliente = udp.recvfrom(1024)
    elif msg == "2":
        print("Digite o id do artigo: ", end="")
        idx = int(input())
        print("Digite o valor do lance: ", end="")
        lance = int(input())
        udp.sendto(f'lance,{idx},{lance}'.encode(), dest)
        msg, cliente = udp.recvfrom(1024)
    elif msg == "3":
        print("todo se a virose deixar")
    elif msg == "sair":
        udp.sendto(f'sair'.encode(), dest)
        break
    else:
        print("Não entendi!")
    
udp.close()