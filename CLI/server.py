import socket
import threading

# Function to handle receiving messages from the client
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client: {message}")
            else:
                break
        except:
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))  # Bind the server to localhost and port 5555
    server.listen(1)
    print("Server started, waiting for connections...")

    client_socket, client_address = server.accept()
    print(f"Client connected from {client_address}")

    # Start a new thread for receiving messages
    receive_thread = threading.Thread(target=handle_client, args=(client_socket,))
    receive_thread.start()

    # Loop to send messages from the server to the client
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

start_server()