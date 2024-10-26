import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Function to handle receiving messages from the server
def handle_server(server_socket, chat_window):
    while True:
        try:
            message = server_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.config(state=tk.NORMAL)
                chat_window.insert(tk.END, f"Server: {message}\n")
                chat_window.config(state=tk.DISABLED)
                chat_window.see(tk.END)
            else:
                break
        except:
            break

def send_message(server_socket, input_field, chat_window):
    message = input_field.get()
    if message:
        server_socket.send(message.encode('utf-8'))
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {message}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)
        input_field.delete(0, tk.END)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))  # Connect to the server on localhost and port 5555

    # Setup GUI
    root = tk.Tk()
    root.title("Client Chat")

    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
    chat_window.pack(padx=10, pady=10)

    input_field = tk.Entry(root, width=50)
    input_field.pack(padx=10, pady=10)

    send_button = tk.Button(root, text="Send", command=lambda: send_message(client, input_field, chat_window))
    send_button.pack()

    # Start receiving messages in a separate thread
    receive_thread = threading.Thread(target=handle_server, args=(client, chat_window))
    receive_thread.start()

    root.mainloop()

start_client()