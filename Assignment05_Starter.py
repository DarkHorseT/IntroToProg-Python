# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <LYenckeb>,<8/2/2020>, Added code for Assignment05
# -------------------------------------------------- #
from typing import TextIO

datafile = 'C:\_PythonClass\Assignment05\ToDoList.txt'
strchoice = ""
str_data = ""
dic_row = {}
lstfile = []
strlsit = ""
list_item = ''
list_cost = ""


#lstfile = 'C:\_PythonClass\Assignment05\ToDoList.txt'  # data storage file

#----processing----------------------------------------#


data_file = open("ToDoList.txt","r")
for row in data_file:
    str_dataata = row.split(",")               # Reads one row from the file and removes the commas
    dic_row = {"item - " + list_item + " cost - " + list_cost + '\n'}
    lstfile.append(dic_row)
data_file.close()

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
        data_input = open(datafile, 'w')
        list_item = str(input("Add a item: "))
        list_cost = str(input("How much does it cost: "))
        dic_row = {"item", list_item, "cost", list_cost, '\n'}
        lstfile.append(dic_row)

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
        try:
            list_item = input("Item to Remove: ")

            #remove_item = open(datafile)
            for dic_row in lstfile:
                if dic_row["item"] == list_item:
                    str_data.remove(lstfile)
                    print(list_item, "item removed")
        except:
            print(" ----------------")
            print("| Item not found | ")
            print(" ----------------")

            continue

#--- save to file ---------------------------------------------------#


    elif (strChoice.strip() == '4'):
        savefile = open(datafile, "a")
        for dic_row in lstfile:
            savefile.write("item - " + list_item + " cost - " + list_cost + '\n')
        savefile.close()


        continue




#--- exit ------------------------------------------------------------#

    elif (strChoice.strip() == '5'):
        exit = input("press enter to exit:")
        if exit == "": break

    else:
        print("---------------")
        print("| Not a option |")
        print("----------------")