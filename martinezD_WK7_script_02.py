"""
Dana Willis Martinez
October 18, 2026
CYBR 473 - Violent Python
Module 7 Assignment 2
"""

import socket
import sys

print("Client Application")
print("Establish a connection to a server available on PORT 5555")

PORT = 5555

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localHost = socket.gethostname()
    
    print(f"\nAttempting Connection to: {localHost}:{PORT}")
    clientSocket.connect((localHost, PORT))
    print("Socket Connected ...\n")
    
    # Define 10 differing messages to send to the server
    messages = [
        "Hello Server",
        "Black Hat Python",
        "TCP Socket Programming",
        "Cybersecurity Module 7",
        "Data Integrity Check",
        "MD5 Hashing Test",
        "Python Network Script",
        "Secure Communications",
        "Packet Analysis",
        "Final Message Exit"
    ]
    
    for i, msg in enumerate(messages, 1):
        print(f"--- Message {i} ---")
        print(f"Sending: {msg}")
        
        # Send message bytes to server
        messageBytes = bytes(msg, "utf-8")
        clientSocket.sendall(messageBytes)
        
        # Receive the MD5 digest response from the server
        response_buffer = clientSocket.recv(2048)
        print(f"Received MD5 Digest from Server: {response_buffer.decode('utf-8')}\n")
        
    # Close socket connection after sending all 10 messages
    clientSocket.close()
    print("All 10 messages sent and responses received. Client shutting down.")

except Exception as err:
    sys.exit(str(err))