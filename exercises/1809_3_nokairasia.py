n = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
x = 0

for i in range(12):
    for j in range(n[i]):
        D = j+1
        if D % 2 == 1:
            x = x+1
print(x)
