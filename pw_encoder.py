# Krish Kapoor

def encode(pw: str):
    encoded = ""

    for num in pw:
        if (int(num) + 3 >= 10):
            encoded += str((int(num) + 3) % 10)
        else:
            encoded += str(int(num) + 3)

    return encoded

def decode(password):
    decoded_password = ""
    for num in password:
        if (int(num) - 3 < 0):
            decoded_password += str((int(num) - 3) + 10)
        else:
            decoded_password += str(int(num) - 3)
    return decoded_password

if __name__ == "__main__":
    pw = ""

    while (True):
        print("Menu")
        print("-------------")

        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        print("Please enter an option: ", end='')
        option = int(input())

        if option == 1:
            print("Please enter your password to encode: ", end='')
            pw = encode(input())

            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {pw}, and the original password is {decode(pw)}.\n")
        elif option == 3:
            break