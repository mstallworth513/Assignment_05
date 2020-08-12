#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: MStallworth, 2020-Aug-10, Added script loading inventory from file, adding data, displaying data, deleting data, and saving inventory
# DBiesinger, 2030-Jan-01, Created File. MStallworth, 2020-Aug-10, Appended file
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []
# replace list of lists with list of dicts
dicRow = {}  # list of data row
dicRow1 = {'id': 1, 'cd': 'The Big Wheel', 'artist': 'Runrig'}
dicRow2 = {'id': 2, 'cd': 'Bad', 'artist': 'Michael Jackson'}
lstTbl.append(dicRow1)
lstTbl.append(dicRow2)
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        print('Goodbye.')
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        lstTbl.clear() # clear the data from the memory
        objFile = open(strFileName, 'r') # open the saved file
        for row in objFile: # go through every line in file
            lstRow = row.strip().split(',') # ignore blank lines and seperate data with comma
            dicRow = {'id': lstRow[0], 'cd': lstRow[1], 'artist': lstRow[2]} # Place all data from file into a dictionary
            lstTbl.append(dicRow) # place data from file into the cleared 2d list
        objFile.close()
        print('The data from your file has been successfully loaded to memory. Use choice "i" to check for your data.', '\n')

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ') # Create variable names for all parts of data
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID) # convert ID into an integer 
        dicRow = {'id': intID, 'cd': strTitle, 'artist': strArtist} # format how user data is added into 2d list
        lstTbl.append(dicRow) # add user data into in memory user 2d list
        print()
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl: # unpack the 2d list
            print(*row.values(), sep = ', ')
        print()
   
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        print('The entries in this inventory are numbered in rows starting from 0', '\n')
        print('Row # = id - 1', '\n')
        for row in lstTbl: # unpack 2d list and print
            print(*row.values(), sep = ', ')
        delUserInput = int(input('Enter row # of the entry you would like to remove:')) # allow user to choose row # they want to delete
        print()
        print('You have chosen to delete row:', delUserInput) # show user which option they chose
        lstTbl.pop(delUserInput) # remove data with row # the user entered 
        print()
        print('Your inventory is now:', '\n')
        for row in lstTbl: # reprint data with the entry now removed 
            print(*row.values(), sep = ', ')
        print()
        print('If you deleted this option by mistake reload your data with option "l."', '\n')
        

    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') # open file and overwrite data
        for row in lstTbl:
            strRow = ''
            for item in row.values(): # unpack dictionary values
                strRow += str(item) + ',' # store data into variable 
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow) # write stored values into file
        objFile.close()
        print()
    else:
        print('Please choose either l, a, i, d, s or x!')

