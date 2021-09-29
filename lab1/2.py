from os import error
import sys 
import operator

def calc(str): 
    try:
        think = str[1]
        if think == 'add':return operator.add(int(str[2]), int(str[3]))
        elif think == 'mull':return operator.mull(int(str[2]), int(str[3]))
        elif think == 'divide':return operator.truediv(int(str[2]), int(str[3]))
        elif think == 'sub':return operator.sub(int(str[2]), int(str[3]))
    except:
        return False

print(calc(sys.argv[:]))