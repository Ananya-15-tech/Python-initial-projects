def shipping_fee(is_prime):
    if is_prime=="yes":
     message = "Shipping is free!"

    else:
       message ="Shipping fee:$5"
    return message

prime_status = input("Is the user a prime a prime member(yes/no)?")
result = shipping_fee(prime_status)
print(result)