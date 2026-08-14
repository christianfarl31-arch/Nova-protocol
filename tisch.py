# tisch.py - N.O.V.A. Tisch v1.2 "Peanuts"
import socket
HOST, PORT = '0.0.0.0', 4761
print("🔨 N.O.V.A. Tisch online. Port 4761 = 4e:6f:76:61")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)); s.listen()
    print("Warte auf Slots...")
    while True:
        conn, addr = s.accept()
        with conn:
            conn.sendall(b"WHO:FRAME_RENDER B:0.05 LAT:200\n")
            angebot = conn.recv(1024).decode().strip()
            print(f"Angebot von {addr}: {angebot}")
            if "ME:" in angebot:
                slot_id = angebot.split("ME:")[1].split()[0]
                conn.sendall(f"YOU:{slot_id} JOB:FRAME_4821\n".encode())
                ergebnis = conn.recv(1024).decode().strip()
                print(f"Ergebnis: {ergebnis}")
                conn.sendall(f"PAID:FRAME_4821 TO:{slot_id} AMT:0.04\n".encode())
                print(f"💰 Peanuts bezahlt an {slot_id}")
