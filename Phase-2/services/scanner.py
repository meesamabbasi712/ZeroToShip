import os
from models.file_data import FileData

def scan_directory(folder_path):
    files = []

    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)

            file = FileData(
                name=os.path.splitext(filename)[0],
                extension=os.path.splitext(filename)[1],
                size=os.path.getsize(full_path),
                path=full_path,
                created_time=os.path.getctime(full_path),
                modified_time=os.path.getmtime(full_path)
            )

            files.append(file)

    return files


if __name__ == "__main__":
    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Folder does not exist.")
    else:
        result = scan_directory(folder)
        print(f"Found {len(result)} files.")

        for file in result:
            print(file)
