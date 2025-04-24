import socket
from threading import Thread

SERVER_HOST = "192.168.137.158"
SERVER_PORT = 5002
separator_token = "<SEP>"

name = input("Masukkan nama kamu: ")

s = socket.socket()
print(f"[+] Menghubungkan ke {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Terhubung.")

def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            print("\n" + message)
        except Exception as e:
            print("[!] Terputus dari server.")
            break

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    msg = input()
    if msg.lower() == "exit":
        break
    full_msg = f"{name}{separator_token}{msg}"
    s.send(full_msg.encode())

s.close()
