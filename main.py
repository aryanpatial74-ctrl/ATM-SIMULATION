print(":::::::::: Welcome to Patial's ATM:::::::::::")
print("Please insert your card...")



from account_acess import account_access

while True:
    print("\nENTER THE TASK YOU WOULD LIKE TO DO:")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Exit")

    option = input("ENTER YOUR OPTION: ")

    if option == "1":
        from options import deposit
        deposit()
    elif option == "2":
        from options import withdrawl
        withdrawl()
    elif option == "3":
        print("Thank you for using Patial's ATM.")
        break
    else:
        print("INVALID OPTION. Please try again.")

