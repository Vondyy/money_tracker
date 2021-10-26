print("This is where you can keep count of your money")
with open(r"balance.txt") as f:
    var = f.read()
print("Your balance is ", var)
bob = input("Enter your number here: ")
with open(r"balance.txt", "w") as f: #open in write mode
    f.write(bob)
with open(r"balance.txt") as f:
    var = f.read()
print("Your new balance is: ", var)
# def deposit():
#     deposit = int(input("Enter amount to be deposited: "))
#     new_balance = balance + deposit
#     print("Aasdsadasdmount left in your account: USD" + str(contents))
#     return (new_balance)
# balance = deposit()
# ##aasdfsdfsdnm
