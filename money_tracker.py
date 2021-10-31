print("This is where you can keep count of your money")
with open(r"balance.txt") as f:
    var = f.read()
print("Your balance is ", var)
john = input(str("Choose a for adding, b for minus: "))
bob = input(str("Enter your number here: "))
if john == "a":
    balance = var + bob
    print("New balance is :", balance)
with open(r"balance.txt", "w") as f: #open in write mode
    balance = var + bob
    f.write(balance)
with open(r"balance.txt") as f:
    balance = f.read()
    print("new balance", balance)
if john == "b":
    balance = var - bob
    print("New balance is :", balance)
with open(r"balance.txt", "w") as f: #open in write mode
    f.write(balance)
with open(r"balance.txt") as f:
    balance = f.read()
    print("new balance", balance)




#print("Your new balance is: ", var)

# def deposit():
#     deposit = int(input("Enter amount to be deposited: "))
#     new_balance = balance + deposit
#     print("Aasdsadasdmount left in your account: USD" + str(contents))
#     return (new_balance)
# balance = deposit()
# ##aasdfsdfsdnm
