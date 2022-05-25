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
earn = 0

try:
    udp.sendto("isOpen".encode(), dest)
    msg, cliente = udp.recvfrom(1024)
except:
    print("O leilão está fechado! Volte mais tarde!!")
    exit(1)

print(msg, cliente)
print('Para sair digite sair\n')
msg=''
while msg != 'sair':
    print("1. Listar meus artigos")
    print("2. Adicionar artigo")
    print("3. Remover artigo")
    print("4. Ganhos")
    print("sair")
    msg = input()
    if msg == "1":
        udp.sendto("list".encode(), dest)
        msg, cliente = udp.recvfrom(1024)
    elif msg == "2":
        print("Digite o nome do artigo: ", end="")
        nome = input()
        print("Digite o preço do artigo: ", end="")
        preco = int(input())
        udp.sendto(f'add,{nome},{preco}'.encode(), dest)
        msg, cliente = udp.recvfrom(1024)
    elif msg == "3":
        print("Digite o id do artigo: ", end="")
        idx = int(input())
        udp.sendto(f'remove,{idx}'.encode(), dest)
        msg, cliente = udp.recvfrom(1024)
    elif msg == "4":
        udp.sendto(f'ganhos'.encode(), dest)
        msg, cliente = udp.recvfrom(1024)
    elif msg == "sair":
        udp.sendto(f'sair'.encode(), dest)
        break
    else:
        print("Não entendi!")


    udp.sendto(msg.encode(), dest)
udp.close()