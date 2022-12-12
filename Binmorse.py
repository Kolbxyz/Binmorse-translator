## Libraries
import json

## Variables
MorseData = json.load(open('MorseData.json', "r"))
BinaryData = json.load(open('BinaryData.json', "r"))

Debug = False

## Functions
def FromMorseToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += MorseData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Translating: \"" + ToTranslate + "\" from morse to alphabetic..." + "\n\n" + TranslatedCode + "\n")

def FromAlphaToMorse():
    TranslatedCode = ""
    for c in range(0, len([*ToTranslate])):
        for key in MorseData .keys():
            if MorseData [key] == ToTranslate[c]:
              TranslatedCode += key + " "
            if Debug: print(TranslatedCode, key)            
    TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
    print("Translating: \"" + ToTranslate + "\" from alphabetic to morse..." + "\n\n" + TranslatedCode + "\n")
     
def FromBinaryToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += BinaryData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Translating: \"" + ToTranslate + "\" from binary to alphabetic..." + "\n\n" + TranslatedCode + "\n")

def FromAlphaToBinary():
    TranslatedCode = ""
    for c in range(0, len([*ToTranslate])):
        for key in BinaryData .keys():
            if BinaryData [key] == ToTranslate[c]:
               TranslatedCode += key + " "
               if Debug: print(TranslatedCode, key)
                
    TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
    print("Translating: \"" + ToTranslate + "\" from alphabetic to binary..." + "\n\n" + TranslatedCode + "\n")

## Connectors
print("~~~~~~~~ Welcome to BINMORSE translator! ~~~~~~~~")

while True:
    Mode = int(input("1: Morse --> Alphabetic\n2: Alphabetic --> Morse\n3: Binary --> Alphabetic\n4: Alphabetic --> Binary\n\nEnter mode's number:"))
    print("Selected mode: " + (Mode == 1 and "Morse to alphabetic" or Mode == 2 and "Alphabetic to morse" or Mode == 3 and "Binary to Alphabetic" or "Alphabetic to Binary") + " (" + str(Mode) + ")")

    ToTranslate = str.lower(str(input("\nString to translate: ")))
    TranslatedCode = ""
    if Mode == 1:
        FromMorseToAlpha()
    elif Mode == 2:
        FromAlphaToMorse()
    elif Mode == 3:
        FromBinaryToAlpha()
    elif Mode == 4:
        FromAlphaToBinary()
    else:
        exit()

    print("~~~~~~~~ Thanks for using BINMORSE translator! ~~~~~~~~")
