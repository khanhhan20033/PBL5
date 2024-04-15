import socket
import cv2
import numpy as np

server_address = ('localhost', 5678)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

print("Đã kết nối tới server")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    data = cv2.imencode('.jpg', frame)[1].tobytes()
    frame_size = len(data)
    header = np.array([frame_size], dtype=np.int32).tobytes()
    client_socket.sendall(header)
    client_socket.sendall(data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


client_socket.close()

cap.release()

cv2.destroyAllWindows()