str1 = input()
str2 = input()
n = len(str2)
m = len(str1)

for i in range(n-m+1):
    check = 1
    for j in range(m):
        if str1[j] == str2[i+j]:
            check = -1
            break
    if check == 1:
        break

print(check)
