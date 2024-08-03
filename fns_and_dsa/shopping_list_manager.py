def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input("Enter the item to add:"))
        elif choice == '2':
            # Prompt for and remove an item
            Item = input("Enter the item to remove:")
            if Item in shopping_list:
                shopping_list.remove(Item)
            else:
                print("Item is not in the List")
        elif choice == '3':
            # Display the shopping List
            for i in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()