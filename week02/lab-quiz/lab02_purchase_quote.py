item1=input("enter item name: ")
quantity_one=int(input("enter quantity:"))
unit_price_one=float(input("enter unit price:"))
item2=input("enter second item: ")
quantity_two=int(input("enter quantity:"))
unit_price_two=float(input("enter unit price:"))
delivery_fee=float(input("delivery fee:"))
tax_percent=float(input("tax percent:"))


line1_total= quantity_one * unit_price_one
line2_total= quantity_two * unit_price_two
subtotal= line1_total + line2_total

tax_amount= subtotal * (tax_percent/100)

final_total= subtotal+ tax_amount+ delivery_fee
print("\n purchase quote")
print(f"{item1} line total: {line1_total:.2f} TRY")
print(f"{item2} line total: {line2_total:.2f} TRY")
print(f"tac amount: {tax_amount:.2f} TRY")
print(f"Final total: {final_total:.2f} TRY")

#input() function always returns a string. we must convert it to int or float before arithmatic.
