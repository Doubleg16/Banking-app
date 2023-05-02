import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="bank_app",
    password="Doubleg123@"
)

mycursor = mydb.cursor()

def login():
    print("Please enter your account details to login.")
    account_num = input("Account number: ")
    pin = input("PIN: ")

    mycursor.execute("SELECT * FROM customers WHERE account_num = %s AND pin = %s", (account_num, pin))
    result = mycursor.fetchone()

    if result:
        print("Login successful.")
        return True
    else:
        print("Invalid account number or PIN.")
        return False

def create_account():
    print("Please enter your personal details to create an account.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    dob = input("Date of birth (YYYY-MM-DD): ")
    initial_deposit = float(input("Initial deposit: "))
    pin = input("Choose a 4-digit PIN: ")
    account_num = "BA" + str(hash(first_name + last_name + dob))[-8:] # generate account number

    # insert new customer into the database
    sql = "INSERT INTO customers (account_num, first_name, last_name, dob, balance, pin) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (account_num, first_name, last_name, dob, initial_deposit, pin)
    mycursor.execute(sql, val)
    mydb.commit()

    print("Account created successfully.")
    print("Your account number is:", account_num)

def deposit():
    print("Please enter the following details to deposit money.")
    account_num = input("Account number: ")
    amount = float(input("Amount to deposit: "))

    mycursor.execute("SELECT balance FROM customers WHERE account_num = %s", (account_num,))
    result = mycursor.fetchone()

    if result:
        balance = result[0]
        new_balance = balance + amount
        mycursor.execute("UPDATE customers SET balance = %s WHERE account_num = %s", (new_balance, account_num))
        mydb.commit()
        print("Deposit successful.")
        print("New balance:", new_balance)
    else:
        print("Invalid account number.")

def withdraw():
    print("Please enter the following details to withdraw money.")
    account_num = input("Account number: ")
    amount = float(input("Amount to withdraw: "))

    mycursor.execute("SELECT balance FROM customers WHERE account_num = %s", (account_num,))
    result = mycursor.fetchone()

    if result:
        balance = result[0]
        if amount <= balance:
            new_balance = balance - amount
            mycursor.execute("UPDATE customers SET balance = %s WHERE account_num = %s", (new_balance, account_num))
            mydb.commit()
            print("Withdrawal successful.")
            print("New balance:", new_balance)
        else:
            print("Insufficient funds.")
    else:
        print("Invalid account number.")

def check_balance():
    account_num = input("Account number: ")

    mycursor.execute("SELECT balance FROM customers WHERE account_num = %s", (account_num,))
    result = mycursor.fetchone()

    if result:
        balance = result[0]
        print("Current balance:", balance)
    else:
        print("Invalid account number.")

# main program loop
while True:
    print("Welcome to the Bank App.")
    print("1. Login")
    print("2. Create account")
   
