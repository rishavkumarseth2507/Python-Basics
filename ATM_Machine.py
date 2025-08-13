'''
Project: ATM Machine
Concept:
A user can “log in” with a PIN, check their balance, deposit money, withdraw money, or exit.
'''

balance = 1000
pin = "1234"

a = input("Enter 4-digit pin: ")
if a != pin:
    print("Incorrect PIN, Access denied!")
else:
    
    while(True):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = int(input("Choose an option (1-4): "))
        if(choice==1):  print(f"Your balace is: {balance: .2f}")
        elif(choice==2):    
            amount = float(input("Enter amount to Deposit: "))
            if amount>0:
                balance += amount
                print(f"Your balace is: {balance: .2f}")
        elif(choice==3):
            amount = float(input("Enter amount to Withdraw: "))
            if(amount > balance):
                print("Insufficient Balance!")
            else:   
                balance -= amount
                print(f"Your balace is: {balance: .2f}")
        elif(choice==4):    
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-4.")
        

    