import socket

while(True):
    target = input("digite a url ou ip do seu alvo: ")
    port = input("digite a porta: ")
    time = input("tempo maximo de espera em segundos: ")


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(int(time))
    codig = client.connect_ex((target,  int(port)))

    print (codig)
