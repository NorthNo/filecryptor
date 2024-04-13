from colorama import Fore
import sys
import os

def print_message(msg_type, message):
    if msg_type == "w":
        print(Fore.YELLOW + "[Warning] " + Fore.WHITE + message)
    elif msg_type == "i":
        print(Fore.LIGHTBLACK_EX + "[INFO] " + Fore.WHITE + message)
    elif msg_type == "s":
        print(Fore.GREEN + "[SUCCESSFULL] " + Fore.WHITE + message)
    elif msg_type == "e":
        print(Fore.RED + "[ERROR] " + Fore.WHITE + message)

def encrypt_file(path, key):
    try:
        print_message("i", "File Path: " + str(path))
        print_message("i", "Encryption Key: " + str(key))
        
        with open(path, 'rb') as fin:
            file = bytearray(fin.read())

        for i, value in enumerate(file):
            file[i] = value ^ key

        with open(path, 'wb') as fout:
            fout.write(file)

        print_message("s", "Encryption Done...")
        
    except Exception as e:
        print_message("e", 'Error caught: ' + str(e))

def decrypt_file(path, key):
    try:
        print_message("i", "File Path: " + str(path))
        print_message("i", "Decryption Key: " + str(key))
        
        with open(path, 'rb') as fin:
            file = bytearray(fin.read())

        for i, value in enumerate(file):
            file[i] = value ^ key

        with open(path, 'wb') as fout:
            fout.write(file)

        print_message("s", "Decryption Done...")

    except Exception as e:
        print_message("e", "Error caught: " + str(e))

if len(sys.argv) == 4:
    file_path = sys.argv[1]
    operation = sys.argv[2]
    key = int(sys.argv[3])
    
    if os.path.exists(file_path):
        if operation == "-d":
            decrypt_file(file_path, key)
        elif operation == "-e":
            encrypt_file(file_path, key)
        else:
            print_message("w", "Invalid operation. Please use '-d' for decryption or '-e' for encryption.")
    else:
        print_message("w", "File not found.")
else:
    print_message("w", "imageCryptographer.py target_file_path operation(-d or -e) key(integer)")
