from itertools import permutations

W = int(input())
n = list(map(int, input().split()))

maxSuma = 0
l = len(n)

for i in permutations(n, l):
    suma = 0
    for j in range(l):
        if W >= suma + i[j]:
            suma += i[j]
    if maxSuma < suma:
        maxSuma = suma

print(maxSuma)