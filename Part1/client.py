# Import libraries
import socket ,pickle ,errno ,sys ,argparse

class Message:
	From=0
	Msg=0


def Main(): 
	# local host IP '127.0.0.1' 
	host = '127.0.0.1'

	# Defining connection port 
	port = 4400

	
	# connect to server on local computer 
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		s.connect((host,port)) 
	
	except socket.error as e:
		print("Client Error")
		sys.exit(1)
	

	# message object sent to server
	messageobj=Message()
	messagecheck=pickle.dumps(messageobj)
	print("Check msg is",messagecheck)
	messagecheck=pickle.loads(messagecheck)
	print("Unloaded is:",messagecheck)
	message = Message()
	message={"a":1,"b":2}
	message=pickle.dumps(message)
	print("Dump is:",message)

	while True: 

		# message sent to server 
		try:
			s.send(message)
			
		except socket.error as e:
			print("Transmission Error")
			sys.exit(1)

		# message received from server 
		data = s.recv(4096) 
		print("Data raw is:",data)
		#data_unpacked = pickle.loads(data)
		encoding = 'utf-8'
		data_unpacked=data.decode(encoding)
		print("Data received from server",data_unpacked)

		# ask the client whether he wants to continue 
		ans = input('\nDo you want to continue(y/n) :') 
		if ans == 'y': 
			continue
		else: 
			break
	# close the connection 
	s.close() 

if __name__ == '__main__': 
	Main() 

