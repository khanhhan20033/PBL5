import cv2
import socket
import pickle

# Khởi tạo kết nối TCP với server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5678)
client_socket.connect(server_address)

# Chụp ảnh từ máy ảnh của client sử dụng OpenCV
camera = cv2.VideoCapture(0)
_, frame = camera.read()

# Chuyển đổi ảnh thành định dạng byte và gửi qua kết nối TCP
data = pickle.dumps(frame)
client_socket.sendall(data)

# Đóng kết nối
client_socket.close()
camera.release()
