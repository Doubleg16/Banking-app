def ask_create_or_deposit():
    choice = input("Do you want to create an account or deposit money? (type 'create' or 'deposit'): ")
    while choice.lower() not in ['create', 'deposit']:
        choice = input("Invalid choice. Please type 'create' or 'deposit': ")
    return choice.lower()

user_choice = ask_create_or_deposit()

if user_choice == 'create':
    # call function to create account
    create_account()
elif user_choice == 'deposit':
    # call function to deposit money
    deposit_money()
else:
    # handle invalid choice
    print("Invalid choice")