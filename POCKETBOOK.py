print("Made for HackTheLib 2020. Pocketbook V 1.10\n")
print("Welcome to Pocketbook. Type FILES to find files, EDIT to edit files, DEL to delete files, QUIT to quit the program or NEW for a new file\n")
Log = {"Example Text": "Hello, World!", "System info": "Version 1.0, Preview edition. For More Version info, go to the devpost page. ", "Credits": "Made By Rishi Suresh for Hack the Lib 2020"}
import time
from datetime import date
today = date.today()
print("Today's date:", today)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("The time which this program started was " + current_time)

while True:
    Data = input()
    if Data == ("FILES"): 
        print ("Here are the names of the files stored on this program. \n")
        del Data
        for x in Log:
            print(x)
    elif Data == ("NEW"):
        print("Please name the file")
        del Data
        Data = input()
        Log[Data] = ""
        print("The File is Called " + Data + ". Type EDIT to edit the file contents.") 
    elif Data == ("EDIT"):
        print ("Enter the file's name that you would like to edit")
        filename = input()
        if filename in Log:
            print ("Enter the new file contents")
            contents = input()
            Log[filename] = contents
            print("Final files and their contents")
            print(Log)
        elif filename not in Log:
            print("There is no file called " + filename + ". Please create a new file, or retype the file name in the system.")
            del filename
    elif Data == ("DEL"):
        print("Type the filename you would like to delete")
        Filename2 = input()
        del Log[Filename2]
        print("File Deleted Successfuly.")
    elif Data == "QUIT":
        quit()