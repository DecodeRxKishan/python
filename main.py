Item_name=input("Enter the name of the item: ")
Quantity=int(input("Enter the Quantity of the item: "))
price=float(input("Enter the price of the item: "))
total=(Quantity * price)

print("##################BILL####################")
print("Item name     Quantity     price")
print(" ", Item_name,"      ", Quantity,"       ", price)
print("Amount to be paid", total)
print("##################BILL####################")


