from socket import *
serverPort = 1473
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))
    
    sentence = connectionSocket.recv(1024).decode()
    line = sentence.splitlines()[0]
    method, path, _ = line.split()
    print(path)
    if path == '/' or path == '/index.html' or path == '/main_en.html' or path == '/en':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj/main_en.html", "rb")
        connectionSocket.send(testF.read())
        
    elif path == '/ar' :
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj/main_ar.html", "rb")
        connectionSocket.send(testF.read())
        
    elif path.endswith('.html') :
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj"+path, "rb")
        connectionSocket.send(testF.read())
        
    elif path.endswith('.css') :
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/css \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj"+path, "rb")
        connectionSocket.send(testF.read())
    
    elif path.endswith('.png') :
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/png \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj"+path,"rb")
        connectionSocket.send(testF.read())
        
    elif path.endswith('.jpg') :
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        testF = open("C:/Users/EASY LIFE/OneDrive/Desktop/NetworkProj"+path, "rb")
        connectionSocket.send(testF.read())    
        
        
    connectionSocket.close()
        
    
    
