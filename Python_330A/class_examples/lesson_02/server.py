import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

server_socket.bind(('127.0.0.1', 50000))

server_socket.listen(1)

connection, client_address = server_socket.accept()

