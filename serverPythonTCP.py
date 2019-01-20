# from socket import *
import socket

HOST = '127.0.0.1'   # or 127.0.0.1 or localhost
PORT = 2600
ADDR = (HOST,PORT)
BUFFER = 4096

#create a socket (SRV)
#see python docs for socket for more info

srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind socket to address
srv.bind((ADDR))	#double parens create a tuple with one object
srv.listen(5) # maximum queued connections is 5
a = True
while a:
    conn,addr = srv.accept() #accepts the connection
    print ('...connected!' ,' ',addr)
    conn.sendall('Wohhhowwwww'.encode('utf-8'))
    data =conn.recv(BUFFER) 
    print(data)
conn.close()