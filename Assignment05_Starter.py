# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <LYencken>,<8/2/2020>, Added code for Assignment05
# -------------------------------------------------- #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dic_row = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = "C:\_PythonClass\Assignment05\ToDoList.txt"
strData = open(objFile, "r+")
for row in strData:
    lstTable = row.splitlines()
    dic_row = ({lstTable[0]: lstTable[1].strip()})
    lstTable.append(dic_row)
strData.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):

    print("""
    Menu of Options
    1) Add a new item.
    2) Show Data
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Select menu option: "))
    print()



    #--- new list ----------------------------------------#
    if (strChoice.strip() == '1'):
        print("enter item and cost of item")
        listitem = str(input("item: "))
        listcost = str(input("cost: "))
        dicRow = {listitem: listcost.strip()}
        print(dic_row)
        continue

    # --- read file ----------------------------------------#
    elif (strChoice.strip() == "2"):
        print("current data")
        print(dicRow)

    # --- remove item ----------------------------------------#

    elif (strChoice.strip() == '3'):

        objFile = "C:\_PythonClass\Assignment05\ToDoList.txt"
        strData = open(objFile, "r")
        dic_row = {row.split(",")[0]: row.split(",")[1].strip() for row in strData}
        print("Task and Priority\n", dic_row)
        item_delete = input("What item do you want me to remove?: ")
        if item_delete in dic_row:
            del dic_row[item_delete]
            print(item_delete, " deleted")
        else:
            print("Does not exist in list")

        continue

    # --- save file ----------------------------------------#
    elif (strChoice.strip() == '4'):
        objFile = "C:\_PythonClass\Assignment05\ToDoList.txt"
        strData = open(objFile, "a")
        strData.write(listitem + ',' + listcost + '\n')
        strData.close()
        print('Save to File')
        continue

    #--- exit list ----------------------------------------#
    elif (strChoice.strip() == '5'):
        leave = input("Press enter to exit: ")
        exit()