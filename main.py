'''
import socket

def send_data(server_address, data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    client_socket.sendall(data.encode())
    client_socket.close()

# 서버 주소와 포트
server_address = ('localhost', 12345)

# 데이터 전송 테스트
send_data(server_address, "Hanwoo,12000,https://www.coupang.com/vp/products/1267767150?itemId=2271396043&vendorItemId=70268609273&pickType=COU_PICK&sourceType=CATEGORY&categoryId=194176&isAddedCart=")
'''

import socket
import threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 12345)

sock.connect(server_address)

# 서브스레드(수신)
def handler(sock):  # c: 소켓, a: 주소

    while True:
        try:
            data = sock.recv(1024)
            if not data:  # 데이터가 없으면 연결이 종료된 것이므로 소켓 제거
                #sock.close()
                continue
        except:
            print("예외가 발생했습니다.")
            continue
        else:
            print(f'received Message : {data.decode()}')


cThread = threading.Thread(target=handler, args=(sock,))
cThread.daemon = True
cThread.start()
# 메인함수(송신)
a = 0
while True:
    msg = "Hanwoo,12000,https://www.coupang.com/vp/products/1267767150?itemId=2271396043&vendorItemId=70268609273&pickType=COU_PICK&sourceType=CATEGORY&categoryId=194176&isAddedCart="
    try:  # 데이터 전송
        if a == 0:
            sock.send(msg.encode())  # 메시지 전송
            a += 1

    except:  # 연결이 종료됨
        print("연결이 종료되었습니다")
        break
