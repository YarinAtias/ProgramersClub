import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "127.0.0.1"
PORT = 8820
FAILED_FINDING_MESSAGE = "This file is not available, try again please."
END_SESSION_MESSAGE = "-999"

server_socket.bind((IP, PORT))
run_server = True
run_client = True
ALREADY_SENT_DIR = False

print("Server is up and running")

def download_files():
    global run_client
    global run_server
    global ALREADY_SENT_DIR

    if not ALREADY_SENT_DIR:
        data_to_send = f"""Files to download\n{chr(10).join(files_directory)}\n(Enter -999 to finish the session)
            """
        ALREADY_SENT_DIR = True
        client_socket.send(data_to_send.encode())
    else:
        data_received = client_socket.recv(1024).decode()
        if data_received == END_SESSION_MESSAGE:
            run_client = False
            run_server = False
            client_socket.send(END_SESSION_MESSAGE.encode())
            client_socket.close()
        else:
            if data_received in files_directory:
                run_client = False
                run_server = False
                client_socket.send(f"Downloading {data_received}...".encode())
            else:
                client_socket.send(FAILED_FINDING_MESSAGE.encode())


def upload_files():
    global run_client
    global run_server
    try:
        message = client_socket.recv(1024).decode()
        if message == END_SESSION_MESSAGE:
            run_client = False
            run_server = False
    except:
        pass

def user_choice_func():
    user_choice_text = "Choose 1 to download files\nChoose 2 to upload a file".encode()
    client_socket.send(user_choice_text)


while run_server:
    server_socket.listen()
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    files_directory = os.listdir("saved_files")
    user_choice_func()
    user_choice = client_socket.recv(1024).decode()
    while run_client:
        if user_choice == '1':
            download_files()
        elif user_choice == '2':
            upload_files()



server_socket.close()
