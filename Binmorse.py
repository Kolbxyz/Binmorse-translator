## Libraries
import json
import binascii

## Variables
morseData = json.load(open('morseData.json', "r"))
binaryData = json.load(open('binaryData.json', "r"))

debug = False

## Functions
def fromMorseToAlpha():
    translatedCode = ""
    for c in range(0, len(str.split(toTranslate, " "))):
        translatedCode += morseData [str.split(toTranslate, " ")[c]]
        if debug: print(translatedCode, c)
    print("Translating: \"" + toTranslate + "\" from morse to alphabetic..." + "\n\n" + translatedCode + "\n")

def fromAlphaToMorse():
    translatedCode = ""
    for c in range(0, len([*toTranslate])):
        for key in morseData .keys():
            if morseData [key] == toTranslate[c]:
              translatedCode += key + " "
            if debug: print(translatedCode, key)            
    translatedCode = translatedCode[0:len(translatedCode)-1]
    print("Translating: \"" + toTranslate + "\" from alphabetic to morse..." + "\n\n" + translatedCode + "\n")
     
def fromBinaryToAlpha():
    translatedCode = ""
    for c in range(0, len(str.split(toTranslate, " "))):
        translatedCode += binaryData [str.split(toTranslate, " ")[c]]
        if debug: print(translatedCode, c)
    print("Translating: \"" + toTranslate + "\" from binary to alphabetic..." + "\n\n" + translatedCode + "\n")

def fromAlphaToBinary():
    translatedCode = ""
    for c in range(0, len([*toTranslate])):
        for key in binaryData .keys():
            if binaryData [key] == toTranslate[c]:
               translatedCode += key + " "
               if debug: print(translatedCode, key)
                
    translatedCode = translatedCode[0:len(translatedCode)-1]
    print("Translating: \"" + toTranslate + "\" from alphabetic to binary..." + "\n\n" + translatedCode + "\n")

def fromHexToAlpha():
    translatedCode = str(binascii.unhexlify(toTranslate.encode('utf-8')))
    translatedCode = translatedCode.replace("b'","")
    translatedCode = translatedCode.replace("'","")
    print("Translating: \"" + toTranslate + "\" from hex to alphabetic..." + "\n\n" + translatedCode + "\n")

def fromAlphaToHex():
    translatedCode = str(binascii.hexlify(toTranslate.encode('utf-8')))
    translatedCode = translatedCode.replace("b'","")
    translatedCode = translatedCode.replace("'","")
    print("Translating: \"" + toTranslate + "\" from alphabetic to hex..." + "\n\n" + translatedCode + "\n")

## Connectors
print("~~~~~~~~ Welcome to BINMORSE translator! ~~~~~~~~")

while True:
    mode = int(input("1: Morse --> Alphabetic\n2: Alphabetic --> Morse\n3: Binary --> Alphabetic\n4: Alphabetic --> Binary\n5: Hex --> Alphabetic\n6: Alphabetic --> Hex\n\nEnter mode's number:"))
    print("Selected mode: " + (mode == 1 and "Morse to alphabetic" or mode == 2 and "Alphabetic to morse" or mode == 3 and "Binary to Alphabetic" or mode == 4 and "Alphabetic to Binary" or mode == 5 and "Alphabetic to Hex" or mode == 6 and "Hex to Alphabetic" ) + " (" + str(mode) + ")")

    toTranslate = str.lower(str(input("\nString to translate: ")))
    translatedCode = ""
    if mode == 1:
        fromMorseToAlpha()
    elif mode == 2:
        fromAlphaToMorse()
    elif mode == 3:
        fromBinaryToAlpha()
    elif mode == 4:
        fromAlphaToBinary()
    elif mode == 5:
        fromHexToAlpha()
    elif mode == 6:
        fromAlphaToHex()
    else:
        exit()

    print("~~~~~~~~ Thanks for using BINMORSE translator! ~~~~~~~~")
