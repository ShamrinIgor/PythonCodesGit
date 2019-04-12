import socket, threading, time, random

shutdown = False
join = False

Dictinary = {\
"a" : [7, 31, 50, 63, 66, 77, 84],\
"b" : [11, 64],\
"c" : [17, 33, 49],\
"d" : [10, 27, 51, 76],\
"e" : [25, 26, 28, 32, 48, 67, 69, 72, 75, 79, 82, 85],\
"f" : [8, 9],\
"g" : [44, 83],\
"h" : [19, 20, 21, 54, 70, 87],\
"i" : [2, 3, 29, 53, 68, 73],\
"j" : [18],\
"k" : [41],\
"l" : [42, 81, 86, 95],\
"m" : [40, 52],\
"n" : [0, 43, 80, 88, 89],\
"o" : [16, 30, 61, 65, 91, 94, 96],\
"p" : [1, 62],\
"q" : [15],\
"r" : [4, 24, 39, 58, 71, 99],\
"s" : [6, 34, 56, 57, 59, 90],\
"t" : [5, 23, 35, 37, 38, 60, 74, 78, 92],\
"u" : [13, 14, 36],\
"v" : [22],\
"w" : [45, 46],\
"x" : [12],\
"y" : [55, 93],\
"z" : [47]}

def my_encode(message):
	encrypted_message = ""

	for char in message:
	     char = Dictinary[char][random.randint(0,len(Dictinary[char]) - 1)]
	     encrypted_message += str(char) + ' '
	return encrypted_message

def my_decode(message):
    decrypted_message = ""
    numbers = message.split()
    for i in numbers:
        for letter in Dictinary:
            if int(i) in Dictinary[letter]:
                decrypted_message += letter

    return decrypted_message

def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				#print((data.decode("utf-8")))
				encrypted_message = ""; prefix = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						prefix += i
					elif k == True and i != ":":
						encrypted_message += i
					elif k == False:
						prefix += i
				print(prefix + " " + my_decode(encrypted_message))

				time.sleep(0.2)
		except:
			pass
host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.43.16", 9999)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Name: ")

	rT = threading.Thread(target = receving, args = ("RecvThread",s))
	rT.start()

	while shutdown == False:
	if join == False:
		s.sendto(("[" + alias + "] => join chat ").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input()
			secret = my_encode(message)
			message = secret

			if message != "":
				s.sendto(("[" + alias + "] ::" + message).encode("utf-8"),server)

			time.sleep(0.2)
		except:
			s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()
