import socket                   # Import socket module
import time
import sys

fp = open('slog.txt', 'a')

port = 60001                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
#host = socket.gethostname()     # Get local machine name
s.bind(('10.100.0.7', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    fp.write(str(int(time.time() * 1000000)))
    fp.write('\n')
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    #Here it is imperative that you already have a file for transfer.  You can easily create a file of n 
    #bytes using any language and then name it 'mytext.txt' and it will work with this test
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
#        print('Sent ', repr(l))
        l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

