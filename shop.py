import datetime
name = input("What is your gmail? {EXAMPLE : insert@gmail.com} ")
product = input("What do you want today? {product} ")
qty = int ( input("Quantity? ") )
price_per_unit = float ( input("Price_per_unit ") )
subtotal = qty * price_per_unit
tax_rate = 0.07
tax = subtotal * tax_rate
total = subtotal + tax
dt = datetime.datetime.now()

print(dt)
print("---------------------")
print("-------RECIEPT-------")
print("---------------------")
print("My gmail is ", name)
print("I want ", product)
print("The quanity is ", qty)
print("The price per unit is ", price_per_unit)
print("subtotal ", subtotal)
print("tax_rate ", tax_rate)
print("tax 7%" , tax)
print("total" , total)


