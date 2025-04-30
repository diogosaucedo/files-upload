#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do Aplicatido no servidor
IP = '127.0.0.1'  # Endereço IPv4 do servidor - Seu IP
PORTA = 1234       # Porta para escutar as conexões: 1 - 65535

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Atribuir a IP e Porta ao Socket
conexao.bind((IP, PORTA))

print("Aguardando conexoes...")
    # Aceitar a conexão e obter o objeto de conexão e o endereço do cliente

while True:
    # Esperar por uma mensagem do cliente
    dados, ip = conexao.recvfrom(4096)
    print('Recebido {} bytes de {}'.format(len(dados), ip))
    print('Conteudo:', dados.decode())
    
    # Responder ao cliente
    message = 'Ola, cliente!'
    conexao.sendto(message.encode(), ip)