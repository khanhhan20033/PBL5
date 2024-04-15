import socket
import cv2
import numpy as np

server_address = ('localhost', 5678)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)


server_socket.listen()

print("Server đang chờ kết nối...")

client_socket, client_address = server_socket.accept()

print("Đã kết nối với client:", client_address)

while True:
    data = client_socket.recv(4)
    if not data:
        break

    frame_size = np.frombuffer(data, dtype=np.int32)[0]
    data = b''
    received_size = 0
    while received_size < frame_size:
        chunk = client_socket.recv(65536)
        if not chunk:
            break
        data += chunk
        received_size += len(chunk)

    if received_size == frame_size:

        frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)

        cv2.imshow("Video từ client", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
server_socket.close()
cv2.destroyAllWindows()