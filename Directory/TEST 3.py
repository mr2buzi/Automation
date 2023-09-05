import os
import shutil
import datetime
from datetime import date

#defining variables
date = date.today()
part_1 = 'selfTest_MCU'
part_2 = 'Module_Report'
# this concatenates the beginning and end of the name
name = (part_1 + '_' + part_2) 
# this is the format of the filename
test_report = name + '_' + str(date) + '.txt' 

#This creates the file that we are going to write to and is named as test_report
with open ((test_report), 'w') as file:
    file.write("Any Text")


#Defining The Paths
#we are getting the current working directory and assigning it to variable
current_directory = os.getcwd() 
#printing to ensure the current working directory is correct
print("Current Directory:", current_directory) 
#here we are joining the current working directory with the filename
destination_file_path = os.path.join(current_directory, test_report) 
#This is where the files we want to write a report for are located
source_file_paths = ['C:\\Users\\hagbi\\Desktop\\Coding\\SoftwareDev\\Uncle_Atif_Work_XP\\Python\\Automation\\Directory\\Part_2',
                     'C:\\Users\\hagbi\\Desktop\\Coding\\SoftwareDev\\Uncle_Atif_Work_XP\\Python\\Automation\\Directory\\Part_1'
                     ] 

#Showing destination file path to ensure its the correct path
print("DestinatioN_file_path", destination_file_path)

#make the folder if it doesnt exist
for source_file_path in source_file_paths: 

    #using this your checking if source_file_path exists
    filename = os.path.isfile(source_file_path)
    

    # this code is checking the start and end of the filename, if its true it will run the following code below
    if filename.endswith('.txt') and filename.startswith('NTR'): 
        try:

            if not os.path.exists(destination_file_path):
                #if it doesnt exist make the directory
                os.makedirs(destination_file_path) 

             #Open the file and read it
            with open((source_file_path), 'r') as source_file: 
                #read the source_file contents and then store it in a variable
                file_contents = source_file.read() 


#Open the destination file and write the contents to the file
                with open ((destination_file_path), 'w') as destination_file: 
                    #we are storing the information in the file_contents variable
                    destination_file.write(file_contents)
                    #we are just copying the information with 2 placeholders (%s)
                    print("contents copied from '%s' to '%s' successfully" %(source_file_paths, destination_file_path)) 

#begins an exception handling bock for IOErros (input output errors)
        except IOError as e:
            #if the error number is 13 then print the error code
            if e.errno == 13: 
                print ("Permission Denied: Error 13")
            else:
                #e provides more information about the error
                print ("an error occured"), e 
        #catches more exceptions
        except Exception as e: 
                #prints it with more info
                print ("An error occured"), e 

    else:
        #or print this
        print ("the file doesnt start with UT") 
