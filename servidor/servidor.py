import socket
import os

# Configurações do servidor
IP = '127.0.0.1'  # Endereço IPv4 do servidor
PORTA = 1234      # Porta para escutar as conexões

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Atribuir IP e Porta ao Socket
sock.bind((IP, PORTA))
sock.listen(1)  # Aceita apenas 1 conexão por vez

print("Servidor aguardando conexões em", IP, ":", PORTA)

while True:
    # Esperar por uma conexão do cliente
    conexao, endereco_cliente = sock.accept()
    print(f"Conexão estabelecida com {endereco_cliente}")
    
    try:
        # Receber o tamanho do nome do arquivo (4 bytes)
        tamanho_nome = int.from_bytes(conexao.recv(4), byteorder='big')
        
        # Receber o nome do arquivo usando o tamanho recebido
        nome_arquivo = conexao.recv(tamanho_nome).decode()
        print(f"Recebendo arquivo: {nome_arquivo}")
        
        # Criar diretório 'arquivos' se não existir
        if not os.path.exists('arquivos'):
            os.makedirs('arquivos')
        
        # Criar o caminho completo do arquivo dentro do diretório 'arquivos'
        caminho_arquivo = os.path.join('arquivos', nome_arquivo)
        
        # Receber o tamanho do arquivo (8 bytes)
        tamanho_arquivo = int.from_bytes(conexao.recv(8), byteorder='big')
        
        # Criar o arquivo para escrita
        bytes_recebidos = 0
        with open(caminho_arquivo, 'wb') as arquivo:
            while bytes_recebidos < tamanho_arquivo:
                # Calcular quanto falta receber
                bytes_restantes = tamanho_arquivo - bytes_recebidos
                # Definir o tamanho do chunk (mínimo entre 4096 e bytes restantes)
                chunk_size = min(4096, bytes_restantes)
                # Receber os dados do arquivo em chunks
                dados = conexao.recv(chunk_size)
                if not dados:
                    break
                arquivo.write(dados)
                bytes_recebidos += len(dados)
        
        print(f"Arquivo {nome_arquivo} recebido e salvo com sucesso!")
        # Enviar confirmação ao cliente
        conexao.send("Arquivo recebido com sucesso!".encode())
        
    except Exception as e:
        print(f"Erro durante a transferência: {str(e)}")
        conexao.send(f"Erro: {str(e)}".encode())
    
    finally:
        # Fechar a conexão
        conexao.close()