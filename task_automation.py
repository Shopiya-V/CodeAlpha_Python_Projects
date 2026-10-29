import os
import shutil

folder = input("Enter folder path: ")

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):
        ext = file.split(".")[-1].lower()

        if "." in file:
            new_folder = os.path.join(folder, ext + "_files")
        else:
            new_folder = os.path.join(folder, "Others")

        os.makedirs(new_folder, exist_ok=True)
        shutil.move(path, os.path.join(new_folder, file))

print("Files organized successfully!")
