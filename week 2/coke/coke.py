coke_price = 50

while coke_price > 0:
    print("Amount Due:", coke_price)
    coin = int(input("Insert coin: "))

    if coin in [5, 10, 25, 50]:
        coke_price -= coin
    else:
        print("Invalid coin")

print("Change Owed:", abs(coke_price))