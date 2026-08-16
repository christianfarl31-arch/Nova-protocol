#!/usr/bin/env python3
# N.O.V.A. v0.1 - Protocol for 5ms compute
# Port 4761 = 4e:6f:76:61 = Nova in Hex
# HEAT:TRUE

import socket
import time
import json
import sys
import argparse

PORT = 4761
HOST = '0.0.0.0'

def serve():
    """Tisch sein: HEAT:TRUE auf Port 4761"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"🧬 N.O.V.A. Tisch offen auf {HOST}:{PORT}")
        print(f"HEAT:TRUE, TTL:5ms, CAP:10")
        print("Warte auf Jobs... Strg+C zum Beenden")

        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    t_start = time.time_ns()
                    data = conn.recv(1024)
                    if not data: continue

                    try:
                        job = json.loads(data.decode())
                        if job.get("op") == "ping":
                            # Simuliere 1ms Arbeit
                            time.sleep(0.001)

                            t_end = time.time_ns()
                            latency_us = (t_end - t_start) // 1000

                            response = {
                                "op": "pong",
                                "ttl_ms": 5,
                                "latency_us": latency_us,
                                "heat": True,
                                "cap": 9,
                                "port": PORT
                            }
                            conn.sendall(json.dumps(response).encode())
                            print(f"Pong -> {addr[0]} in {latency_us}us")
                        else:
                            conn.sendall(b'{"error":"unknown_op"}')
                    except json.JSONDecodeError:
                        conn.sendall(b'{"error":"bad_json"}')
            except KeyboardInterrupt:
                print("\nHEAT:FALSE. Tisch schließt.")
                break

def ping(target='127.0.0.1'):
    """Kunde sein: Ping an Tisch schicken"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.01) # 10ms Timeout
        try:
            t_start = time.time_ns()
            s.connect((target, PORT))

            job = {"op": "ping", "ttl_ms": 5}
            s.sendall(json.dumps(job).encode())

            data = s.recv(1024)
            t_end = time.time_ns()

            rtt_us = (t_end - t_start) // 1000
            response = json.loads(data.decode())

            print(f"Pong von {target}:{PORT}")
            print(f"Antwort: {response}")
            print(f"RTT: {rtt_us}us = {rtt_us/1000:.2f}ms")

            if rtt_us < 5000:
                print("✅ HEAT:TRUE - Unter 5ms! Hypernet lebt!")
            else:
                print("❌ Zu langsam für N.O.V.A. >5ms")

        except socket.timeout:
            print("❌ Timeout. Kein Tisch auf Port 4761?")
        except ConnectionRefusedError:
            print("❌ Verbindung abgelehnt. Läuft der Tisch?")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='N.O.V.A. v0.1 Tisch oder Client')
    parser.add_argument('--serve', action='store_true', help='Starte als Tisch auf Port 4761')
    parser.add_argument('--ping', type=str, nargs='?', const='127.0.0.1',
                       help='Pinge einen Tisch. Default: 127.0.0.1')

    args = parser.parse_args()

    if args.serve:
        serve()
    elif args.ping:
        ping(args.ping)
    else:
        print("N.O.V.A. v0.1")
        print("Nutze: python nova.py --serve ODER python nova.py --ping")
