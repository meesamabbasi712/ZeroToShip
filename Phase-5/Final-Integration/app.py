from scanner import scan_directory
from analyzer import analyze_files, find_empty_folders


def show_list(title, files):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if not files:
        print("No files found.")
    else:
        for file in files:
            print(file.location)

    print("=" * 50)


def dashboard(files, analysis, empty_folders):
    print("\n" + "=" * 50)
    print("STORAGE SUMMARY DASHBOARD")
    print("=" * 50)

    total_size = sum(file.size for file in files)

    print(f"Total Files      : {len(files)}")
    print(f"Large Files      : {len(analysis['large_files'])}")
    print(f"Old Files        : {len(analysis['old_files'])}")
    print(f"Screenshots      : {len(analysis['screenshots'])}")
    print(f"Archive Files    : {len(analysis['archive_files'])}")
    print(f"Duplicate Groups : {len(analysis['duplicates'])}")
    print(f"Empty Folders    : {len(empty_folders)}")
    print(f"Total Space Used : {round(total_size / (1024*1024), 2)} MB")


def main():
    folder = input("Enter folder path to scan: ")

    files = scan_directory(folder)
    analysis = analyze_files(files)
    empty_folders = find_empty_folders(folder)

    while True:

        print("\n" + "=" * 45)
        print("        DOOM FOLDER STORAGE ANALYZER")
        print("=" * 45)
        print("1. View Dashboard")
        print("2. View Large Files")
        print("3. View Old Files")
        print("4. View Screenshots")
        print("5. View Archive Files")
        print("6. View Duplicate Files")
        print("7. View Empty Folders")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            dashboard(files, analysis, empty_folders)

        elif choice == "2":
            show_list("Large Files", analysis["large_files"])

        elif choice == "3":
            show_list("Old Files", analysis["old_files"])

        elif choice == "4":
            show_list("Screenshots", analysis["screenshots"])

        elif choice == "5":
            show_list("Archive Files", analysis["archive_files"])

        elif choice == "6":
            print("\nDuplicate Files")
            print("=" * 50)

            if not analysis["duplicates"]:
                print("No duplicate files found.")
            else:
                for group in analysis["duplicates"].values():
                    print()
                    for file in group:
                        print(file.location)

        elif choice == "7":
            print("\nEmpty Folders")
            print("=" * 50)

            if not empty_folders:
                print("No empty folders found.")
            else:
                for folder in empty_folders:
                    print(folder)

        elif choice == "8":
            print("\nThank you for using Doom Folder Storage Analyzer!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
