from socket import *

HOST = 'localhost'
PORT = 2600
ADDR = (HOST,PORT)
BUFFER = 4096

cli = socket(AF_INET,SOCK_STREAM)
cli.connect((ADDR))

data = cli.recv(BUFFER)
print (data)

cli.close()