import os
import shutil

# Set the main folder path
main_folder = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/Added_EPOC_NUMBER'

# Set the destination folder path
destination_folder = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/FINAL_FILES'

# Loop through all subfolders and files
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith('.wav'):
            # Get the file path
            file_path = os.path.join(root, file)

            # Copy the file to the destination folder
            shutil.copy(file_path, destination_folder)

print('Files merged successfully!')