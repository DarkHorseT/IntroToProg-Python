# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <LYencken>,<8/2/2020>, Added code for Assignment05
# -------------------------------------------------- #
from typing import TextIO

objFile = 'C:\_PythonClass\Assignment05\ToDoList.txt'
strchoice = ""
str_data = ""
dic_row = {}
lstfile = []
strlsit = ""
list_item = ''
list_cost = ""


#lstfile = 'C:\_PythonClass\Assignment05\ToDoList.txt'  # data storage file

#----processing----------------------------------------#


objFile = open("ToDoList.txt","r")
for row in objFile:
    str_data = row.split(",")               # Reads one row from the file and removes the commas
    dic_row = {"item " + list_item[0] + " cost " + list_cost[1].strip() + '\n'}
    lstfile.append(dic_row)
objFile.close()

#---- Menu List -----------------------------------------#


# Get user Input
while True:
    print("""
    Menu list
    1: Add Item
    2: Show Item
    3: Remove data
    4: Save to file
    5: Exit
    """)
    strChoice = str(input("please choose a option: "))





#--- Process the data -----------------------------------------#


    if (strChoice.strip() == '1'):
        # List to File
        print("-----------")
        print("Add to list")
        print("------------")
        #objFile = open(objFile, 'w')
        list_item = str(input("Add a item: "))
        list_cost = str(input("How much does it cost: "))
        dic_row = {"item " + list_item + " cost " + list_cost.strip() + '\n'}
        print(dic_row)

        continue


#-----display file -------------------------------------------------#

    elif (strChoice.strip() == '2'):
        # File to List
        print("--------------------")
        print("current data in file")
        print("--------------------")
        print(lstfile)

        continue

#--- remove item ---------------------------------------------------#

    elif (strChoice.strip() == '3'):
            str_data = open(objFile, "r")
            delete = input("type what you want removed: ")
            if delete in dic_row:
                del dic_row[delete]
                print("Removed")
            else:
                print(" ----------------")
                print("| Item not found | ")
                print(" ----------------")



            continue

#--- save to file ---------------------------------------------------#


    elif (strChoice.strip() == '4'):
        objFile = "C:\_PythonClass\Assignment05\ToDoList.txt"
        str_data = open(objFile, "w")
        str_data.write(list_item + ',' + list_cost + '\n')
        str_data.close()
        print('Saved')
        continue






#--- exit ------------------------------------------------------------#

    elif (strChoice.strip() == '5'):
        exit = input("press enter to exit:")
        if exit == "": break

    else:
        print("---------------")
        print("| Not a option |")
        print("----------------")