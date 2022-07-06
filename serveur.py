import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Bonjour petit client ","utf-8"))
    reponse = clientsocket.recv(255)
    print("Le clinet a envoyé : "+reponse.decode("utf-8") )

