import socket
import multiprocessing

def handle_client(client_socket):
    """Função que lida com a comunicação com um cliente"""
    print('Conexão recebida de:', client_socket.getpeername())
    while True:
        request = client_socket.recv(1024)
        if not request:
            break
        print('Recebido:', request.decode('utf-8'))
        client_socket.send(b'Hello from server!')
    client_socket.close()

def server(host='0.0.0.0', port=9999):
    """Função que inicia o servidor e aceita conexões"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f'Servidor escutando em {host}:{port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Conexão aceita de {addr}')

        # Cria um novo processo para lidar com o cliente
        process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        process.start()

# ps -ef f | grep servidor2.py
if __name__ == "__main__":
    server()
