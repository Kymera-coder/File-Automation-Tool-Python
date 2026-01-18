import os
import shutil

SOURCE_FOLDER = "files"
DESTINATION_FOLDERS = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder not found.")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in DESTINATION_FOLDERS.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    print(f"Moved {file} to {folder}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(SOURCE_FOLDER, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, other_path)
                print(f"Moved {file} to Others")

if __name__ == "__main__":
    organize_files()