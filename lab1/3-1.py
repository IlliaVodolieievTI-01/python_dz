from sys import argv

mystr = argv[1]

sign = "+-"

def myfuncion(index, str):
    if str[index] in sign and str[index + 1] in sign:
        return False
    elif str[index] not in "+-0123456789":
        return False
    elif str[len(str)-1] in sign:
        return False
    elif index == len(str)-1:
        return True
    else:
        return myfuncion(index + 1, str)

if mystr:
    if myfuncion(0, mystr):
        print("(True,", eval(mystr), ")")
    else:
        print("(False, None)")