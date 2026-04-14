import json
import re

balance = 10000
transactions = []
PIN_FILE = "pin.json"

# Load or create PIN
def load_pin():
    try:
        with open(PIN_FILE, "r") as file:
            data = json.load(file)
            return data["pin"]
    except:
        return None

def save_pin(pin):
    with open(PIN_FILE, "w") as file:
        json.dump({"pin": pin}, file)

# Set PIN
def set_pin():
    pattern = r"^\d{4}$"
    while True:
        pin = input("Create a 4-digit PIN: ")
        if re.match(pattern, pin):
            save_pin(pin)
            print(" PIN created successfully")
            break
        else:
            print("Enter exactly 4 digits")

#  Check PIN
def check_pin():
    saved_pin = load_pin()
    if not saved_pin:
        print("No PIN found. Please set PIN first.")
        set_pin()
        return check_pin()

    pin = input("Enter your PIN: ")
    if pin == saved_pin:
        print("Access granted")
        return True
    else:
        print("Incorrect PIN")
        return False

# Check Balance
def check_balance():
    print(f"Current Balance: ₹{balance}")

#  Deposit
def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print(" Enter a valid amount")
            return
        balance += amount
        transactions.append({"type": "Deposit", "amount": amount, "balance": balance})
        print(f" Deposited ₹{amount}. New Balance: ₹{balance}")
    except:
        print("Invalid input")

# Withdraw
def withdraw():
    global balance
    LIMIT = 5000  # daily limit

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter valid amount")
        elif amount > LIMIT:
            print(f"Limit exceeded! Max ₹{LIMIT}")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append({"type": "Withdraw", "amount": amount, "balance": balance})
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{balance}")
    except:
        print("Invalid input")

# Transactions
def show_transactions():
    if not transactions:
        print("⚠ No transactions yet")
    else:
        print("\n--- Transaction History ---")
        for t in transactions:
            print(f"{t['type']} | ₹{t['amount']} | Balance: ₹{t['balance']}")

#  Menu
def menu():
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transactions\n5. Exit")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("Enter a number (1-5)")
            continue

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_transactions()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

# Start Program
if check_pin():
    menu()
