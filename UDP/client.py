# This is client code to receive video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.1.57'  # socket.gethostbyname(host_name)
print(host_ip)
port = 9999

# client_socket.sendto(b'Hello', (host_ip, port))
vid = cv2.VideoCapture(0)  # replace 'rocket.mp4' with 0 for webcam

fps, st, frames_to_count, cnt = (0, 0, 20, 0)

while True:
    # msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    # print('GOT connection from ', client_addr)
    WIDTH = 400
    while vid.isOpened():
        _, frame = vid.read()
        frame = imutils.resize(frame, width=WIDTH)
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        print("bufer")
        print(buffer)
        message = base64.b64encode(buffer)
        print("message")
        print(message)
        client_socket.sendto(message, ('192.168.1.57', 9999))
        frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('TRANSMITTING VIDEO', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            client_socket.close()
            break
        if cnt == frames_to_count:
            try:
                fps = round(frames_to_count / (time.time() - st))
                st = time.time()
                cnt = 0
            except:
                pass
        cnt += 1
''''
fps, st, frames_to_count, cnt = (0, 0, 20, 0)
while True:
    packet, _ = client_socket.recvfrom(BUFF_SIZE)

    data = base64.b64decode(packet, ' /')

    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("RECEIVING VIDEO", frame)
    key = cv2.waitKey(1) & 0xFF
    print("packet")
    print(packet)
    print("data")
    print(data)
    print("npdata")
    print(npdata)
    print("frame")
    print(frame)
    if key == ord('q'):
        client_socket.close()
        break
    if cnt == frames_to_count:
        try:
            fps = round(frames_to_count / (time.time() - st))
            st = time.time()
            cnt = 0
        except:
            pass
    cnt += 1
'''
