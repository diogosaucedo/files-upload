#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do cliente
IP = '127.0.0.1'  # Endereço IP do servidor
PORTA = 1234       # Porta para conexão

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar-se ao servidor
sock.connect((IP,PORTA))

try:
    # Enviando uma mensagem
    mensagem = 'Oiii. Somente um teste'
    sock.sendall(mensagem.encode())

    #Esperando a resposta do servidor
    dados = sock.recv(4096)
    print('Resposta do servidor:', dados.decode())
    

finally:
    # Fecha conexao
    sock.close
