#!/usr/local/bin/python3

import jinja2
import re
import mysql.connector
import cgi

# Look for template file
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

# Creates the environemtn and load the template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('template.html')

# Import user input from html form
form = cgi.FieldStorage()

# Check the species from user input
species = form.getfirst('species')
# Store user input into a list
input = []
input.append(form.getfirst('gene_symbol'))
input.append(form.getfirst('gene_id'))
input.append(form.getfirst('entrez_id'))
input.append(form.getfirst('author'))
input.append(form.getfirst('screen_title'))
input.append(form.getfirst('stable_id'))

# Added '%' to fit the SQL query snytax
for i in range(len(input)):
    if input[i]:
        input[i] = '%' + input[i] + '%'
    else:
        input[i] = '%'


# Connect to mySQL server
# Use your database login information here
conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')

# Initiate cursor object
cur = conn.cursor()

# The SQL query
fly_qry = """
        SELECT s.stable_id, s.screen_title, s.authors, s.pubmed_id, s.organism, m.gene_id, m.entrez_id, m.gene_symbol, s.reagent_type, m.phenotype
        FROM  fly_screens s
        JOIN fly_screen_data m ON s.id = m.screen_id
        WHERE m.gene_symbol LIKE %s
        AND m.gene_id LIKE %s
        AND m.entrez_id LIKE %s
        AND s.authors LIKE %s
        AND s.screen_title LIKE %s
        AND s.stable_id LIKE %s
    """
human_qry = """
        SELECT s.stable_id, s.screen_title, s.authors, s.pubmed_id, s.organism, m.gene_id, m.entrez_id, m.gene_symbol, s.reagent_type, m.phenotype
        FROM  human_screens s
        JOIN human_screen_data m ON s.id = m.screen_id
        WHERE m.gene_symbol LIKE %s
        AND m.gene_id LIKE %s
        AND m.entrez_id LIKE %s
        AND s.authors LIKE %s
        AND s.screen_title LIKE %s
        AND s.stable_id LIKE %s
"""

# Initiate output list
st_id = list()
stitle = list()
auth = list()
pub = list()
org = list()
geneid = list()
entid = list()
genesym = list()
reagent = list()
phenotype = list()
# Store ouput function
def store_output(cursor):
    for (stid, st, au, pu, og, gid, ent, gs, re, ph) in cursor:
        st_id.append(stid)
        stitle.append(st)
        auth.append(au)
        pub.append(pu)
        org.append(og)
        geneid.append(gid)
        entid.append(ent)
        genesym.append(gs)
        reagent.append(re)
        phenotype.append(ph)

# Placeholder to prevent SQL injection
# Execute the SQL query dpending on the species
if species == 'Human':
    cur.execute(human_qry, (input))
    store_output(cur)
elif species =='Drosophila':
    cur.execute(fly_qry, (input))
    store_output(cur)
else:
    cur.execute(human_qry, (input))
    store_output(cur)
    cur.execute(fly_qry, (input))
    store_output(cur)

# Clean up connection
conn.close()

print("Content-Type: text/html\n\n")
print(template.render(stid=st_id, screent=stitle, author=auth, pubmed=pub, orga=org, geid=geneid, ent_id=entid, gene_sym=genesym, retype=reagent, pheno=phenotype))

