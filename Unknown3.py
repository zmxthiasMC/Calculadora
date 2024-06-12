fo = open("numeros.txt", "r+")
data = fo.read()
print(fo.tell())
fo.close()
result = ""
numPhoneKeypad = [("2","abc"), 
                ("3","def"), 
                ("4","ghi"), 
                ("5","jkl"), 
                ("6", "mno"), 
                ("7", "pqrs"),
                ("8","tuv"), 
                ("9","wxyz")]
lastChar = " "
iCont = 0
for cNum in data: 
    if cNum is not lastChar:
        if lastChar != ' ' and lastChar != ',' and lastChar != '.' and lastChar != ':' and lastChar != '!' and lastChar != '\n':
            result += numPhoneKeypad[int(lastChar) - 2][1][iCont]
            iCont = 0
        else:
            result += lastChar
    else:
        iCont += 1
    lastChar = cNum

print(result)
