# Python Programm zum Öffnen/Schließen des Gripper
# author: Michael Engelmann
# date: 21.7.2022

import socket

HOST = "192.168.1.1" # IP-Adresse des UR3
PORT = 30002 # Port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Socket-Message
# (0,False)-> Gripper öffnen, (0,True)-> Gripper schließen
data = "set_tool_digital_out(0,True)" + "\n"

# Übertragung der Socket-Message
s.send(data.encode())

data = s.recv(1024)
s.close()

print ("Received", repr(data))
