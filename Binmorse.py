## Libraries
import json
import binascii
import base64

## Variables
morseData = json.load(open('morseData.json', "r"))
binaryData = json.load(open('binaryData.json', "r"))
modesData = json.load(open('modes.json', "r"))

debug = False

## Functions
def displayModesList():
    modeList = ""
    for n in range(1,len(modesData)+1):
        modeList  += str(n) + ") " + modesData[str(n)] + "\n"
    return modeList


def fromMorseToAlpha(Input):
    Input = str.lower(Input)
    translatedCode = ""
    for c in range(0, len(str.split(Input, " "))):
        translatedCode += morseData [str.split(Input, " ")[c]]
        if debug: print(translatedCode, c)
    return  "Translating: \"" + input + "\" from morse to alphabetic..." + "\n\n" + translatedCode + "\n"


def fromAlphaToMorse(Input):
    Input = str.lower(Input)
    translatedCode = ""
    for c in range(0, len([*input])):
        for key in morseData .keys():
            if morseData [key] == input[c]:
              translatedCode += key + " "
            if debug: print(translatedCode, key)            
    translatedCode = translatedCode[0:len(translatedCode)-1]
    return "Translating: \"" + input + "\" from alphabetic to morse..." + "\n\n" + translatedCode + "\n"


def fromBinaryToAlpha(Input):
    Input = str.lower(Input)
    translatedCode = ""
    for c in range(0, len(str.split(Input, " "))):
        translatedCode += binaryData [str.split(Input, " ")[c]]
        if debug: print(translatedCode, c)
    return "Translating: \"" + input + "\" from binary to alphabetic..." + "\n\n" + translatedCode + "\n"


def fromAlphaToBinary(Input):
    Input = str.lower(Input)
    translatedCode = ""
    for c in range(0, len([*input])):
        for key in binaryData .keys():
            if binaryData [key] == input[c]:
               translatedCode += key + " "
               if debug: print(translatedCode, key)
                
    translatedCode = translatedCode[0:len(translatedCode)-1]
    return "Translating: \"" + input + "\" from alphabetic to binary..." + "\n\n" + translatedCode + "\n"


def fromHexToAlpha(Input):
    translatedCode = str(binascii.unhexlify(Input.encode('utf-8')))
    translatedCode = translatedCode.replace("b'","")
    translatedCode = translatedCode.replace("'","")
    return "Translating: \"" + input + "\" from hex to alphabetic..." + "\n\n" + translatedCode + "\n"


def fromAlphaToHex(Input):
    translatedCode = str(binascii.hexlify(Input.encode('utf-8')))
    translatedCode = translatedCode.replace("b'","")
    translatedCode = translatedCode.replace("'","")
    return  "Translating: \"" + input + "\" from alphabetic to hex..." + "\n\n" + translatedCode + "\n"


def fromBaseToAlpha(Input):
    subMode = str(input("Which sub mode would you like to use? (b16; a85; b32; b64; b85): "))
    translatedCode = ""

    if subMode == "b16": translatedCode = base64.b16decode(Input).decode("ascii")
    if subMode == "a85": translatedCode = base64.a85decode(Input).decode("ascii")
    if subMode == "b32": translatedCode = base64.b32decode(Input).decode("ascii")
    if subMode == "b64": translatedCode = base64.b64decode(Input).decode("ascii")
    if subMode == "b85": translatedCode = base64.b85decode(Input).decode("ascii")

    return "Decoding: \"" + Input + "\" from alphabetic to " + subMode + "..." + "\n\n" + translatedCode + "\n"


def fromAlphaToBase(Input):
    subMode = str(input("Which sub mode would you like to use? (b16; a85; b32; b64; b85): "))
    translatedCode = ""

    if subMode == "b16": translatedCode = base64.b16encode(Input.encode("ascii")).decode("ascii")
    if subMode == "a85": translatedCode = base64.a85encode(Input.encode("ascii")).decode("ascii")
    if subMode == "b32": translatedCode = base64.b32encode(Input.encode("ascii")).decode("ascii")
    if subMode == "b64": translatedCode = base64.b64encode(Input.encode("ascii")).decode("ascii")
    if subMode == "b85": translatedCode = base64.b85encode(Input.encode("ascii")).decode("ascii")

    return "Encoding: \"" + Input + "\" from " + subMode + " to alphabetic..." + "\n\n" + translatedCode + "\n"
    



## Connectors
print("~~~~~~~~ Welcome to BINMORSE translator! ~~~~~~~~\n")

while True:
    mode = int(input(displayModesList()+"\n\nSelect mode's number: "))
    print("Selected mode: " + modesData[str(mode)] + " (" + str(mode) + ")")
    toTranslate = str(input("\nString to translate: "))

    if mode == 1:
        result = fromMorseToAlpha(toTranslate)
    elif mode == 2:
        result = fromAlphaToMorse(toTranslate)
    elif mode == 3:
        result = fromBinaryToAlpha(toTranslate)
    elif mode == 4:
        result = fromAlphaToBinary(toTranslate)
    elif mode == 5:
        result = fromHexToAlpha(toTranslate)
    elif mode == 6:
        result = fromAlphaToHex(toTranslate)
    elif mode == 7:
        result = fromBaseToAlpha(toTranslate)
    elif mode == 8:
        result = fromAlphaToBase(toTranslate)
    elif mode == 0:
        print("This mode doesn't exist!")
        exit()

    print(result)

    print("~~~~~~~~ Thanks for using BINMORSE translator! ~~~~~~~~\n")
