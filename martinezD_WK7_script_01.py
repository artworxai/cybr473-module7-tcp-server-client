"""
Dana Willis Martinez
October 18, 2026
CYBR 473 - Violent Python
Module 7 Assignment
"""

import socket
import hashlib
import sys

print("Server Starting up\n")

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localHost = socket.gethostname()
    localPort = 5555
    
    serverSocket.bind((localHost, localPort))
    serverSocket.listen(1)
    print(f"Server listening on {localHost}:{localPort}...\nWaiting for Connection Request")
    
    conn, client = serverSocket.accept()
    print(f"Connection Received from Client: {client}")
    
    while True:
        # Receive data from client
        buffer = conn.recv(2048)
        if not buffer:
            break
            
        print(f"Received message bytes: {buffer}")
        
        # Check if client wants to exit
        if b'exit' in buffer.lower():
            print("Server Terminated by User Request.")
            break
            
        # Create MD5 Hash of the message
        message_str = buffer.decode('utf-8').strip()
        md5_digest = hashlib.md5(message_str.encode('utf-8')).hexdigest()
        
        print(f"Generated MD5 Digest: {md5_digest}")
        
        # Send the MD5 digest back to the client
        conn.sendall(bytes(md5_digest, "utf-8"))

    conn.close()
    serverSocket.close()

except Exception as err:
    sys.exit(str(err))