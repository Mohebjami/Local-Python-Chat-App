import socket
import threading

# Function to handle receiving messages from the server
def handle_server(server_socket):
    while True:
        try:
            message = server_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))  # Connect to the server on localhost and port 5555

    # Start a new thread for receiving messages
    receive_thread = threading.Thread(target=handle_server, args=(client,))
    receive_thread.start()

    # Loop to send messages from the client to the server
    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

start_client()