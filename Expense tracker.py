expenselist = []

print("WELCOME TO THE EXPENSE TRACKER")

while True:
    print("\n===MENU===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if(choice==1):
        date=input("Enter the date: ")
        category=input("Enter the category (food, travel, makeup): ")
        description=input("Enter the details: ")
        amount=float(input("Enter the amount: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenselist.append(expense)
        print("\n DONE BRO. Expenses are added successfully.")

    elif(choice==2):
        if (len(expenselist)==0):
            print("NO EXPENSES ARE ADDED.")
        else:
            print("===this is all your expenses===")
            count= 1
            for eachexpense in expenselist:
                print(f"expense number {count} => {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                count+=1

    elif(choice==3):
        total=0
        for eachexpense in expenselist:
            total = total + eachexpense["amount"]
        print("\n TOTAL KHARCH", total)

    elif(choice==4):
        print("THANK YOU FOR USING OUR SYSTEM.")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN.")
