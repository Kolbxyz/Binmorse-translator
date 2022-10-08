import json
MorseData = json.load(open('MorseData.json', "r"))
BinaryData = json.load(open('BinaryData.json', "r"))

Debug = False

def FromMorseToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += MorseData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Binary to alphabetic -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

def FromAlphaToMorse():
     TranslatedCode = ""
     for c in range(0, len([*ToTranslate])):
         for key in MorseData .keys():
             if MorseData [key] == ToTranslate[c]:
                TranslatedCode += key + " "
                if Debug: print(TranslatedCode, key)
                
     TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
     print("Alphabetic to binary -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")
     
def FromBinaryToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += BinaryData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Binary to alphabetic -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

def FromAlphaToBinary():
     TranslatedCode = ""
     for c in range(0, len([*ToTranslate])):
         for key in BinaryData .keys():
             if BinaryData [key] == ToTranslate[c]:
                TranslatedCode += key + " "
                if Debug: print(TranslatedCode, key)
                
     TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
     print("Alphabetic to binary -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

while True:
    Mode = int(input("1: Morse --> Alphabetic\n2: Alphabetic --> Morse\n3: Binary --> Alphabetic\n4: Alphabetic --> Binary\n\n"))
    print("Selected mode: " + (Mode == 1 and "Morse to alphabetic" or Mode == 2 and "Alphabetic to morse" or Mode == 3 and "Binary to Alphabetic" or "Alphabetic to Binary"))

    ToTranslate = str.lower(str(input("\nString to translate: ")))
    TranslatedCode = ""
    if Mode == 1:
        FromMorseToAlpha()
    elif Mode == 2:
        FromAlphaToMorse()
    elif Mode == 3:
        From BinaryToAlpha()
    elif Mode == 4:
        FromAlphaToBinary()
    else:
        exit()

exit()
