original_price = float(input("Enter original price:"))
discount = float(input("Enter discount %"))
dis = discount/100*original_price
total_price = original_price-dis
print(total_price)