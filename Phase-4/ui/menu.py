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

def show_dashboard():
    print("\n" + "=" * 45)
    print("      STORAGE SUMMARY DASHBOARD")
    print("=" * 45)
    print("Total Files      : 250")
    print("Folders Scanned  : 35")
    print("Total Space Used : 12.8 GB")
    print("=" * 45)
    
   def show_warnings():
    print("\n" + "!" * 45)
    print("           STORAGE WARNINGS")
    print("!" * 45)
    print("Warning: 3 Empty folders detected.")
    print("Warning: Large storage block (5.2 GB) found.")
    print("Recommendation: Clean unnecessary files.")
    print("!" * 45)
    def sort_files():
    print("\n" + "=" * 45)
    print("          SORT FILES")
    print("=" * 45)
    print("1. Sort by Name")
    print("2. Sort by Size")
    print("3. Sort by Date")

    option = input("Choose sorting option: ")

    if option == "1":
        print("Files sorted by Name.")
    elif option == "2":
        print("Files sorted by Size.")
    elif option == "3":
        print("Files sorted by Date.")
    else:
        print("Invalid sorting option.")   
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
    show_warnings()

        elif choice == "8":
    sort_files()

        elif choice == "9":
            print("\nThank you for using Storage Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
