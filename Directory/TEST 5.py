import os
import shutil
import datetime

# Defining variables
today = datetime.date.today()
part_1 = 'selfTest_MCU'
part_2 = 'Module_Report'
# This concatenates the beginning and end of the name
name = f"{part_1}_{part_2}"
# This is the format of the filename
test_report = f"{name}_{today}.txt"

# This creates the file that we are going to write to and is named as test_report
with open(test_report, 'w') as file:
    file.write("Any Text")

# Defining The Paths
# We are getting the current working directory and assigning it to a variable
current_directory = os.getcwd()
# Printing to ensure the current working directory is correct
print("Current Directory:", current_directory)

# Here we are joining the current working directory with the filename
destination_file_path = os.path.join(current_directory, test_report)

# This is where the folders we want to copy data from are located
source_directory_paths = [
    'C:\\Users\\hagbi\\Desktop\\Coding\\SoftwareDev\\Uncle_Atif_Work_XP\\Python\\Automation\\Directory\\Part_2',
    'C:\\Users\\hagbi\\Desktop\\Coding\\SoftwareDev\\Uncle_Atif_Work_XP\\Python\\Automation\\Directory\\Part_1'
]

# Showing destination file path to ensure it's the correct path
print("Destination_file_path:", destination_file_path)

# Make the folder if it doesn't exist
if not os.path.exists(destination_file_path):
    os.makedirs(destination_file_path)

# Iterate through source directories
for source_directory_path in source_directory_paths:
    if os.path.isdir(source_directory_path):
        # List files in the source directory
        for filename in os.listdir(source_directory_path):
            if filename.endswith('.txt') and filename.startswith('NTF'):
                try:
                    source_file_path = os.path.join(source_directory_path, filename)
                    # Open the source file and read its contents
                    with open(source_file_path, 'r') as source_file:
                        file_contents = source_file.read()

                    # Open the destination file and write the contents
                    with open(os.path.join(destination_file_path, filename), 'w') as destination_file:
                        destination_file.write(file_contents)
                    print(f"Contents copied from '{source_file_path}' to '{destination_file_path}' successfully")
                except IOError as e:
                    if e.errno == 13:
                        print("Permission Denied: Error 13")
                    else:
                        print("An error occurred:", e)
                except Exception as e:
                    print("An error occurred:", e)
    else:
        print(f"The directory '{source_directory_path}' does not exist.")

print("Process completed.")
