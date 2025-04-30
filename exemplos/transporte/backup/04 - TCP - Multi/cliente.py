import socket
import threading
import sys

# Função para lidar com a recepção de mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            # Receber e exibir mensagens do servidor
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            # Se ocorrer algum erro, desconectar o cliente
            print("Erro ao receber mensagem do servidor.")
            client_socket.close()
            break

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 55555        # Porta para conexão

# Conectar ao servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Iniciar uma thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Enviar mensagens para o servidor
while True:
    message = input()
    client_socket.send(message.encode("utf-8"))

