import socket, select,zlib
def send_to_all (sock, message):
	for socket in connected_list:
		if socket != server_socket and socket != sock :
			try :
				socket.send(message)
			except :
				socket.close()
				connected_list.remove(socket)

if __name__ == "__main__":
	name=""
	record={}

	connected_list = []
	buffer = 4096
	port = 5001

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind(("localhost", port))
	server_socket.listen(10)
	connected_list.append(server_socket)

	print "\33[32m \t\t\t\t Welcome to Chat Room Server\33[0m" 

	while 1:
		rList,wList,error_sockets = select.select(connected_list,[],[])

		for sock in rList:
			if sock == server_socket:
				sockfd, addr = server_socket.accept()
				name=sockfd.recv(buffer)
				connected_list.append(sockfd)
				record[addr]=""
				if name in record.values():
					sockfd.send("\r\33[31m\33[1m Username already taken!\n\33[0m")
					del record[addr]
					connected_list.remove(sockfd)
					sockfd.close()
					continue
				else:
					record[addr]=name
					print "Client (%s, %s) connected" % addr," [",record[addr],"]"
					sockfd.send("\33[32m\r\33[1m Welcome to chat room. Enter 'exit' anytime to exit\n\33[0m")
					send_to_all(sockfd, "\33[32m\33[1m\r "+name+" joined the conversation \n\33[0m")

			else:
				try:
					data1 = sock.recv(buffer)
					data=data1[:data1.index("\n")]
					i,p=sock.getpeername()
					if data == "exit":
						msg="\r\33[1m"+"\33[31m "+record[(i,p)]+" left the conversation \33[0m\n"
						send_to_all(sock,msg)
						print "Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]"
						del record[(i,p)]
						connected_list.remove(sock)
						sock.close()
						continue

					else:
						msg="\r\33[1m"+"\33[35m "+record[(i,p)]+": "+"\33[0m"+data+"\n"
						send_to_all(sock,msg)
            
				except:
					(i,p)=sock.getpeername()
					send_to_all(sock, "\r\33[31m \33[1m"+record[(i,p)]+" left the conversation unexpectedly\33[0m\n")
					print "Client (%s, %s) is offline (error)" % (i,p)," [",record[(i,p)],"]\n"
					del record[(i,p)]
					connected_list.remove(sock)
					sock.close()
					continue

	server_socket.close()


