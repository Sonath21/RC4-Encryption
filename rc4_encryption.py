def KSA(key):
    key_length = len(key)
    S = list(range(256))
    for i in range(256):
        S[i] = i
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, text):
    ascii_key = []
    for character in key:
        ascii_value = ord(character)
        ascii_key.append(ascii_value)
    S = KSA(ascii_key)
    keystream = PRGA(S)
    result = []
    for char in text:
        result.append(chr(ord(char) ^ next(keystream)))  # XOR
    return ''.join(result)


def text_to_binary(text):
    binary_string = ''
    for char in text:
        binary_string += binary_array[char]
    return binary_string


def binary_to_text(binary):
    text = ''
    for i in range(0, len(binary), 5):
        binary_segment = binary[i:i + 5]
        char_code = int(binary_segment, 2)
        character = chr(char_code + 65)
        text += character
    return text


binary_array = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011',
    'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011',
    'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001'
}

key = "HOUSE"
message = "MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE"

message_binary = text_to_binary(message)
encrypted_binary = RC4(key, message_binary)
decrypted_binary = RC4(key, encrypted_binary)
decrypted_message = binary_to_text(decrypted_binary)

print("Original Message:", message)
print("Encrypted Binary:", encrypted_binary)
print("Decrypted Message:", decrypted_message)
