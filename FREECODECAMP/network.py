# writing a web browser socket
'''import socket
mysock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) #going across the internet
mysock.connect( ('data.pr4e.org', 80) ) #makig a call
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #the GET request to retrieve info
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()'''

# writing a web browser using urllib
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# reading web pages using urllib
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())