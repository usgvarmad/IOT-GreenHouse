import socket
from time import sleep

s = socket.socket()         # Create a socket object
port = 12345                # Reserve a port for your service.

# Be sure to change this address!!
address = '172.20.10.4'

s.connect((address, port))

f = open('plot1.jpg','rb')
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

sleep(1)
s = socket.socket()         # Create a socket object
s.connect((address, port))

f = open('plot2.jpg','rb')
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

sleep(1)
s = socket.socket()         # Create a socket object
s.connect((address, port))

f = open('plot3.jpg','rb')
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

sleep(1)
s = socket.socket()         # Create a socket object
s.connect((address, port))

f = open('plot4.jpg','rb')
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