arg1 = input()
operation = input()
arg2 = input()
import operator
operations = {
    '+': operator.add,
    "*": operator.mul,
    '-': operator.sub,
    '/': operator.truediv
    }
    def calc(operation, arg1, arg2)
    	return operations[operation](arg1, arg2)
    print("%.2f" % calc(operation, arg1, arg2))