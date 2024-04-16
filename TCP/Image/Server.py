import socket
import pickle
import cv2

# Khởi tạo server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',5678)
server_socket.bind(server_address)
server_socket.listen(1)

print("Đang chờ kết nối từ client...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()
print("Đã kết nối với", client_address)

# Nhận dữ liệu ảnh từ client
data = b""
while True:
    packet = client_socket.recv(4096)
    if not packet: break
    data += packet

# Giải nén dữ liệu ảnh và hiển thị
frame = pickle.loads(data)
cv2.imshow('Received Image', frame)
cv2.waitKey(0)

# Đóng kết nối
client_socket.close()
server_socket.close()
