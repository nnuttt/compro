firstday = int(input("firstday :"))
DIY = int(input("dayinthisyear :"))
D = firstday
x = 0

for i in range(DIY):
    if D == 2:
        x = x+1
    if D == 7:
        D = 1
    else:
        D = D+1

print(x)
