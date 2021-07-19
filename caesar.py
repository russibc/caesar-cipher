class Caesar:
    
    def caesar(cleartext, key, alphabet, cipher):
        result = ""
        cleartext = cleartext.lower()

        if not cipher:
            key = len(alphabet) - key

        for x in cleartext:
            if x not in alphabet:
                result += x
            else:
                i = alphabet.index(x)
                j = (i+key) % len(alphabet)
                result = result+alphabet[j]

        return result
