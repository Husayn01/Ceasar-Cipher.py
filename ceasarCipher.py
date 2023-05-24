import pyfiglet

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','z']
ceasarCipherArt = pyfiglet.figlet_format("Ceasar Cipher")
print(ceasarCipherArt)

def ceasarCipher(text, shift, cipherDirection):
    cipherText = ""
    for letter in text:
        if letter in alphabets:
            index = alphabets.index(letter)
            if cipherDirection == "encode":
                newIndex = index + int(shift)
            elif cipherDirection == "decode":
                newIndex = index - int(shift)
            newLetter = alphabets[newIndex]
            cipherText += newLetter
        else:
            cipherText += letter
    print(f"The {direction}d text is: {cipherText}")


shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    print("------------------------------------")
    txt = input("Type your message: \n").lower()
    print("------------------------------------")
    shiftNum = int(input("Type the shift number: \n"))
    print("------------------------------------")
    shiftNum = shiftNum % 25
    ceasarCipher(text = txt, shift = shiftNum, cipherDirection = direction)
    print("------------------------------------")
    runAgain = input("Type 'yes' to go again, if not type 'no' \n")
    if runAgain == "no":
        shouldContinue = False
        print("Goodbye")

