 CLI that computes tip and per-person split for a
restaurant bill.\ 

print("Tip Calculator")

bill = input("Enter the bill amount: $")
tip_percent = input("Enter the tip percentage (e.g., 15): ")
num_people = input("Enter the number of people: ")

try:
    bill = float(bill)
    tip_percent = float(tip_percent)
    num_people = int(num_people)

    if bill <= 0:
        print("Bill amount must be greater than 0.")
        exit()

    if tip_percent < 0:
        print("Tip percentage can't be negative.")
        exit()

    if num_people <= 0:
        print("Number of people must be at least 1.")
        exit()

    tip_amount = bill * tip_percent / 100
    total = bill + tip_amount
    per_person = total / num_people

    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total:.2f}")
    print(f"Amount per person: ${per_person:.2f}")

except ValueError:
    print("Please enter valid numbers.")
