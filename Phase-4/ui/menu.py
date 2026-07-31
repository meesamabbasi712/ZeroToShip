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
    print("Large Files      : 15")
    print("Old Files        : 20")
    print("Screenshots      : 18")
    print("Archive Files    : 7")
    print("Duplicate Files  : 5")
    print("Empty Folders    : 3")
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
            show_dashboard()

        elif choice == "2":
            print("\nLarge Files")
            print("- movie.mp4")
            print("- project.zip")
            print("- backup.iso")

        elif choice == "3":
            print("\nOld Files")
            print("- report_2021.pdf")
            print("- notes_old.docx")

        elif choice == "4":
            print("\nScreenshots")
            print("- Screenshot1.png")
            print("- Screenshot2.png")

        elif choice == "5":
            print("\nArchive Files")
            print("- files.zip")
            print("- backup.rar")

        elif choice == "6":
            print("\nDuplicate Files")
            print("- copy_photo.jpg")
            print("- duplicate_notes.txt")

        elif choice == "7":
            show_warnings()

        elif choice == "8":
            sort_files()

        elif choice == "9":
            print("\nThank you for using DoomFolder Storage Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
