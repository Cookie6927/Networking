import socket

# Define the server's IP address and port number
server_ip = "127.0.0.1"
server_port = 8000

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server's IP address and port number
server_socket.bind((server_ip, server_port))
print("Server listening on {}:{}".format(server_ip, server_port))

# Listen for packets and send a response
while True:
    try:
        # Receive a packet and print its contents
        data, address = server_socket.recvfrom(1024)
        print("Received packet from {}: {}".format(address, data))

        # Send a response packet
        response = "Hello, client!".encode()
        server_socket.sendto(response, address)
        print("Sent response to {}: {}".format(address, response))
    except:
        # Handle any exceptions that occur while running the server
        print("An exception occurred while running the server")
