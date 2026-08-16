







from datetime import datetime

def add_expense():
    print("\n💰 ADD EXPENSE")
    print("------------------------")

    budget = float(input("Daily budget ₹: "))
    food = float(input("Food ₹: "))
    travel = float(input("Travel ₹: "))
    other = float(input("Other ₹: "))

    total = food + travel + other
    balance = budget - total

    print("\n========================")
    print("       SUMMARY")
    print("========================")
    print("Budget  : ₹", budget)
    print("Total   : ₹", total)
    print("Balance : ₹", balance)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("history.txt", "a") as file:
        file.write(
            f"{now} | Budget ₹{budget} | "
            f"Food ₹{food} | Travel ₹{travel} | "
            f"Other ₹{other} | Total ₹{total} | "
            f"Balance ₹{balance}\n"
        )

    print("\n✅ Expense saved!")

    if balance >= 0:
        print("👍 Within budget")
    else:
        print("⚠️ Over budget")


def view_history():
    print("\n📋 EXPENSE HISTORY")
    print("========================")

    try:
        with open("history.txt", "r") as file:
            data = file.read()

        if data:
            print(data)
        else:
            print("No history yet.")

    except FileNotFoundError:
        print("No history yet.")


while True:
    print("\n")
    print("╔════════════════════════╗")
    print("║     💰 MONEY MANAGER   ║")
    print("╠════════════════════════╣")
    print("║  1️⃣  Add Expense       ║")
    print("║  2️⃣  View History      ║")
    print("║  3️⃣  Exit              ║")
    print("╚════════════════════════╝")

    choice = input("👉 Choose: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("\nThanks for using Money Manager! 👋")
        break

    else:
        print("❌ Invalid choice")

