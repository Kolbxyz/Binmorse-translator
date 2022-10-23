MorseData = {
"-----": "0",
".----": "1",
"..---": "2",
"...--": "3",
"....-": "4",
".....": "5",
"-....": "6",
"--...": "7",
"---..": "8",
"----.": "9",
"/": " ",
"-....-": "-",
"..--..": "?",
"-.-.-.": ";",
"---...": ":",
"-..-.": "/",
".----.": "'",
".-": "a",
"-...": "b",
"-.-.": "c",
"-..": "d",
".": "e",
"..-.": "f",
"--.": "g",
"....": "h",
"..": "i",
".---": "j",
"-.-": "k",
".-..": "l",
"--": "m",
"-.": "n",
"---": "o",
".--.": "p",
"--.-": "q",
".-.": "r",
"...": "s",
"-": "t",
"..-": "u",
"...-": "v",
".--": "w",
"-..-": "x",
"-.--": "y",
"--..": "z"
}  
BinaryData = {
"00110000": "0",
"00110001": "1",
"00110010": "2",
"00110011": "3",
"00110100": "4",
"00110101": "5",
"00110110": "6",
"00110111": "7",
"00111000": "8",
"00111001": "9",
"01000001": "A",
"01000010": "B",
"01000011": "C",
"01000100": "D",
"01000101": "E",
"01000110": "F",
"01000111": "G",
"01001000": "H",
"01001001": "I",
"01001010": "J",
"01001011": "K",
"01001100": "L",
"01001101": "M",
"01001110": "N",
"01001111": "O",
"01010000": "P",
"01010001": "Q",
"01010010": "R",
"01010011": "S",
"01010100": "T",
"01010101": "U",
"01010110": "V",
"01010111": "W",
"01011000": "X",
"01011001": "Y",
"01011010": "Z",
"01100001": "a",
"01100010": "b",
"01100011": "c",
"01100100": "d",
"01100101": "e",
"01100110": "f",
"01100111": "g",
"01101000": "h",
"01101001": "i",
"01101010": "j",
"01101011": "k",
"01101100": "l",
"01101101": "m",
"01101110": "n",
"01101111": "o",
"01110000": "p",
"01110001": "q",
"01110010": "r",
"01110011": "s",
"01110100": "t",
"01110101": "u",
"01110110": "v",
"01110111": "w",
"01111000": "x",
"01111001": "y",
"01111010": "z",
"00101110": ".",
"00100111": ",",
"00111010": ":",
"00111011": ";",
"00111111": "?",
"00100001": "!",
"00101100": "'",
"00101000": "(",
"00101001": ")",
"00100000": " "
}  

Debug = False

def FromMorseToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += MorseData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Morse to alphabetic -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

def FromAlphaToMorse():
     TranslatedCode = ""
     Chars=[]
     for char in ToTranslate:
        Chars.append(char)
     for c in range(0, len(Chars)):
         for key in MorseData .keys():
             if MorseData [key] == ToTranslate[c]:
                TranslatedCode += key + " "
                if Debug: print(TranslatedCode, key)
                
     TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
     print("Alphabetic to morse -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")
     
def FromBinaryToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += BinaryData [str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print("Binary to alphabetic -->" + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

def FromAlphaToBinary():
     TranslatedCode = ""
     Chars=[]
     for char in ToTranslate:
        Chars.append(char)
     for c in range(0, len(Chars)):
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
        FromBinaryToAlpha()
    elif Mode == 4:
        FromAlphaToBinary()
    else:
        exit()

exit()
