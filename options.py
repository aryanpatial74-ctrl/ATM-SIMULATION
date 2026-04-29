from databse import accounts

def withdrawl():
    acc_no = input("Enter your account number: ")
    entered_pin = int(input("Enter your PIN: "))

    if acc_no in accounts and accounts[acc_no]["pin"] == entered_pin:
        print("Access granted. Welcome", accounts[acc_no]["name"])
        print("Your current balance is ₹", accounts[acc_no]["balance"])

        withdrawl_amount = int(input("Enter the amount you would like to withdraw: "))
        if withdrawl_amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= withdrawl_amount
            print("Withdrawal successful!")
            print("Remaining balance is ₹", accounts[acc_no]["balance"])
        else:
            print("Insufficient balance. Transaction cancelled.")
    else:
        print("Invalid account number or PIN")

def deposit():
    acc_no = input("Enter your account number: ")
    entered_pin = int(input("Enter your PIN: "))

    if acc_no in accounts and accounts[acc_no]["pin"] == entered_pin:
        print("Access granted. Welcome", accounts[acc_no]["name"])
        print("Your current balance is ₹", accounts[acc_no]["balance"])

        deposit_amount = int(input("Enter the amount you would like to deposit: "))
        accounts[acc_no]["balance"] += deposit_amount
        print("Deposit successful!")
        print("Updated balance is ₹", accounts[acc_no]["balance"])
    else:
        print("Invalid account number or PIN")


if __name__ == "__main__":
    withdrawl()
    deposit()
