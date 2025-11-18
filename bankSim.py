
num = int(input("How many bank accounts do you want to create? ")) 

for i in range(num):
    print(f"\nCreating account {i+1}:")
    
    name = input("Enter account owner's name: ")   
    balance = float(input("Enter initial balance: ")) 
    
    accounts.append([name, balance])  

print("\nAccounts have been created successfully!\n")    


while True:
    print("\n===== BANKING MENU =====")
    print("1. Show all account balances")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Show accounts above average balance")
    print("5. Exit")

    choice = input("Choose an option: ")  
1]}")

    
    elif choice == "2":
        name = input("Enter account name: ")  
        found = False
        for acc in accounts:
            if acc[0] == name:
                amount = float(input("Deposit amount: "))  
                acc[1] += amount
                print("Deposit successful!")
                found = True
                break
        if not found:
            print("Account not found!")


    elif choice == "3":
        name = input("Enter account name: ")  
        found = False
        for acc in accounts:
            if acc[0] == name:
                amount = float(input("Withdraw amount: "))  
                if amount <= acc[1]:
                    acc[1] -= amount
                    print("Withdrawal successful!")
                else:
                    print("Not enough balance!") 
                found = True
                break
        if not found:
            print("Account not found!")

   
    elif choice == "4":
        avg = sum(acc[1] for acc in accounts) / len(accounts)  
        print(f"\nAverage balance: {avg}")
        print("*** Accounts above average ***")
        for acc in accounts:
            if acc[1] > avg:
                print(f"{acc[0]} : {acc[1]}")

   
    elif choice == "5":
        print("Exiting program... Goodbye!")  
        break

    else:
        print("Invalid option! Try again.") 


    if choice == "1":
        print("\n*** All Accounts ***")
        for acc in accounts:
            print(f"{acc[0]} : {acc[