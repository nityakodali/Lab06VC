def encoder(x):
    password = ""
    for char in x:
        digit = int(char) + 10
        digit = (digit + 3) % 10
        password += str(digit)
    return password


def decoder(x):
    password = ""
    for char in x:
        digit = int(char) + 10
        digit = (digit - 3) % 10
        password += str(digit)
    return password


def main():
    password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter you password to encode: ")
            password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decoder(password)}.")
        elif option == 3:
            break


if __name__ == "__main__":
    main()
