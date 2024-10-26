import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Function to handle receiving messages from the client
def handle_client(client_socket, chat_window):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.config(state=tk.NORMAL)
                chat_window.insert(tk.END, f"Client: {message}\n")
                chat_window.config(state=tk.DISABLED)
                chat_window.see(tk.END)
            else:
                break
        except:
            break

def send_message(client_socket, input_field, chat_window):
    message = input_field.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {message}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)
        input_field.delete(0, tk.END)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))  # Bind the server to localhost and port 5555
    server.listen(1)
    print("Server started, waiting for connections...")

    client_socket, client_address = server.accept()
    print(f"Client connected from {client_address}")

    # Setup GUI
    root = tk.Tk()
    root.title("Server Chat")

    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
    chat_window.pack(padx=10, pady=10)

    input_field = tk.Entry(root, width=50)
    input_field.pack(padx=10, pady=10)

    send_button = tk.Button(root, text="Send", command=lambda: send_message(client_socket, input_field, chat_window))
    send_button.pack()

    # Start receiving messages in a separate thread
    receive_thread = threading.Thread(target=handle_client, args=(client_socket, chat_window))
    receive_thread.start()

    root.mainloop()

start_server()