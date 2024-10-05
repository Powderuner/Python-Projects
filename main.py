import os
import shutil
import datetime


def backup_files(source_directory, backup_directory):
    # Create the backup directory with the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(backup_directory, f"backup_{timestamp}")

    try:
        # Make the backup directory
        os.makedirs(backup_path, exist_ok=True)
        print(f"Backup directory created at: {backup_path}")

        # Copy all files and directories from the source to the backup directory
        for root, dirs, files in os.walk(source_directory):
            relative_path = os.path.relpath(root, source_directory)
            dest_dir = os.path.join(backup_path, relative_path)
            os.makedirs(dest_dir, exist_ok=True)

            for file in files:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} to {dest_file_path}")

        print("Backup completed successfully.")

    except Exception as e:
        print(f"An error occurred during backup: {e}")


if __name__ == "__main__":
    # Set your source and backup directories here
    source_directory = "/Users/markarmstrong/Documents/CS 1436"  # Change this to the directory you want to back up
    backup_directory = "/Users/markarmstrong/Documents/CS 3341"  # Change this to where you want the backup to be saved

    # Run the backup function
    backup_files(source_directory, backup_directory)
