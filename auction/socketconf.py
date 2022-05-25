import socket

def createSocket():
    HOST = ''             
    PORT = 5000    
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    return udp

