#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do Aplicatido no servidor
IP = '127.0.0.1'  # Endereço IPv4 do servidor - Seu IP
PORTA = 1234       # Porta para escutar as conexões: 1 - 65535

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Atribuir a IP e Porta ao Socket
sock.bind((IP, PORTA))
sock.listen()

print("Aguardando conexoes...")

while True:
    # Esperar por uma mensagem do cliente
    conexao, ip = sock.accept()
    try:
        dados = conexao.recv(4096)
        print('Recebido {} bytes de {}'.format(len(dados), ip))
        print('Conteudo:', dados.decode())
        
        # Responder ao cliente
        message = 'Ola, cliente!'
        conexao.sendall(message.encode())

    finally:
        # Fechar conexao
        conexao.close