from sys import argv

import operator
operations = {
    "add": operator.add,
    "mul": operator.mul,
    "sub": operator.sub,
    "truediv": operator.truediv
}

def calc(operation, a, b): 
    return operations[operation](a, b)

operation = argv[1]
a = float(argv[2])
b = float(argv[3])

try: 
    operations[operation]
except KeyError as e:
    raise Warning('Not-allowed operation: {}'.format(e.args[0]))

print("%.2f" % calc(operation, a, b))