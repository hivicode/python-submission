import socket
from threading import Thread

SERVER_HOST = "192.168.137.158"
SERVER_PORT = 5002
separator_token = "<SEP>"
name = input("Masukkan nama anda: ")

s = socket.socket()
print(f"[*] Menghubungkan ke {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Terhubung.")

def listen_for_messages():
    while True:
        try:
            msg = s.recv(1024).decode()
            print("\n" + msg)
        except Exception as e:
            print("[!] Koneksi terputus:", e)
            s.close()
            break

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == "exit":
        break
    message = f"{name}{separator_token}{to_send}"
    try:
        s.send(message.encode())
    except Exception as e:
        print("[!] Error mengirim pesan: ", e)
        break
s.close()
