import os
import shutil

def organize_files(folder_path, file_categories):
    # Create folders for each category if they don't exist
    for category, extensions in file_categories.items():
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through files and move them to the corresponding folders
    for file in files:
        for category, extensions in file_categories.items():
            if file.lower().endswith(tuple(extensions)):
                file_path = os.path.join(folder_path, file)
                destination_path = os.path.join(folder_path, category, file)

                # Move the file to the corresponding folder
                shutil.move(file_path, destination_path)
                print(f"Moved {file} to {category} folder.")

if __name__ == "__main__":
    # Specify the folder path where the script will operate
    folder_path = r"C:\path\to\your\folder"

    # Define file categories and their corresponding extensions
    file_categories = {
        'photos': ['.jpg', '.jpeg'],
        'programs': ['.exe'],
        'documents': ['.pdf', '.doc', '.docx'],
        'audio_video': ['.mp3', '.mp4']
        # Add more categories and extensions as needed
    }

    # Call the function to organize files
    organize_files(folder_path, file_categories)