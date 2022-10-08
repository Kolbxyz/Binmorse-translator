import json
Database = json.load(open('Database.json', "r"))

Debug = False

def TranslateToAlpha():
    TranslatedCode = ""
    for c in range(0, len(str.split(ToTranslate, " "))):
        TranslatedCode += Database[str.split(ToTranslate, " ")[c]]
        if Debug: print(TranslatedCode, c)
    print((Mode == 1 and "Morse to alphabetic -->" or "Alphabetic to morse -->") + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

def TranslateToMorse():
     TranslatedCode = ""
     for c in range(0, len([*ToTranslate])):
         for key in Database.keys():
             if Database[key] == ToTranslate[c]:
                TranslatedCode += key + " "
                if Debug: print(TranslatedCode, key)
                
     TranslatedCode = TranslatedCode[0:len(TranslatedCode)-1]
     print((Mode == 1 and "Morse to alphabetic -->" or "Alphabetic to morse -->") + "\n(" + ToTranslate + ")\n" + TranslatedCode + "\n")

while True:
    Mode = int(input("1: Morse --> Alphabetic\n2: Alphabetic --> Morse\n\n"))
    print("Selected mode: " + (Mode == 1 and "Morse to alphabetic" or "Alphabetic to morse"))

    ToTranslate = str.lower(str(input("\nString to translate: ")))
    TranslatedCode = ""
    if Mode == 1:
        TranslateToAlpha()
    elif Mode == 2:
        TranslateToMorse()
    else:
        exit()

exit()
