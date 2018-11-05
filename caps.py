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
            for sub1folder in os.listdir(folderpath):
                sub1folderpath = os.path.join(str(folderpath), str(sub1folder))
                
                # subsubfolder
                if os.path.isdir(sub1folderpath):
                    #print(os.listdir(sub1folderpath))
                    for sub2folder in os.listdir(sub1folderpath):
                        sub2folderpath = os.path.join(str(sub1folderpath), str(sub2folder))

                        # subsubsubfolder
                        if os.path.isdir(sub2folderpath):
                            #print(os.listdir(sub2folderpath))
                            for sub3folder in os.listdir(sub2folderpath):
                                sub3folderpath = os.path.join(str(sub2folderpath), str(sub3folder))

                                # subsubsubsubfolder
                                if os.path.isdir(sub3folderpath):
                                    for sub4folder in os.listdir(sub3folderpath):
                                        sub4folderpath = os.path.join(str(sub3folderpath), str(sub4folder))

                                        # subsubsubsubsubfolder
                                        if os.path.isdir(sub4folderpath):
                                            for sub5folder in os.listdir(sub4folderpath):
                                                sub5folderpath = os.path.join(str(sub4folderpath), str(sub5folder))
                                        
                                        elif os.path.isfile(sub4folderpath):
                                            os.rename(sub4folderpath, sub4folderpath.upper())


                                elif os.path.isfile(sub3folderpath):
                                    os.rename(sub3folderpath, sub3folderpath.upper())

                        elif os.path.isfile(sub2folderpath):
                            #print(subsubfolderpath)
                            os.rename(sub2folderpath, sub2folderpath.upper())
                        
                elif os.path.isfile(sub1folderpath):
                    #print(subfolderpath)
                    os.rename(sub1folderpath, sub1folderpath.upper())

        elif os.path.isfile(folderpath):
            #print(folderpath)
            os.rename(folderpath, folderpath.upper())

    print('\nProcess complete, please check files.\n')
elif os.path.isfile(path):
    print('ERROR: The path you entered is to a file')
else: 
    print('ERROR: Invalid folder path')    

# -- TO DO: --

# Implement improved version using os.walk()

# manage exceptions

# Implement reversal option to revert to original names