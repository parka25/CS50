amountDue = 50
while amountDue > 0:
    print("Amount Due: ", amountDue)
    coin = int(input("Insert Coin: "))
    if coin == 50 or coin == 25 or coin == 5:
        amountDue = amountDue - coin
changedOwed = amountDue
print("Change Owed: ", amountDue)