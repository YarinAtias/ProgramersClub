import os.path
import socket
import shutil

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
END_SESSION_MESSAGE = "-999"
FAILED_FINDING_MESSAGE = "This file is not available, try again please."

IP = "127.0.0.1"
PORT = 8820

client_socket.connect((IP, PORT))
run_client = True
FIRST_TIME_ASKED = False
user_choice = '0'

def download_files():
    global run_client
    global FIRST_TIME_ASKED

    received_data = client_socket.recv(1024).decode()
    if not FIRST_TIME_ASKED:
        print(received_data)
        data_to_send = input("Enter the file you want to get: ").encode()
        client_socket.send(data_to_send)
        FIRST_TIME_ASKED = True
    else:
        if received_data == END_SESSION_MESSAGE:
            print("Goodbye.")
            run_client = False
        elif received_data == FAILED_FINDING_MESSAGE:
            print(received_data)
            data_to_send = input("Enter the file you want to get: ").encode()
            client_socket.send(data_to_send)
        else:
            print(received_data)
            run_client = False


def upload_files():
    global run_client
    file_to_upload = input("Enter file path (Enter -999 to end the session): ")
    if file_to_upload == END_SESSION_MESSAGE:
        print("Goodbye.")
        client_socket.send(END_SESSION_MESSAGE.encode())
        run_client = False
    else:
        if os.path.exists(file_to_upload) and os.path.isfile(file_to_upload):
            file_name = os.path.basename(file_to_upload)
            if file_name in os.listdir("saved_files"):
                print("This file is already in the directory. Try again please.")
            else:
                shutil.copy(file_to_upload, "saved_files")
                print("File has uploaded!")
                client_socket.send(END_SESSION_MESSAGE.encode())
                run_client = False
        else:
            print("File did not found. Please try again.")


def user_choice_func():
    user_choice_text = client_socket.recv(1024).decode()
    print(user_choice_text)
    global user_choice
    user_choice = input()

def main():
    user_choice_func()
    global user_choice
    ALREADY_CHOOSE = False

    while run_client:
        if user_choice == '1':
            if not ALREADY_CHOOSE:
                client_socket.send('1'.encode())
                ALREADY_CHOOSE = True
            else:
                download_files()
        elif user_choice == '2':
            if not ALREADY_CHOOSE:
                client_socket.send('2'.encode())
                ALREADY_CHOOSE = True
            else:
                upload_files()
        else:
            print("Choice wasn't recognized. Please try again")
            user_choice = input()


if __name__ == '__main__':
    main()
client_socket.close()