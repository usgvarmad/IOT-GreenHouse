import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
#print host+ "host name"
s.connect(('192.168.43.46', port))
#s.send("Hello server!")
f = open('cam.jpg','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close()        # Close the socket when done
