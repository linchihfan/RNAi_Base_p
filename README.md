# RNAi Database

A web page data mining tool for Human and Drosophila melanogaster RNAi.




# Demo:
![](demo.gif)

# Requirement

JQuery Supported Browsers:

Internet Explorer: 9+
Chrome, Edge, Firefox, Safari: Current and Current - 1
Opera: Current
Safari Mobile iOS: 7+
Android 4.0+

# Detailed Usage

1. Pick a species or pick both

2. Type in your search keyword in the fields

3. Submit!

# Implementation

1. Separate the meta data and the actual data from the raw data. This was simply done with the a python script

2. Created MySQL tables that was mentioned in the proposal. However, I separated the species to avoid screen_id duplicates between species.

3. Utilized python_scripts/parese_tsv.py and python_scripts/parse_mete.py to import the data to MySQL server

4. rnai_qry.cgi looks for user input from search.html, and execute SQL query then return the data to templates/template.html


# Data Source

Data Provided by http://www.genomernai.org/

GenomeRNAi: a database for cell-based and in vivo RNAi phenotypes, 2013 update.
Schmidt EE, Pelz O, Buhlmann S, Kerr G, Horn T, Boutros M.
Nucleic Acids Res. 2013 Jan 1;41(D1):D1021-6. doi: 10.1093/nar/gks1170. Epub 2012 Nov 27.

GenomeRNAi: a database for cell-based RNAi phenotypes. 2009 update.
Gilsdorf M, Horn T, Arziman Z, Pelz O, Kiner E, Boutros M.
Nucleic Acids Res. 2010 Jan;38(Database issue):D448-52. Epub 2009 Nov 12.

GenomeRNAi: a database for cell-based RNAi phenotypes.
Horn T, Arziman Z, Berger J, Boutros M.
Nucleic Acids Res. 2007 Jan;35(Database issue):D492-7. Epub 2006 Nov 28.

The landing page background video:
https://www.youtube.com/watch?v=cK-OGB1_ELE

The interactable result table was implemented with DataTables:
https://datatables.net/
