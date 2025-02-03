print("Hello, world!")

def atbash_encode(text):
    text2 = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text2 += chr(ord(letter) * -1 + 155)
            else:
                text2 += chr(ord(letter) * -1 + 219)
        else:
            text2 += letter
    return text2
    
print(atbash_encode(atbash_encode("Hello, world!")))