import socket

cs = socket.socket()

print('welcome to discord lite chatserver !')
try:
	cs.connect(('', 5000))
	while True:
		name = input("Enter your name : ")
		cs.send(name.encode('utf-8'))
		res = cs.recv(1024).decode('utf-8')
		if res.startswith('username'):
			continue
		else:
			break
except socket.error as e:
    print(str(e))

while True:
    msg = input('Enter a message : ')
    cs.send(str.encode(msg))
    res = cs.recv(1024)
    print(res.decode('utf-8'))

cs.close()
