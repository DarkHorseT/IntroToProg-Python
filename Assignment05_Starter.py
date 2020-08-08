# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <LYenckeb>,<8/2/2020>, Added read/write to file code
# -------------------------------------------------- #

# Declare my variables
# Declare my variables
strChoice = '' # User input
lstRow = []  # list of data
strFile = 'ToDoList.txt'  # data storage file
objFile = None  # file handle


# Get user Input
while(True):
    print("type either" '\n' "w: (write)" '\n' "r: (read)" '\n' "type exit to leave")
    strChoice = input("Choose to [w]rite or [r]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        # List to File
        objFile = open(strFile, "a+")
        lstRow = input("Add a item: ")
        objFile.write(lstRow[:] + " | ")
        lstRow = input("How much does it cost: ")
        objFile.write(lstRow[:] + '\n')
        objFile.close()
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row
            print(lstRow[:].split())
        objFile.close()
    else:
        print('Please choose either w or r!')