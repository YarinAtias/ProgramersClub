from binary_conversions import decimal_to_binary, binary_to_decimal

XOR_NUMBER = 5
def xor_encryption(file):
    with open(file, 'r') as f:
        file_as_lines = f.readlines()
    encrypted_file = ""
    for line in file_as_lines:
        for letter in line:
            if letter == " ":
                encrypted_file = encrypted_file + ""
            elif letter == "\n":
                encrypted_file = encrypted_file + "\n"
                continue
            else:
                letter_as_ascii = ord(letter)
                letter_after_xor_encryption = letter_as_ascii ^ XOR_NUMBER
                encrypted_letter = decimal_to_binary(letter_after_xor_encryption)
                encrypted_file = encrypted_file + str(encrypted_letter)
            encrypted_file = encrypted_file + " "
    encrypted_file = encrypted_file[0:-1]
    with open(file, 'w') as f:
        f.write(encrypted_file)
    print("File encrypted.")



def xor_decryption(encrypted_file_param, decrypted_file_param):
    with open(encrypted_file_param, 'r') as f:
        file_as_lines = " ".join(f.readlines())
    file_as_lines = file_as_lines.split(" ")
    decrypted_file = ""
    for element in file_as_lines:
        if element == "": decrypted_file = decrypted_file + " "
        elif element == "\n": decrypted_file = decrypted_file + "\n"
        else:
            encrypted_letter_to_decimal = binary_to_decimal(element)
            decrypted_letter_as_decimal = encrypted_letter_to_decimal ^ XOR_NUMBER
            decrypted_letter = chr(decrypted_letter_as_decimal)
            decrypted_file = decrypted_file + decrypted_letter
    with open(decrypted_file_param, 'w') as f:
        f.write(decrypted_file)
    print("File decrypted.")



file_to_encrypt = "encrypted_file"
xor_encryption(file_to_encrypt)
xor_decryption(file_to_encrypt, "decrypted_file")
