from sys import argv

mycalc = argv[1]
try:
	print(eval(mycalc))
except NameError:
    print("Input error (Name error)")
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("Input error (Syntax error)")


