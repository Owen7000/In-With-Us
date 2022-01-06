import time, os, socket, threading

def start_server():
    global address, server_socket
    address = ('', 54545)
    print("Setting up a server socket")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time.sleep(0.25)
    print("Configuring server socket")
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    time.sleep(0.25)
    print("Binding socket")
    server_socket.bind(address)
    time.sleep(0.25)
    os.system("cls")
    print("Server setup complete")
    print("Your IP Address is:" + socket.gethostbyname(socket.gethostname()))
