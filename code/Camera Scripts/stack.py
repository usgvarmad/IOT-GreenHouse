#import socket               # Import socket module

#s = socket.socket()         # Create a socket object
#host = '172.20.10.4' # Get local machine name
#port = 12345                 # Reserve a port for your service.
#s.bind((host, port))        # Bind to the port
#f = open('cam.jpg','wb')
#s.listen(5)                 # Now wait for client connection.
#while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print 'Got connection from', addr
#    print "Receiving..."
#    l = c.recv(1024)
#    while (l):
#        print "Receiving..."
#        f.write(l)
#        l = c.recv(1024)
#    f.close()
#    print "Done Receiving"
#    c.send('Thank you for connecting')
#    c.close()                # Close the connection



import SocketServer
import socket
import os
# Boilerplate code from:
# https://docs.python.org/2/library/socketserver.html

counter = 0
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        global counter
        # self.request is the TCP socket connected to the client
        if(counter == 0):
            f = open('plot1.jpg','wb')
        elif(counter==1):
            f = open('plot2.jpg','wb')
        elif(counter==2):
            f = open('plot3.jpg','wb')
        elif(counter==3):
            f = open('plot4.jpg','wb')
        self.data = self.request.recv(1024)
        while(self.data):
            f.write(self.data)
            self.data = self.request.recv(1024)
        f.close()



        #self.request.sendall(controlVars)
        counter += 1
        if (counter == 4):
            counter = 0

if __name__ == "__main__":
    PORT = 12345 #change this to whatever port you want

    # get local IP in platform independent manner
    # must be connected to the internet
    # this solution to get the local IP is from:
    # http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    try:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.connect(("google.com",80))
        HOST = str(mySocket.getsockname()[0])
        mySocket.close()
    except:
        print "You gotta be connected to the internet!!"
        exit()
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
