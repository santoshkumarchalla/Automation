File Organization Script

Overview
This Python script organizes files in a specified directory based on their file extensions. It creates destination folders for different file types and moves files accordingly. Additionally, the script creates a backup of the files before moving them and zips the backup folder.

Features
File Organization: Files are categorized into folders based on their extensions (e.g., TextFiles, PDFFiles, ImageFiles).

Backup and Zip: Before moving files, a backup folder is created, and its contents are compressed into a zip file (backup_archive.zip).

Logging: Activities and any errors are logged to a file (file_organization_log.txt) for reference.

Usage
- Run the script: python file_organization.py.
- Enter the path to the directory in the main.
- The script will organize files, create a backup, and log activities.
