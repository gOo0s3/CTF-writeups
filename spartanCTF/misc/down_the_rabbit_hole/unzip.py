import os
import zipfile

def extract_zip(zip_file_path, folder_name):
    # Extract zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(folder_name)

    # Check for zip files inside the extracted files
    for file in os.listdir(folder_name):
        if file.endswith(".zip"):
            # Create new folder with same name as extracted zip file
            new_folder = os.path.join(folder_name, file[:-4])
            os.mkdir(new_folder)

            # Extract the next level of zip files
            zip_path = os.path.join(folder_name, file)
            extract_zip(zip_path, new_folder)

# Set the path of your first zip file
root_zip_path = "hole.zip"
root_folder = "."
# Extract the root zip file
extract_zip(root_zip_path, root_folder)
