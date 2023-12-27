import os
import shutil
import logging
import zipfile

def zip_backup_folder(backup_folder, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(backup_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, backup_folder)
                zipf.write(file_path, arcname=arcname)

def organize_files(directory_path):
    # Create a dictionary to map file extensions to folder names
    folder_mapping = {
        '.txt': 'TextFiles',
        '.pdf': 'PDFFiles',
        '.jpg': 'ImageFiles',
        # Add more extensions and folder names as needed
    }

    # Set up logging to a file
    logging.basicConfig(filename='file_organization_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    # Set up logging to the console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # Log the start of the script
    logging.info('File organization script started.')

    try:
        # Create the backup folder
        backup_folder = os.path.join(directory_path, 'Backup')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # Zip the backup folder
        zip_file_path = os.path.join(directory_path, 'backup_archive.zip')
        zip_backup_folder(backup_folder, zip_file_path)
        logging.info(f'Backup folder zipped to {zip_file_path}')

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)

                # Check if the extension is in the mapping
                if file_extension in folder_mapping:
                    destination_folder = os.path.join(directory_path, folder_mapping[file_extension])

                    # Create the destination folder if it doesn't exist
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    # Move the file to the destination folder
                    shutil.move(file_path, os.path.join(destination_folder, filename))

                    # Log the file movement
                    logging.info(f'Moved {filename} to {destination_folder}')

        # Log the successful completion of the script
        logging.info('File organization script completed successfully.')
        print('File organization script completed successfully.')

    except Exception as e:
        # Log any exceptions that occur during the script execution
        logging.error(f'An error occurred: {str(e)}')
        print(f'An error occurred: {str(e)}')  # Print the error message to the console

if __name__ == "__main__":
    # Get user input for the directory path
    directory_path = r'D:\Learn_visual_studio\test_folder'

    # Call the organize_files function
    organize_files(directory_path)
