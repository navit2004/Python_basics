# write a python program to print the conntents of a directory using the os module. Search online for the function which does that. 
import os

def print_directory_contents(directory):
    try:
        # Get the list of all files and directories in the specified directory
        contents = os.listdir(directory)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")

# Example usage:
directory_path = '.'  # Replace with the path to your directory of interest
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
