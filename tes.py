import mysql.connector

# Establishing connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="bank_app",
  password="Doubleg123@"
)

# Creating a cursor object
mycursor = mydb.cursor()

# Function to create a new account
def create_account():
    print("Please provide the following details:")
    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    pin = input("4-digit PIN: ")

    # Inserting user data into the database
    sql = "INSERT INTO customers (name, dob, pin) VALUES (%s, %s, %s)"
    val = (name, dob, pin)
    mycursor.execute(sql, val)
    mydb.commit()

    print("Account created successfully!")
    return mycursor.lastrowid  # Return the customer ID of the newly created account


# Function to authenticate user login
def login():
    print("Please provide your login details:")
   
    pin = input("PIN: ")

    # Retrieving user data from the database
    sql = "SELECT * FROM customers WHERE  pin=%s"
    val = ( pin)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()

    if user:
        print("Login successful!")
        return user
    else:
        print("Invalid login details. Please try again.")
        return None


# Function to check account balance
def check_balance(user):
    print("Your current balance is: $", user[3])


# Function to deposit money into account
def deposit(user):
    amount = float(input("Enter amount to deposit: "))
    current_balance = user[3]
    new_balance = current_balance + amount

    # Updating user balance in the database
    sql = "UPDATE customers SET balance=%s WHERE id=%s"
    val = (new_balance, user[0])
    mycursor.execute(sql, val)
    mydb.commit()

    print("$", amount, "has been deposited into your account.")
    print("Your new balance is: $", new_balance)


# Function to withdraw money from account
def withdraw(user):
    amount = float(input("Enter amount to withdraw: "))
    current_balance = user[3]

    if amount > current_balance:
        print("Insufficient balance.")
    else:
        new_balance = current_balance - amount

        # Updating user balance in the database
        sql = "UPDATE customers SET balance=%s WHERE id=%s"
        val = (new_balance, user[0])
        mycursor.execute(sql, val)
        mydb.commit()

        print("$", amount, "has been withdrawn from your account.")
        print("Your new balance is: $", new_balance)


# Main function
def main():
    user = None

    while True:
        if not user:
            print("1. Login")
            print("2. Create Account")
            print("3. Quit")
            choice = int(input("Enter choice: "))

            if choice == 1:
                user = login()
            elif choice == 2:
                user = create_account()
            elif choice == 3:
                print("Thank you for using our banking app!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            choice = int(input("Enter choice: "))

            if choice == 1:
                check_balance(user)
            elif choice == 2:
                deposit(user)
            elif choice == 3:
                withdraw(user)
            elif choice == 4:
                user = None
            else:
                print("Invalid choice. Please try again.")

