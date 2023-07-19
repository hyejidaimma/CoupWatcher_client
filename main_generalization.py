import socket

def send_product_info(server_host, server_port, product_name, desired_price, product_link):
    # 서버에 연결
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected to server {server_host}:{server_port}")

    # 상품 정보를 서버에 전송
    data = f"{product_name},{desired_price},{product_link}"
    client_socket.send(data.encode())

    # 서버로부터 응답 수신
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

    # 연결 종료
    client_socket.close()

# 서버 호스트와 포트 정보
server_host = 'localhost'
server_port = 12345

# 테스트할 상품 정보
product_name = "상품명"
desired_price = "10000"
product_link = "https://example.com/product"

# 서버에 상품 정보 전송
send_product_info(server_host, server_port, product_name, desired_price, product_link)
