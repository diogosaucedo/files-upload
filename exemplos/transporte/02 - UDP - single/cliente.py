#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do cliente
IP = '127.0.0.1'  # Endereço IP do servidor
PORTA = 1234       # Porta para conexão

# Criar um socket TCP/IP
# socket.SOCK_DGRAM --> UDP
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Enviando uma mensagem
    mensagem = 'Oiii. Somente um teste'
    conexao.sendto(mensagem.encode(), (IP,PORTA) )

    #Esperando a resposta do servidor
    dados, ip = conexao.recvfrom(4096)
    print('Resposta do servidor:', dados.decode())
    

finally:
    # Fecha conexao
    conexao.close
