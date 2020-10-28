#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:12:33 2020

@author: chelsea
"""
import csv

with open('DisplayData.html', 'w') as htmlFile, open("CompiledData.csv", "r") as dataFile:
    
    HtmlStart = ["<!DOCTYPE html> \n", "<html>\n"] 
    htmlFile.writelines(HtmlStart)
    data = csv.reader(dataFile, delimiter=',')
    
    Head = ["<head>\n",
            "<title> Protein information</title>\n",
            "<meta charset=\"UTF-8\">\n",
            "<link rel=\"stylesheet\" href=\"style.css\">\n",
            "</head>\n"]
    htmlFile.writelines(Head)
   
    #for row in data:
        #print(row)
    
    Table = ["<body>\n", "<table>\n<thead>\n<tr>\n"]
    htmlFile.writelines(Table)
        
    dataDict = csv.DictReader(dataFile)

   
  
    for fieldname in dataDict.fieldnames:
        htmlFile.write("<th>"+fieldname+"</th>\n")
    
    htmlFile.write("</tr>\n</thead>\n<tbody>\n")
    
    line = 0
    for row in dataDict:
        if line!=0 :
            htmlFile.write("<tr>\n")
            for fieldname in dataDict.fieldnames:
                htmlFile.write("<td>" + row[fieldname]+"</td>\n")
            htmlFile.write("</tr>\n")      
        line=line+1

    htmlFile.write("</tbody>\n</table>\n</body>\n</html>")
    
    
        
    

    
    
    htmlFile.close()
    dataFile.close()


