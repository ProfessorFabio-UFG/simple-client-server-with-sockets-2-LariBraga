from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

conta = input("Digite a conta: ") # recebe a conta a ser feita no formato "número1 número2 operação"

s.send(str.encode(conta))  # send some data
data = s.recv(1024)     # receive the response (do servidor)

print ("Resultado: " + bytes.decode(data)) # print the result

s.close() # close the connection