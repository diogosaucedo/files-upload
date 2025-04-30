#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket

# Configurações do Aplicatido no servidor
IP = '127.0.0.1'  # Endereço IPv4 do servidor - Seu IP
PORTA = 1234       # Porta para escutar as conexões: 1 - 65535

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:
    # Atribuir a IP e Porta ao Socket
    conexao.bind((IP, PORTA))
    # Colocar o socket para escutar por conexões
    conexao.listen()

    print("Aguardando conexões...")
    # Aceitar a conexão e obter o objeto de conexão e o endereço do cliente
    conn, addr = conexao.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            # Receber dados do cliente
            dados = conn.recv(1024)
            if not dados:
                break
            # Imprimir os dados recebidos
            print('Dados recebidos:', dados.decode())
            # Enviar dados de volta ao cliente
            conn.sendall(dados)
