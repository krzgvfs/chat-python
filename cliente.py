import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))

terminado = False

print("Enter 'exit' to close chat")

while not terminado:
    cliente.send(input('New msg: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'exit':
        terminado = True
    else:
        print(msg)
cliente.close()
