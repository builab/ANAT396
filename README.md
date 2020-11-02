# ANAT396

**Goal of Project**

Given a list of Uniprot protein IDs this code will find the protein name, Uniprot ID, gene name, InterPro ID, OrtoDB ID and number of amino acids.

**How it works**

The code requires that the list of Uniprot protein IDs is in a CSV file, where each ID is on a new line. Example is the Proteins.csv file. The CSV file with the IDs must be called Proteins.csv, as ProcessingProteins.py will read this file. The ProcessingProteins.py will loop through every ID and search it in Uniprot. The Uniprot page is then saved into result.xml, which the information of interest is extracted from. The information is then written into the CompiledData.csv file, which will store the protein name, Uniprot ID, gene name, InterPro ID, OrtoDB ID and number of amino acids. The CSVtoHtml.py file is then runned. This file will write a html file that will be used to display the information, DisplayData.html. The style.css describes how the html file will be displayed to the screen. The script.js is the file that contains the JavaScript which makes the data searchable.

**How to run it**

1.Run ProcessingProteins.py
2.Run CSVtoHtml.py
3.Open DisplayData.html is a browser




