import socket

IP = '0.0.0.0'
PORTA = 80 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORTA))
sock.listen()

print("Aguardando conexoes...")

while True:
    conexao, ip = sock.accept()
    try:
        dados = conexao.recv(4096)
        print('Recebido {} bytes de {}'.format(len(dados), ip))
        print('Conteudo:', dados.decode())
        
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
                  <html><body><h1>Funfo!</h1></body></html>"""
        conexao.sendall(message.encode())

    finally:
        # Fechar conexao
        conexao.close