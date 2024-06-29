import socket
import json

PORT = 5050

SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
def starting():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(ADDR)
        server.listen(1)
        while True:
            conn, addr = server.accept()
            with conn:
                log_data = b""
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    log_data += data
                    if log_data:
                        log_data = json.loads(log_data.decode("utf-8"))
                        print("Received data: ")
                        print(log_data)


if __name__ == "__main__":
    starting()
