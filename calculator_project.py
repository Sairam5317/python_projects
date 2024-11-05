def get_operand(number):
    while True:
        operand = input("Enter "+str(number)+ " operand: ")
        try:
            operand = float(operand)
            return operand
        except:
            print("inavalid operand,It should be numerical")
operand1 = get_operand(1)
operand2 = get_operand(2)

result = 0
operator = input("enter the operation sign that you want to perform: ")
if operator == "+":
    result = operand1 + operand2
elif operator == "-":
    result = operand1 - operand2
elif operator == "*":
    result = operand1 * operand2
elif operator == "/":
    result = operand1 / operand2
else:
    print("invalid operator")
print(result)