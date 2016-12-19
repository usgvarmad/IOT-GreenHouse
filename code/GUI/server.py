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
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        dataArray = self.data.split(",")
        for x in range (0,13):
            if(x%2 == 0):
                if(dataArray[x] == "temperature"):
                    fd = open('temp.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "humidity"):
                    fd = open('humid.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "light"):
                    fd = open('light.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "sm0"):
                    fd = open('sm0.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "sm1"):
                    fd = open('sm1.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "sm2"):
                    fd = open('sm2.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
                elif(dataArray[x] == "sm3"):
                    fd = open('sm3.csv','a')
                    fd.write(str(counter)+","+dataArray[x+1]+"\n")
                    fd.close()
            #list_of_items_in_line = line.split(",")
            #first_int = int(list_of_items_in_line[0])

        #fd = open('temp.csv','a')
        #fd.write(self.data+"\n")
        #fd.close()

        # send back the control variables
        with open('control.txt', 'r') as f:
            controlVars = f.readline()
        print controlVars
        self.request.sendall(controlVars)
        counter += 5

if __name__ == "__main__":
    PORT = 9999 #change this to whatever port you want

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

    data_path = "temp.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('temp.csv','w')
        fd.write("")
        fd.close()
    data_path = "humid.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('humid.csv','w')
        fd.write("")
        fd.close()
    data_path = "light.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('light.csv','w')
        fd.write("")
        fd.close()
    data_path = "sm0.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('sm0.csv','w')
        fd.write("")
        fd.close()
    data_path = "sm1.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('sm1.csv','w')
        fd.write("")
        fd.close()
    data_path = "sm2.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('sm2.csv','w')
        fd.write("")
        fd.close()
    data_path = "sm3.csv"
    if(os.path.exists(data_path) and os.path.getsize(data_path) > 0):
        fd = open('sm3.csv','w')
        fd.write("")
        fd.close()

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
