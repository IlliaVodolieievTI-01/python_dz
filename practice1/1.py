import os
import random
import timeit

with open('file.txt', 'a') as f:
	while os.path.getsize('file.txt') < 5000000:
		f.write(str(random.randint(0, 100)))
k = """
with open('file.txt', 'r') as f1:
	lines = f1.readlines()
	s = 0
	for line in lines:
		if line.strip().isdigit():
			s += int(line.strip())
"""
print(timeit.timeit(k, number=1))

k = """
with open('file.txt', 'r') as f2:
	s = 0
	for line in f2:
		if line.strip().isdigit():
			s += int(line.strip())
"""
print(timeit.timeit(k, number=1))

k = """
with open('file.txt', 'r') as f3:
	l = (in line.strip()) for line in f3 if line.strip().isdigit())
	s = sum(l)
"""
print(timeit.timeit(k, number=1))