
stocks = {}

print("Stock Portfolio Tracker")

while True:
    print("\n1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Stock name: ")
        price = float(input("Stock price: "))
        quantity = int(input("Quantity: "))

        stocks[name] = price * quantity
        print("Stock added successfully!")

    elif choice == "2":
        for name, value in stocks.items():
            print(name, ":", value)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
