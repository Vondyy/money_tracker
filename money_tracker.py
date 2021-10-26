with open('balance.txt') as f:
    contents = f.read()
    print("Your balance is:", contents)

def deposit():
    deposit = int(input("Enter amount to be deposited: "))
    new_balance = balance + deposit
    print("Aasdsadasdmount left in your account: USD" + str(new_balance))
    return (new_balance)
balance = deposit()
##aasdfsdfsdnm
