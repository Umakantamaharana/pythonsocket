import socket
from _thread import *
import pyfiglet

serversocket = socket.socket()
print(pyfiglet.figlet_format("WELCOME \nTO DISCORD"))
threads = 0
clientdb = {}

try:
	serversocket.bind(('',5000))
except socket.error as e:
	print(str(e))

serversocket.listen()

def multithread(cl):
	cl.send(str.encode("You are joined"))
	while True:
		msg = cl.recv(1024).decode('utf-8')
		print()		
		print(clientdb[cl]+" : "+msg)
		if msg.startswith('@'):
			to = msg.split(':')[0][1:]
			msg = msg.split(':')[1]
			try:
				clientdb[to].send(msg.encode('utf-8'))
			except:
				print(to + " disconnected..")
		
		if not msg:
			break
		cl.sendall("received by server".encode('utf-8'))
	cl.close()
	
while True:
	cl, addr = serversocket.accept()
	def con():
		global name
		name = cl.recv(1024).decode('utf-8')
		if name in clientdb:
			cl.send("username exists. please use other name.".encode('utf-8'))
			name = ''
			con()
		else:
			return name
	con()
	# print("Connected to "+ name)
	print(pyfiglet.figlet_format(name+" connected"))
	clientdb[cl] = name
	start_new_thread(multithread, (cl, ))
	# threads = threads + 1
	# print("Thread no : "+str(threads))
	
serversocket.close()
	
