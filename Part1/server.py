#importing libraries
import socket ,pickle ,errno ,sys ,argparse

# importing thread modules 
from _thread import *
import threading 

#Creating a thread lock object
lock = threading.Lock() 

# thread function 
def threaded(c): 
	while True: 

		# data received from client 
		data = c.recv(4096) 
		if not data: 
			print('Bye') 
			
			# lock released on exit 
			lock.release() 
			break

		print("Data raw is:",data)
		data_unpacked = pickle.loads(data)
		#encoding = 'utf-8'
		#data_unpacked=data.decode(encoding)
		print("Data received from client is",data_unpacked)
		# Accessing message
		#print('Message received is',data_unpacked.message)

		# sending back data object
		try:
			c.send(data) 	
		except socket.error as e:
			print("Transmission Error")
			sys.exit(1)

	# connection closed 
	c.close() 


def Main(): 
	host = "" 

    #port set to 4400
	port = 4400
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.bind((host, port)) 
		print("Socket binded to port", port) 

	except socket.error as e:
		print("Server Error")
		sys.exit(1)

	# put the socket into listening mode 
	s.listen(5) 
	print("Socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		
		c, addr = s.accept() 

		# lock acquired by client 
		lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 

