def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

def get_price(choice):
    if choice == 1:
        return 3.00
    elif choice == 2:
        return 5.00
    elif choice == 3:
        return 4.00
    elif choice == 4:
        return 1.45
    return 0.00

names = {1: "Taco", 2: "Burrito", 3: "Nachos", 4: "Soft Drink"}

ordered = []
total = 0.0

print("Welcome to Taco Palace! Please view the menu below and make a selection")

choice = 0
while choice != 5:
    print_menu()
    choice = int(input("Enter your choice: "))

    if choice in names:
        print("You selected a", names[choice])
        ordered.append(names[choice])
        total = total + get_price(choice)
    elif choice != 5:
        print("Invalid choice. Please try again.")

print()
print("You ordered:" , ", ".join(ordered))
print("Your total is $", total)