#! python3
# linker.py - Creates and assigns folder based links to a csv file based on the contents of the file
# Specifically used for the MIPS Schematic drawing database by Chad Meadowcroft 2018

import pandas as pd
import math
import xlsxwriter   # To create linked xl file
import os.path      # Check for xls or csv versions
import pyperclip

# TODO: Add column titles to linked version

# request filepath from user
print('\n ##### - linker.py - ##### ')
print('\nThis is a tool to add file & folder hyperlinks to an excel database, \nit is set up for the MIPS drawings database at UKAEA but can be manually edited for any database\n')
print('Enter \'copy\' to take the root filepath from clipboard. \nEnter \'man\' to enter filepath manually')

select = input()

if select == 'copy':
    print('\nCopying now...\n')
    rootfolder = str(pyperclip.paste())
    print('Root folder copied: ' + rootfolder)
elif select == 'man':
    print('\nPlease provide a directory path: \n')
    rootfolder = input()
    print('Root folder entered: ' + rootfolder)

print('\nPlease name the excel database to be used. It must be .csv file, the extension does not need to be entered.')
print('Enter \'copy\' to take the excel workbook name from clipboard. \nEnter \'man\' to enter workbook name manually')

select = input()

if select == 'copy':
    print('\nCopying now...\n')
    filename = str(pyperclip.paste())
    print('Filename copied: ' + filename + '.csv')
elif select == 'man':
    print('\nPlease provide a directory path: \n')
    filename = input()
    print('filename entered: ' + filename + '.csv')

# TODO: Options to take xlsx and xls files instead of csv
#if os.path.isfile(filename + '.xlsx'):
#    wrkbook = pd.read_excel(filename + '.xlsx')
#elif os.path.isfile(filename + '.xls'):
#    wrkbook = pd.read_excel(filename + '.xls')

if os.path.isfile(filename + '.csv'):
   wrkbook = pd.read_csv(filename + '.csv')
else:
    print(filename + 'does not exist as csv in the current directory')

# Create filepath lists
system = []
subsystem = []
enclosure = []
subrack = []
name = []
dwg_no = []
CAD_name = []
sheet_no = []

linkedworkbook = xlsxwriter.Workbook(filename + '-linked.xlsx')   # Define new workbook for linked version
linkedworksheet = linkedworkbook.add_worksheet('sheet1')                # Define new worksheet
# TODO: Get original sheet name and use here

# Set all column widths (Chosen from original)
linkedworksheet.set_column('A:A', 9)
linkedworksheet.set_column('B:C', 40)
linkedworksheet.set_column('D:D', 13)
linkedworksheet.set_column('E:E', 100)
linkedworksheet.set_column('F:H', 18)
# TODO: Get column widths from original and use here

# Format new workbook
text_format = linkedworkbook.add_format({
    'bold':       1,
    'underline':  1,
    'font_size':  11,
})

# Create lists for each column with windows folder seperators included
for i in range(wrkbook.shape[0]):
    system.append(str(wrkbook.iloc[i, 0]))
    subsystem.append(str(wrkbook.iloc[i, 1]))
    enclosure.append(str(wrkbook.iloc[i, 2]))
    subrack.append(str(wrkbook.iloc[i, 3]))
    name.append(str(wrkbook.iloc[i, 4]))
    dwg_no.append(str(wrkbook.iloc[i, 5]))
    CAD_name.append(str(wrkbook.iloc[i, 6]))
    sheet_no.append(str(wrkbook.iloc[i, 7]))

    # Hyperlinking system -> subsystem -> enclosure -> subrack AND CAD_name for each level
    if system[i] != 'nan':
        folderpath = os.path.join(rootfolder, system[i])                            # Create folderpath var
        filepath = os.path.join(folderpath, CAD_name[i]) + '.DWG'
        cell = 'A' + str(i)                                                         # Define cell number
        linkedworksheet.write_url(cell, folderpath, string=system[i], tip=system[i])# Write hyperlink to cell
        if os.path.isfile(filepath):                     
            cell = 'G' + str(i)                                                         
            linkedworksheet.write_url(cell, filepath, string=CAD_name[i], tip=CAD_name[i])

        if subsystem[i] != 'nan':
            folderpath = os.path.join(rootfolder, system[i], subsystem[i])
            filepath = os.path.join(folderpath, CAD_name[i]) + '.DWG'
            cell = 'B' + str(i)
            linkedworksheet.write_url(cell, folderpath, string=subsystem[i], tip=subsystem[i])
            if os.path.isfile(filepath):                     
                cell = 'G' + str(i)                                                         
                linkedworksheet.write_url(cell, filepath, string=CAD_name[i], tip=CAD_name[i])

            if enclosure[i] != 'nan':
                folderpath = os.path.join(rootfolder, system[i], subsystem[i], enclosure[i])
                filepath = os.path.join(folderpath, CAD_name[i]) + '.DWG'
                cell = 'C' + str(i)
                linkedworksheet.write_url(cell, folderpath, string=enclosure[i], tip=enclosure[i])
                if os.path.isfile(filepath):                     
                    cell = 'G' + str(i)                                                         
                    linkedworksheet.write_url(cell, filepath, string=CAD_name[i], tip=CAD_name[i])

                if subrack[i] != 'nan':
                    folderpath = os.path.join(rootfolder, system[i], subsystem[i], enclosure[i], subrack[i])
                    filepath = os.path.join(folderpath, CAD_name[i]) + '.DWG'
                    cell = 'D' + str(i)
                    linkedworksheet.write_url(cell, folderpath, string=subrack[i], tip=subrack[i])
                    if os.path.isfile(filepath):                     
                        cell = 'G' + str(i)                                                         
                        linkedworksheet.write_url(cell, filepath, string=CAD_name[i], tip=CAD_name[i])

    # Write name, dwg_no, & sheet_no as strings
    if name[i] != 'nan':
        cell = 'E' + str(i)   
        linkedworksheet.write_string(cell, name[i])

    if dwg_no[i] != 'nan':
        cell = 'F' + str(i)   
        linkedworksheet.write_string(cell, dwg_no[i])

    if sheet_no[i] != 'nan':
        cell = 'H' + str(i)   
        linkedworksheet.write_string(cell, sheet_no[i])


linkedworkbook.close()  # Close workbook and end
print('Done')