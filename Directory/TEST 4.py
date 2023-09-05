import os

# Get a list of files in a directory
file_list = os.listdir('C://Users//hagbi//Desktop//Coding//SoftwareDev//Uncle_Atif_Work_XP//Python//Automation//Directory')
print(file_list)
# Iterate through the files and check if they end with ".thr" and start with "ut"
for filename in file_list:
    if filename.endswith(".thr") and filename.startswith("ut"):
        print(f"{filename} meets the conditions.")
        
