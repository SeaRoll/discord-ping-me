from python_imagesearch.imagesearch import imagesearch
import requests
import time

server_ip = "localhost"
user_id = ''
port = 5000

def run_subthread():
  global server_ip, port, user_id
  print('starting thread')
  # check pic.png exists with imagesearch
  while True:
    pos = imagesearch("pic.png")
    if pos[0] == -1:
      print('Image was not found! Which means you are online. sending to bot')
      # send an http request to the server
      requests.get(f'http://{server_ip}:{port}/done/{user_id}')
      return
    time.sleep(1)

user_id = input('Enter your discord id: ')
run_subthread()