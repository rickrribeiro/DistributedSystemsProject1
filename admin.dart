import 'dart:io';

void main(List<String> args){
  RawDatagramSocket.bind(InternetAddress.ANY_IP_V4, 0).then((RawDatagramSocket socket){
    print('Sending from ${socket.address.address}:${socket.port}');
    int port = 5000;
    socket.send('closeXavier'.codeUnits,'127.0.0.1', port);
  });
}