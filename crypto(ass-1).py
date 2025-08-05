def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


message = "hello"
shift = 3

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Org:", message)
print("Enc:", encrypted)
print("Dec:", decrypted)