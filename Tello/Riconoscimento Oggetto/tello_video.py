from tello import Tello
from keyCommand import KeyCommand
from pynput import keyboard
from pynput.keyboard import Key
from datetime import datetime
import cv2

start_time = str(datetime.now().strftime('%d%m%Y%H%M%S'))

tello = Tello()
tello.send_command('command')
tello.send_command('streamon')
#telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")
#telloVideo = cv2.VideoCapture("udp://@192.168.10.1:11111")
telloVideo = cv2.VideoCapture('udp://192.168.10.1:11111')
telloVideo.set(3,640)
telloVideo.set(4,480)

while True:
    ret, frame = telloVideo.read()
    if ret:
        cv2.imshow('Tello Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

telloVideo.release()
cv2.destroyAllWindows()


log = tello.get_log()

out = open('log/log_' + start_time + '.txt', 'x')
for stat in log:
    stat.print_stats()
    out_str = stat.return_stats()
    out.write(out_str)






















