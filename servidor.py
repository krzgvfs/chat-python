import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8888))

servidor.listen() # Escutando requisições
cliente, end = servidor.accept()

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'exit':
        terminado = True
    else:
        print(msg)
    cliente.send(input('New msg: ').encode('utf-8'))

cliente.close()
servidor.close()