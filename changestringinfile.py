import shutil
import datetime
import os

source_file = "\\path\\to\\text\\file\\"

def create_backup(filepath):
    todays_date = datetime.datetime.now() #Get today's date
    stripped_time = todays_date.strftime('%Y%m%d') #Strip time off of todays_date   
    shutil.copyfile(source_file, "\\path\\to\\backup\\folder\\device_" + str(stripped_time) + ".txt") #Moves file from source folder to backup folder and appends the stripped date to the end of the file
    print("device.txt has been copied, renamed to device_" + stripped_time + ".txt, and moved to the backup folder.")

def replace_pc_id(filepath):
    original_id = input("What PC ID are you needing to replace?")
    new_id = input("What is the new PC ID?")
    with open(filepath, 'r+') as devicetxt: #Opens up the file
        file_content = devicetxt.read() #Loads the file into memory
        if original_id in file_content:
            print("Found " + original_id + " in device.txt, " + original_id + " will be replaced with " + new_id)
            file_content = file_content.replace(original_id, new_id) #Switches the original_id with the new_id at this step
            devicetxt.truncate(0) #Clears contents of the file before writeback
            devicetxt.seek(0) #Sets the file's current position back to 0
            devicetxt.write(file_content) #Write's back to the file
        else:
            print("Unable to find existing PC ID, please make sure the PC ID is in the file.")

def main():
    create_backup(source_file)
    replace_pc_id(source_file)

if __name__ == '__main__':
    main()