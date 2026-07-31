def display_menu():
    print("\n" + "=" * 45)
    print("         STORAGE ANALYZER MENU")
    print("=" * 45)
    print("1. View Dashboard")
    print("2. View Large Files")
    print("3. View Old Files")
    print("4. View Screenshots")
    print("5. View Archive Files")
    print("6. View Duplicate Files")
    print("7. View Empty Folders")
    print("8. Sort Files")
    print("9. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nDashboard selected.")

        elif choice == "2":
            print("\nLarge Files selected.")

        elif choice == "3":
            print("\nOld Files selected.")

        elif choice == "4":
            print("\nScreenshots selected.")

        elif choice == "5":
            print("\nArchive Files selected.")

        elif choice == "6":
            print("\nDuplicate Files selected.")

        elif choice == "7":
            print("\nEmpty Folders selected.")

        elif choice == "8":
            print("\nSorting Menu selected.")

        elif choice == "9":
            print("\nThank you for using Storage Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
