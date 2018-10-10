#! python 3
# caps.py - Capitalise all file names within a folder
# Chad Meadowcroft 2018

import os, sys, pyperclip

# request filepath from user
print('\n ##### - caps.py - ##### ')
print('\nThis is an automatic filename capitalising tool, \nit will capitalise the names of all files in the specified folder.\n')
print('Enter \'copy\' to take filepath from clipboard. \nEnter \'man\' to enter filepath manually')

select = input()

if select == 'copy':
    print('\nCopying now...\n')
    path = str(pyperclip.paste())
    print('Filepath copied: ' + path)
elif select == 'man':
    print('\nPlease provide a directory path: \n')
    path = input()
    print('Path entered: ' + path)


# loop through all folders in path
if os.path.isdir(path):
    for folder in os.listdir(path):
        folderpath = os.path.join(str(path), str(folder))

        # subfolder
        if os.path.isdir(folderpath):
            for subfolder in os.listdir(folderpath):
                subfolderpath = os.path.join(str(folderpath), str(subfolder))
                
                # subsubfolder
                if os.path.isdir(subfolderpath):
                    #print(os.listdir(subfolderpath))
                    for subsubfolder in os.listdir(subfolderpath):
                        subsubfolderpath = os.path.join(str(subfolderpath), str(subsubfolder))

                        #if os.path.isdir(subsubfolderpath):
                            #print(os.listdir(subsubfolderpath))

                        if os.path.isfile(subsubfolderpath):
                            #print(subsubfolderpath)
                            os.rename(subsubfolderpath, subsubfolderpath.upper())
                        
                elif os.path.isfile(subfolderpath):
                    #print(subfolderpath)
                    os.rename(subfolderpath, subfolderpath.upper())

        elif os.path.isfile(folderpath):
            #print(folderpath)
            os.rename(folderpath, folderpath.upper())

    print('\nProcess complete, please check files.\n')
elif os.path.isfile(path):
    print('ERROR: The path you entered is to a file')
else: 
    print('ERROR: Invalid folder path')    



# manage exceptions

# Implement reversal option to revert to original names