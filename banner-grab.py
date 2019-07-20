#! /usr/bin/python3

import socket

ports = [21, 22, 25, 3306, 80]

for port in ports:
    s = socket.socket()
    print("Banner for port: ", port)

    try:
        s.connect(("192.168.1.27", port))
        answer = s.recv(1024)
        print(answer)

        s.close()
    except:
        print("IP/Port not reacheable or down.")

