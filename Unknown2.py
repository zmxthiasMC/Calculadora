import sys
if len(sys.argv) == 2:
    codedString = str(sys.argv[1])
    codedString = codedString.replace("%3C", "<")
    codedString = codedString.replace("%3E", ">")
    codedString = codedString.replace("%3D", "=")
    codedString = codedString.replace("%20", " ")
    codedString = codedString.replace("%22", " ' ")
    codedString = codedString.replace("%3A", ":")
    codedString = codedString.replace("%0D", "\n")
    codedString = codedString.replace("%0A", "")
    codedString = codedString.replace("%7B", "{ ")
    codedString = codedString.replace("%7D", "} ")
    codedString = codedString.replace("%28", "( ")
    codedString = codedString.replace("%29", ") ")
    codedString = codedString.replace("%26", "& ")
    codedString = codedString.replace("%2C", ", ")
    print(codedString)
else:
    print("Please, introduce the coded string as argument")


