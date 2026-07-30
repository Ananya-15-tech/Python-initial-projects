#Product Stock Checker
product_number = int(input("Enter the product number:"))
if product_number>=10:
    print("Product available") 
elif product_number <10 and product_number >0:
    print("Last few left")
else :
    print("Out of Stock")
