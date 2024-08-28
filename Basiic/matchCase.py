num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))

operator = input("Enter Operator : ")

match operator:
    case "+":
        print("Addition :",num1+num2)
    case "-":
        print("Subtraction :",num1-num2)
    case "*":
        print("Multiplication :",num1*num2)
    case "/":
        print("Divition :",num1/num2)
    case _:
        print("Enter valid operator :",)


