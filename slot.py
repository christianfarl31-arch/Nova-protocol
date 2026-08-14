# slot.py - N.O.V.A. Slot v1.2 "Peanuts" 
import socket, hashlib, base64, time
TISCH_IP = '127.0.0.1'; PORT = 4761
MY_ID = "PC-BERLIN-442"; HEAT = True
print(f"💎 N.O.V.A. Slot {MY_ID} online. HEAT:{HEAT}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((TISCH_IP, PORT))
    anfrage = s.recv(1024).decode().strip()
    print(f"Tisch sagt: {anfrage}")
    s.sendall(f"ME:{MY_ID} LAT:12 B:0.04 HEAT:{HEAT}\n".encode())
    job = s.recv(1024).decode().strip()
    print(f"Job erhalten: {job}")
    if "JOB:" in job:
        time.sleep(0.1) # Simuliere Arbeit
        fake_bild = b"NOVA_FRAME_4821_DATA"
        hash_val = hashlib.sha256(fake_bild).hexdigest()
        data_b64 = base64.b64encode(fake_bild).decode()
        s.sendall(f"DONE:FRAME_4821 HASH:{hash_val} DATA:{data_b64}\n".encode())
        payment = s.recv(1024).decode().strip()
        print(f"💰 Peanuts erhalten: {payment}")
