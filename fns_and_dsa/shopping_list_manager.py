def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()  # Show menu first

        try:
            choice = int(input("Enter your choice: "))  # ✅ Cast input to number
        except ValueError:
            print("Invalid input. Please enter a number.")  # ✅ Handle non-numeric input
            continue  # Restart loop

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")

        elif choice == 3:
            print("Current Shopping List:")
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
