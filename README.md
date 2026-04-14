# ATM-Machine-System
A simple ATM Machine simulation built using Python functions. This project allows users to perform basic banking operations like checking balance, depositing, withdrawing money, and viewing transaction history.

Project Overview

This application simulates real-world ATM functionality, including:

Secure PIN-based login

Deposit and withdrawal operations

Transaction history tracking

Balance management

The project uses JSON storage for PIN persistence and demonstrates real-world banking logic.

🚀 Features

🔐 Secure PIN authentication system

💰 Check account balance

➕ Deposit money

➖ Withdraw money with limit

📜 View detailed transaction history

⚠ Input validation to prevent errors

💾 Persistent PIN storage using JSON

🛠️ Tech Stack

Python 

JSON (for storing PIN securely)

re module (for PIN validation)

📂 File Structure

atm_machine.py

pin.json   # Auto-created for storing PIN

▶️ How to Run

Install Python (3.x)

Save the code in:

atm_machine.py


Run the program:

python atm_machine.py

📋 Menu Options

1. Check Balance
3. Deposit
4. Withdraw
5. Transactions
6. Exit

🧪 Example Usage

➤ PIN Setup (First Time)

Create a 4-digit PIN: 1234

✅ PIN created successfully

➤ Login

Enter your PIN: 1234

✅ Access granted

➤ Deposit

Enter amount to deposit: 2000

✅ Deposited ₹2000. New Balance: ₹12000

➤ Withdraw

Enter amount to withdraw: 3000

✅ Withdrawn ₹3000. Remaining Balance: ₹9000

➤ Transaction History

--- Transaction History ---

Deposit | ₹2000 | Balance: ₹12000
Withdraw | ₹3000 | Balance: ₹9000


🔒 Security Features

PIN must be exactly 4 digits

PIN stored securely using JSON

PIN required before accessing menu

⚠️ Validation & Error Handling

Prevents invalid inputs (letters instead of numbers)

Prevents negative or zero amounts

Prevents withdrawal beyond balance

Enforces withdrawal limit (₹5000 per transaction)

✨ Improvements Implemented

✅ Fixed PIN validation logic

✅ Added secure PIN storage

✅ Implemented input validation using try-except

✅ Added structured transaction history

✅ Added withdrawal limit

✅ Improved user-friendly output

🔧 Future Improvements

👤 Multiple user accounts

💾 Save balance & transactions to file

🏦 ATM card simulation

📊 Expense analysis integration

🌐 Convert to web app using Flask

🔐 Encrypt PIN for better security
