isvac = input("Is vaccinated(y/n) :")
Pfizer = 0

if isvac == "y" :
    dose1 = input("dose1(sv/sp/az) :")
    dose2 = input("dose2(sv/sp/az/no) :")
    dose3 = input("dose3(sv/sp/az/no) :")
    if dose1 == "sv" and dose2 == "sv" and dose3 == "no" :
        Pfizer = 1
    elif dose1 == "sp" and dose2 == "sp" and dose3 == "no" :
        Pfizer = 1
    elif dose1 == "sv" and dose2 == "no" and dose3 == "no" :
        Pfizer = 1
    elif dose1 == "az" and dose2 == "no" and dose3 == "no" :
        Pfizer = 1
    elif dose1 == "sp" and dose2 == "no" and dose3 == "no" :
        Pfizer = 1
else :
    infected = input("Is infected(y/n) :")
    if infected == "y" :
        Pfizer = 1
    else :
        Pfizer = 2

print(Pfizer)