import socket
from threading import Thread


clients = []

HOST = "localhost"
PORT = 5000
BUFFERSIZE = 4096
ADDR = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)

def handler():
  global client
  while True:
    client, client_adress = SERVER.accept()
    clid = client.recv(BUFFERSIZE).decode("utf8")
    print("%s:%s Bağlandı!" %client_adress)
    clients.append((clid,client))

def inp():
  while True:
    com = input()
    if com == "!clients":
      print(len(clients), "Adet Client var")
    else:
      broadcast(com.encode("utf8"))

def broadcast(msg):
  for x in clients:
    x[1].send(msg)


if __name__ == "__main__":
  SERVER.listen()
  print("Bağlantı Bekleniyor...")
  initialServer = Thread(target = handler)
  initialHandler = Thread(target = inp)
  initialHandler.start()
  initialServer.start()
  initialServer.join()
  initialHandler.join()
  SERVER.close()
