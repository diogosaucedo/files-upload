import socket
import threading

# Lista para armazenar todas as conexões de clientes
conexoes = []

# Função para lidar com cada conexão de cliente
def tratarCliente(conexao, ip):
    try:
        print('Conexão estabelecida com', ip)

        # Adicionar a conexão à lista de conexões
        conexoes.append(conexao)

        # Loop para receber dados do cliente
        while True:
            dados = conexao.recv(4096)
            if not dados:
                break  # Se não houver mais dados, sair do loop

            mensagem = dados.decode()
            if mensagem.lower() == 'exit':
                break

            for con in conexoes:
                if con != conexoes:
                    con.sendall(mensagem.encode())

    finally:
        # Fechar a conexão
        conexao.close()
        conexoes.remove(conexao)

# Configurações do Aplicatido no servidor
IP = '127.0.0.1'  # Endereço IPv4 do servidor - Seu IP
PORTA = 1234       # Porta para escutar as conexões: 1 - 65535

# Criar um socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite o reuso do endereço e porta quando disponíveis
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associar o socket ao endereço e porta do servidor
sock.bind((IP, PORTA))

# Escutar por conexões
sock.listen(5)  # Permitir até 5 conexões pendentes

print("Aguardando conexoes...")

try:
    while True:
        # Esperar por uma conexão
        conexao, ip = sock.accept()

        # Criar uma nova thread para lidar com a conexão
        #  ps -Tl -p <pid>
        novaThread = threading.Thread(target=tratarCliente, args=(conexao, ip))
        novaThread.start()

finally:
    # Fechar o socket do servidor
    sock.close()
