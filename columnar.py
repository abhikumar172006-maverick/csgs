def encrypt(text, key):
    text = text.replace(" ", "").upper()
    key_order = sorted(range(len(key)), key=lambda i: key[i])

    result = ""

    for col in key_order:
        for row in range(col, len(text), len(key)):
            result += text[row]

    return result


def decrypt(cipher, key):
    n = len(key)
    rows = (len(cipher) + n - 1) // n
    extra = len(cipher) % n

    col_lengths = [
        rows if extra == 0 or col < extra else rows - 1
        for col in range(n)
    ]

    key_order = sorted(range(n), key=lambda i: key[i])
    columns = [""] * n
    pos = 0

    for col in key_order:
        length = col_lengths[col]
        columns[col] = cipher[pos:pos + length]
        pos += length

    result = ""

    for row in range(rows):
        for col in range(n):
            if row < len(columns[col]):
                result += columns[col][row]

    return result


text = input("Enter message: ")
key = input("Enter key (letters): ").upper()

cipher = encrypt(text, key)
print("Encrypted message:", cipher)

plain = decrypt(cipher, key)
print("Decrypted message:", plain)
