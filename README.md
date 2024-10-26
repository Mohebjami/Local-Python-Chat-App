# Python Chat Application

This is a simple chat application built in Python, featuring both a Command Line Interface (CLI) and a Graphical User Interface (GUI). The application allows two users (a server and a client) to communicate over a local network using sockets.


## Features

- **CLI Version**: A simple text-based chat interface.
- **GUI Version**: A user-friendly graphical interface using `tkinter`.
- Real-time messaging between server and client.
- Basic error handling for connection issues.

## Directory Structure
    /python-chat-app
    ├── CLI
    │   ├── server.py      # Server implementation for CLI
    │   └── client.py      # Client implementation for CLI
    └── GUI
    ├── ├── ServerGUI.py   # Server implementation with GUI
    └── └── ClientGUI.py   # Client implementation with GUI

## Requirements

    - Python 3.x
    - `tkinter` (for GUI version)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-chat-app.git
   cd python-chat-app

2. Install python-tk
# For GUI version, make sure tkinter is installed (usually comes with Python)
# If using Homebrew on macOS, ensure to install tkinter support
brew install python-tk

 ## --------------------------------------

## Running the Application
    For used CLI version:

        cd CLI
        python server.py

        cd CLI
        python client.py

    For used GUI version:
        cd GUI
        python ServerGUI.py

        cd GUI
        python ClientGUI.py

## Good Luck 😎👍🏻