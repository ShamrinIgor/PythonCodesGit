import time, socket

host = socket.gethostbyname(socket.gethostname())
port = 9999
#print (help(socket))
clients = []

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((host, port))

quit = False
print("[Server started]")

while not quit:
    try:
        data, addr = soc.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime +"]/",end = "")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                soc.sendto(data,client)

    except:
        print("\n[Server Stopped]")
        quit = True

soc.close()
