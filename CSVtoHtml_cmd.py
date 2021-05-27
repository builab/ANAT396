#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:12:33 2020

Convert CSV to Html
Syntax: CSVtoHtml_cmd.py --i input.csv --o display.html

@author: chelsea
"""
import csv, argparse

parser = argparse.ArgumentParser(description='Convert CSV to Html file')
parser.add_argument('--i', '-input', help='Input CSV file 1',required=True)
parser.add_argument('--o', '-output', help='Output Html file',required=True)

args = parser.parse_args()

with open(args.o, 'w') as htmlFile, open(args.i, "r") as dataFile:
	
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
	Body = ["<body>\n",
			"<div class=\"search-app\">\n",
			"<h1>Search Proteins</h1>",
			"<div id=\"search\"></div>\n",
			"<table id=\"protein_information\">\n<thead>\n<tr>\n"]

	htmlFile.writelines(Body)
		
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

	Closing = ["</tbody>\n",
			   "</table>\n<",
			   "</div>\n",
			   "<script src=\"script.js\"></script>\n",
			   "</body>\n",
			   "</html>"
			   ]
	htmlFile.writelines(Closing)
	
	
	htmlFile.close()
	dataFile.close()


