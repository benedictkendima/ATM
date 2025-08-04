print("welcome to dummies Bank \n insert your card")
user_pin = 1234
option = 0
balance = 10000
pin = int(input("enter your pin:>>> "))
if user_pin == pin:
    while option != 4:
        print('''
        ******OPTIONS******
            1. Balance
            2. Withdraw
            3. Transfer
            4. Quite\n
        ''')

        option = int(input("select from option:>>> "))
        if option == 1:
            print(f"Your balance is {balance}")
        elif option == 2:
            withdrawal = int(input("input amount amount:\n>>> #"))
            balance -= withdrawal
            print("you withdrawed #",withdrawal)
            print("your main Balane is: #",balance)
        elif option == 3:
            beneficiary = int(input("Enter Beneficiary account number:\n>>>"))
            print("confirm account details\n",beneficiary)
            beneficiary_amount = int(input("enter amount"))
            balance -= beneficiary_amount
            print("Are you sure you want to send #",beneficiary_amount ,"to ", beneficiary)
            print("your balane is: ",balance)
        elif option == 4:
            print("Thanks for Banking with us")
        else:
            print("Invalid Input")
else:
    print("incorrect password")


