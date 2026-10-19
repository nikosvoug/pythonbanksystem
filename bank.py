from email import message
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


data = {
    "walletMoney": 0,
    "bankMoney": 0,
    "pin": 0,
    "pinVisible": False,
}

def inputData():
    global cashmoney, loginpin
    cashmoney = int(input("Enter your cash money: "))
    loginpin = int(input("Enter your pin to login: "))
    if cashmoney < 0 or loginpin < 0 or len(str(loginpin)) != 4:
        print("Please enter a valid amount of cash and pin")
        time.sleep(2)
        clear()
        inputData()
    data["walletMoney"] = cashmoney
    data["pin"] = loginpin

def mainMenu(firstTime=True):
    if firstTime:
        print("Welcome to the bank")
        time.sleep(2)
    clear()
    print("CASH: " + str(data["walletMoney"]) + "$")
    print("BANK: " + str(data["bankMoney"]) + "$")
    pin_display = str(data["pin"]) if data["pinVisible"] else "****"
    print("PIN: " + pin_display)
    print("1. Deposit money")
    print("2. Withdraw money")
    print("/showpin, /hidepin")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        depositMoney()
    elif choice == "2":
        withdrawMoney()
    elif choice == "/showpin":
        data["pinVisible"] = True
        mainMenu(False)
    elif choice == "/hidepin":   
        data["pinVisible"] = False
        mainMenu(False)
    elif choice == "0":
        exit()
    else:
        print("Invalid choice, please try again.")
        mainMenu()

def depositMoney():
    damount = int(input("Enter the money you want to deposit: "))
    if damount >= data["walletMoney"] and damount > 0:
        print("Your cash balance is too low please try again with a new amount")
        loopPrint(3, "Returning to main menu in:")
        mainMenu(False)
    else:
        data["bankMoney"] += damount
        data["walletMoney"] -= damount
        print("You have just deposited " + str(damount) + "$ to your bank account")
        clear()
        mainMenu(False)

def withdrawMoney():
    wamount = int(input("Enter the money you want to withdraw: "))
    if wamount >= data["bankMoney"] and wamount > 0:
        print("Your cash balance is too low please try again with a new amount")
        loopPrint(3, "Returning to main menu in:")
        mainMenu(False)
    else:
        data["walletMoney"] += wamount
        data["bankMoney"] -= wamount
        print("You have just withdrawed " + str(wamount) + "$ in cash")
        clear()
        mainMenu(False)

def loopPrint(times, message):
    loko = times
    for i in range(times):
        print(f"{message} ({loko})")
        loko -= 1
        time.sleep(1)
        clear()

def whilePrint(message):
    global entered, warning
    while entered:
        if warning > 1:
            print("Error")
            entered = False
        print(f"{message}")

if __name__ == "__main__":
    inputData()
    mainMenu()