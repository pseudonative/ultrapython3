from random import choice
food=choice(["cheese pizza","quiche","morning bun","gummy bear","tea cake"])

bakery_stock={
    "almond croussant":12,
    "toffee cookie":3,
    "morning bun":1,
    "chocolate chunk cookie":9,
    "tea cake":25
}
'''
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
'''

quantity=bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")












