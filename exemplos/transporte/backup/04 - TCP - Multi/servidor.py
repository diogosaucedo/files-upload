import socket
import threading

# Função para lidar com as mensagens dos clientes
def handle_client(client_socket, client_address):
    print(f"Conexão estabelecida com {client_address}")
    while True:
        # Receber a mensagem do cliente
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            print(f"Conexão encerrada por {client_address}")
            break
        print(f"Cliente {client_address}: {message}")
        # Repassar a mensagem para todos os clientes conectados
        broadcast(message, client_socket)
    # Fechar a conexão com o cliente
    client_socket.close()

# Função para retransmitir a mensagem para todos os clientes, exceto o remetente
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode("utf-8"))

# Configurações do servidor
HOST = '0.0.0.0'  # Endereço IP do servidor
PORT = 55555        # Porta para escutar as conexões

# Criar um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5) # Especifica um número máximo de 5 cliente

print(f"Servidor de chat iniciado em {HOST}:{PORT}")

clients = []

while True:
    # Aceitar a conexão e obter o objeto de conexão e o endereço do cliente
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    # Iniciar uma thread para lidar com o cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
