cost = int(input("Cost price :"))
sell = int(input("Selling price :"))

profit = sell-cost

if sell > cost:
    print("You are in profit :",profit)
elif cost > sell:
    print("You are in loss :",profit)
else:
    print("You are in cost to cost :",profit)