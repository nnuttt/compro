taxrate = 0.07
standardD = 3000
Dperdependent = 1500

Gincome = float(input("input gross income :"))
NumberofD = float(input("input number of dependents :"))

netincome = Gincome-standardD-(Dperdependent*NumberofD)
incometax = taxrate*netincome

print("your tax is", round(incometax, 2))