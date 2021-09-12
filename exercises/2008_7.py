number1 = float(input("input number1 :"))
number2 = float(input("input number2 :"))
op = input("input operator :")

if op == "+":
    print(number1+number2)
elif op == "-":
    print(number1-number2)
elif op == "*":
    print(number1*number2)
elif op == "/" and number2 != 0 :
    print(number1/number2)
elif op == "%" and number2 != 0 :
    print(number1%number2)
else :
    print("error")