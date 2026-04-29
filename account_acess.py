from databse import accounts

def account_access():
    acc_no = input("Enter your account number: ")
    entered_pin = int(input("Enter your PIN: "))

    if acc_no in accounts and accounts[acc_no]["pin"] == entered_pin:
        print("Access granted. Welcome", accounts[acc_no]["name"])
        print("Your balance is ₹", accounts[acc_no]["balance"])
    else:
        print("Invalid account number or PIN")

account_access()




