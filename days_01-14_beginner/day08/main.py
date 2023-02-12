from art import logo


def caesarCipher(message, shift, cipher_direction):
    n = len(message)
    me = ""
    if cipher_direction == "decode":
        shift *= -1
    for i in range(0, n):
        if message[i].isalpha():
            temp = ord(message[i])
            temp += shift
            if temp > 122:
                temp -= 26
            elif temp < 97:
                temp += 26
            me += chr(temp)
        else:
            me += message[i]
    return me


run = True
while (run):
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    print(f"Your {direction}d result is {caesarCipher(text,shift,direction)}")

    choice = input(
        "Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == 'no':
        run = False
        print("Goodbye.")
