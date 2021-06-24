import socket

while(True):
    target = input("digite a url ou ip do seu alvo ")
    port = input("digite a porta ")


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    codig = client.connect_ex((target,  int(port)))

    print (codig)