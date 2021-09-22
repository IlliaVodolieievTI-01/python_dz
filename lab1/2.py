from sys import argv

import operator
operations = {
    "add": operator.add,
    "mul": operator.mul,
    "sub": operator.sub,
    "truediv": operator.truediv
}

def calc(operation, arg1, arg2): 
    return operations[operation](arg1, arg2)

operation = argv[1]
arg1 = float(argv[2])
arg2 = float(argv[3])

try: 
    operations[operation]
except KeyError as e:
    raise Warning('Not-allowed operation: {}'.format(e.args[0]))

print("%.2f" % calc(operation, arg1, arg2))