import socket
import sys
import os

# Verificar argumentos da linha de comando
if len(sys.argv) != 3:
    print("Uso: python3 cliente.py <ip-do-servidor> <arquivo>")
    sys.exit(1)

# Obter argumentos da linha de comando
IP_SERVIDOR = sys.argv[1]
ARQUIVO = sys.argv[2]

# Verificar se o arquivo existe
if not os.path.exists(ARQUIVO):
    print(f"Erro: O arquivo {ARQUIVO} não existe!")
    sys.exit(1)

# Configurações de conexão
PORTA = 1234  # Mesma porta do servidor

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar ao servidor
    print(f"Conectando ao servidor {IP_SERVIDOR}:{PORTA}...")
    sock.connect((IP_SERVIDOR, PORTA))
    
    # Preparar o nome do arquivo
    nome_arquivo = os.path.basename(ARQUIVO)
    nome_arquivo_bytes = nome_arquivo.encode()
    
    # Enviar o tamanho do nome do arquivo (4 bytes)
    sock.send(len(nome_arquivo_bytes).to_bytes(4, byteorder='big'))
    
    # Enviar o nome do arquivo
    sock.send(nome_arquivo_bytes)
    
    # Obter o tamanho do arquivo
    tamanho_arquivo = os.path.getsize(ARQUIVO)
    
    # Enviar o tamanho do arquivo (8 bytes)
    sock.send(tamanho_arquivo.to_bytes(8, byteorder='big'))
    
    # Enviar o conteúdo do arquivo
    with open(ARQUIVO, 'rb') as arquivo:
        while True:
            dados = arquivo.read(4096)
            if not dados:
                break
            sock.sendall(dados)
    
    # Aguardar confirmação do servidor
    resposta = sock.recv(1024).decode()
    print(f"Resposta do servidor: {resposta}")

except ConnectionRefusedError:
    print(f"Erro: Não foi possível conectar ao servidor {IP_SERVIDOR}:{PORTA}")
except Exception as e:
    print(f"Erro durante a transferência: {str(e)}")

finally:
    # Fechar a conexão
    sock.close()