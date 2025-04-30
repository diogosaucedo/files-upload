#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do cliente
IP = '127.0.0.1'  # Endereço IP do servidor
PORTA = 1234       # Porta para conexão

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:
    # Conectar ao servidor
    conexao.connect((IP, PORTA))
    # Enviar dados ao servidor
    conexao.sendall(b"Ola mundaum!")
    # Receber resposta do servidor
    dados = conexao.recv(1024)
    conexao.close

print('Dados recebidos do servidor:', dados.decode())
