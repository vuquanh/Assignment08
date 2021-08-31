#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AnhV, 2021-Aug-30, added code 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__ (self, id, title, artist):
        self.cd_id = int(id)
        self.cd_title = title
        self.cd_artist = artist

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    def save_inventory (self, file_name, lst_Inventory):
        objFile = open(file_name, 'w')
        for cd in lst_Inventory:
            datarow = '{},{},{}\n'.format(cd.cd_id, cd.cd_title, cd.cd_artist)
            objFile.write (datarow)
        objFile.close()

    def load_inventory(self, file_name):
        table = []
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            cd = CD(int(data[0]), data[1], data[2])
            table.append(cd)
        objFile.close()
        return table
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    def print_menu(self):
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    def menu_choice(self):
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    def show_inventory(self, table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print('{}\t{} (by:{})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))
        print('======================================')

    def userinput (self):
        """Function to ask user for input of new records
     
         Args:
             None.
     
         Returns:
             id: ID number for the new record
             title: Title name for new record 
             artist: Artist name of the new record 
        """
        id = input('Enter ID: ').strip()
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return id, title, artist
    
# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def additem (strID, strTitle, strArtist):
        """Function to add new data to the table
     
         Args:
             strID: ID number for the new record
             strTitle: Title of the new record
             stArtist: Artist name of the new record 
     
         Returns:
             None.
        """
        cd = CD(int(strID), strTitle, strArtist)
        lstOfCDObjects.append(cd)
    
    @staticmethod    
    def removeitem (intIDDel): 
        """Function to allow users to remove item from the table
     
         Args:
             intIDdel: the ID number of the record user want to delete
     
         Returns:
             None.
        """
        intRowNr = -1
        blnCDRemoved = False
        for cd in lstOfCDObjects:
            intRowNr += 1
            if cd.cd_id == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')


# -- Main Body of Script -- #
ioObj = IO()
fileIOObj = FileIO()

while True:
    # 2.1 Display Menu to user and get choice
    ioObj.print_menu()
    strChoice = ioObj.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = fileIOObj.load_inventory(strFileName)
            ioObj.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            ioObj.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # 3.3 process add a CD
    elif strChoice == 'a':
        strID, strTitle, stArtist = ioObj.userinput()
        DataProcessor.additem(strID, strTitle, stArtist)
        ioObj.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        ioObj.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.5 process delete a CD
    elif strChoice == 'd':
        ioObj.show_inventory(lstOfCDObjects)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        DataProcessor.removeitem (intIDDel) 
        ioObj.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # 3.6 process save inventory to file
    elif strChoice == 's':
        ioObj.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            fileIOObj.save_inventory (strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')   
        continue  # start loop back at top.
        
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

