#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:35:43 2020

@author: chelsea
"""

'''merge two CSV files using the UniprotID as the unique index

    Requirement:  - All IDs in File1 is in File2
                  - the name of the column that holds the IDs is UniProt_ID
'''


'''
Returns a dictionary of the data stored in a specific file. The key will be the
data that is stored in the specified Column. Column must be a fieldname


input:
    
    CSVFile: pass the reader of the name of the csv file  you want to analyze. 
    Type -> string
    
    Column: A string of the fieldname for the column that holds the data you want 
    the information to map to
   
    Skip1stLine: There is a defualt value called, Skip1stLine, which when true will return a list 
    with a place holder in the list. This accounts for the first line of the csv file 
    which gives the title of the info
    
    
    got Idea for this from https://stackoverflow.com/questions/2081836/reading-specific-lines-only
    specifically the enumerate(file). made my own version of this
    
    '''

def DictConvert(CSVFile, Column, Skip1stLine = True):
    Dict = {}   
    with open(CSVFile) as File:
        Reader= csv.DictReader(File)
        for row in Reader:
            NumberOfInvalidFields = 0 #Incase there is a field of an empyt string 
            key = row[Column]
            val = {}
            for field in Reader.fieldnames:
                if field: #checks if field is valid, not empty string
                    if field == Column:
                        continue
                    else:
                        val[field] = row[field]
                
                #keeps track of any invalid fields
                else: 
                    NumberOfInvalidFields = NumberOfInvalidFields +1
                    
                Dict[key] = val
                Fields= list(Reader.fieldnames)
                Fields.remove(Column)
                
                #removes invalid pairs. This is skiped if there isn't any 
                #i.e. NumberOfInvalidFields = 0
                for i in range(0,NumberOfInvalidFields):
                    Fields.remove("") 
                
                
                    
            
    File.close()
    return Dict, Fields

    
            
'''Defining my own exception for when the files don't have the 
same IDs'''
class InputError(Exception):
    def __init__(self, message):
        self.message = message
        
    
        

import csv
with open('MergedCSVFile.csv', 'w') as MergedFile:
    
    #FileOneIDs = List_of_IDs('Proteins_MS_mock.csv', 'UniProt_ID')
    Data1, Fields1 = DictConvert('CompiledData.csv', 'UniProt_ID')
    Data2, Fields2 = DictConvert('Proteins_MS_mock.csv', 'UniProt_ID')
    
    fieldnamesMerged = ['UniProt_ID'] + Fields1 + Fields2
    MergedWriter = csv.DictWriter(MergedFile, fieldnames=fieldnamesMerged)
    MergedWriter.writeheader()
    
    for Key1 in Data1.keys():
            if Key1 in Data2.keys():
                Data1[Key1].update(Data2[Key1])
                del Data2[Key1]
                
                LineToWrite = {'UniProt_ID' : Key1}
                LineToWrite.update(Data1[Key1])
                
                MergedWriter.writerow(LineToWrite)
            else:
                raise InputError("Files do not contain the same IDs")
                
    if Data2 != {}:
        raise InputError("Files do not contain the same IDs")
        
        
        
'''
Returns a list of all the data stored in a specific column in the order that 
they appear in the file. Where the index of the file correlates to the row 
that the ID is in in the file of interest

input:
    
    CSVFile: pass the reader of the name of the csv file  you want to analyze. 
    Type -> string
    
    Column: A string of the fieldname for the column that holds the IDs
   
    Skip1stLine: There is a defualt value called, Skip1stLine, which when true will return a list 
    with a place holder in the list. This accounts for the first line of the csv file 
    which gives the title of the info
    
    
    MIGHT BE USEFUL FOR BIGGER FILES
    
    '''
    
def List_of_IDs(CSVFile, Column, Skip1stLine = True ):
    if Skip1stLine:
        ListData = ["PlaceHolder"]   
    else:
        ListData = ["PlaceHolder"]
        
    with open(CSVFile) as File:
        Reader= csv.DictReader(File)
        for row in Reader:
            ListData = ListData + [row[Column]]
    File.close()
    return(ListData)
        
                


    
    