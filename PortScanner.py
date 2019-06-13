#!/usr/bin/python
import socket 
import sys
#1.the code is making a socket
#2.resolved the IP address and connected to the IP address
#3.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a instance of generic tcp socket

hostname = sys.argv[1] #reads IP adress
lwrPrt = int(sys.argv[2]) #lower port number
hghrPrt = int(sys.argv[3]) #higher port number
IP = socket.gethostbyname(hostname) #connects to the IP adress


def scan(port): #function to scan each port number and test if it connects or not
  
   try:
      tempPort = s.connect((IP,port))
      return True
   except:
      return False
   s.close()

for x in range(lwrPrt,hghrPrt+1):
   
   if scan(x):
      print 'Port ' ,x, ' open'
  
  
