import os
from pathlib import Path

print("=== DoomFolder Environment Check ===")

print("Current Working Directory:")
print(os.getcwd())

print("\nPathlib imported successfully!")

folder = Path.cwd()
print("Current Folder:", folder)
