#Importa a biblioteca de socket no python
#https://realpython.com/python-sockets/#tcp-sockets
import socket
import threading

running = True

# Função para lidar com a recepção de mensagens do servidor
def receive_messages(sock):
    global running
    while running:
        try:
            data = sock.recv(4096)
            if not data:
                break
            print(data.decode())
        except Exception as e:
            print("Erro ao receber mensagem:", e)
            break
    print("Fim da thead")

# Configurações do cliente
IP = '127.0.0.1'  # Endereço IP do servidor
PORTA = 1234       # Porta para conexão

# Criar um socket TCP/IP
# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM --> UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar-se ao servidor
    sock.connect((IP,PORTA))

    # Iniciar a thread para receber mensagens do servidor
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    # Loop para enviar mensagens ao servidor
    while True:
        mensagem = input()
        sock.sendall(mensagem.encode())
        if mensagem.lower() == 'exit':
            running = False  # Define a variável de controle para False para encerrar a thread
            break
        #sock.sendall(mensagem.encode())

except KeyboardInterrupt:
    print("Finalizando...")
    sock.sendall("exit".encode())
    

finally:
    # Fecha conexao
    print("Fechando!")
    running = False
    sock.close
    
