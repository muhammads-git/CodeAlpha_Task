import os
import shutil

def organize_files_by_extension(directory):
    # Change to the target directory
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("The specified directory does not exist.")
        return

    # List all files in the directory
    files = [file for file in os.listdir() if os.path.isfile(file)]

    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)
        # Remove the leading period (.)
        extension = extension[1:]

        # Create a new directory for the extension if it doesn't exist
        if extension:  # Only process files with extensions
            if not os.path.exists(extension):
                os.makedirs(extension)

            # Move the file to the respective directory
            shutil.move(file, os.path.join(extension, file))
            print(f'Moved: {file} to folder: {extension}/')

def main():
    directory = input("Enter the path of the directory to organize: ")
    organize_files_by_extension(directory)
    print("File organization complete.")

if __name__ == "__main__":
    main()
