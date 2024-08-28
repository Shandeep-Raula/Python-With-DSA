num = int(input("Possitive number :"))

if num % 15 ==0 :
    print("Divisible by 15")
else :
    if num % 3 == 0 or num % 5 ==0:
        print("Divisible by 3 or 5") 
    else:
        print("Not divisible")

