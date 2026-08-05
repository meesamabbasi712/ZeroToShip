# Scanner code will be added here
import os
from file_data import FileData


def scan_directory(folder_path):
    files = []

    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)

            try:
                file = FileData(full_path)
                files.append(file)
            except Exception:
                # Skip files that cannot be accessed
                continue

    return files


if __name__ == "__main__":
    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Folder does not exist.")
    else:
        files = scan_directory(folder)
        print(f"\nFound {len(files)} files.\n")

        for file in files:
            print(file)
