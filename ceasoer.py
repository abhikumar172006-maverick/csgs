def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(text, shift)
print("Encrypted message:", encrypted)

decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted message:", decrypted)
