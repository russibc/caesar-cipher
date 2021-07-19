from caesar import Caesar

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cleartext = "hello world"
    key = 3

    print("cleartext:", cleartext)
    ciphertext = Caesar.caesar(cleartext, key, alphabet, True)
    print("encrypted: ", ciphertext)
    print("decrypted: ", Caesar.caesar(ciphertext, key, alphabet, False))

main()