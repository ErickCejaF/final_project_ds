import socket
import RPi.GPIO as GPIO
import time

HOST = '192.168.43.245'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            GPIO.output(21,GPIO.HIGH)
            time.sleep(1)
            data = conn.recv(1024)
            GPIO.output(21,GPIO.LOW)
            if not data:
                break
            conn.sendall(data)
