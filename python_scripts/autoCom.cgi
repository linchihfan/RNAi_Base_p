#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

# This is a script that I attempted to qeury all the autocomplete query
# with just one file, but it didn't work, so I had to split up all the scripts

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    if form.getvalue('stable_id'):
        stid = form.getvalue('stable_id')
    if form.getvalue('gene_symbol'):
        gene_symbol = form.getvalue('gene_symbol')
    if form.getvalue('gene_id'):
        gene_id = form.getvalue('gene_id')
    if form.getvalue('entrez_id'):
        entrez_id = form.getvalue('entrez_id')
    if form.getvalue('author'):
        author = form.getvalue('author')
    if form.getvalue('screen_title'):
        screen_title = form.getvalue('screen_title')
    # Use your database login information here
    conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')
    cursor = conn.cursor()

    qry1 = """
            SELECT stable_id
            FROM  human_screens
            WHERE stable_id LIKE %s
            LIMIT 5
    """
    qry2 = """
            SELECT gene_symbol
            FROM  human_screen_data
            WHERE gene_symbol LIKE %s
            LIMIT 5
    """
    qry3 = """
            SELECT gene_id
            FROM  human_screen_data
            WHERE gene_id LIKE %s
            LIMIT 5
    """
    qry4 = """
            SELECT entrez_id
            FROM  human_screen_data
            WHERE entrez_id LIKE %s
            LIMIT 5
    """
    qry5 = """
            SELECT authors
            FROM  human_screens
            WHERE screen_title LIKE %s
            LIMIT 5
    """
    qry6 = """
            SELECT screen_title
            FROM  human_screens
            WHERE screen_title LIKE %s
            LIMIT 5
    """

    if stid:
        cursor.execute(qry1, ('%' + stid + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))
    if gene_symbol:
        cursor.execute(qry2, ('%' + gene_symbol + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))
    if gene_id:
        cursor.execute(qry3, ('%' + gene_id + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))
    if entrez_id:
        cursor.execute(qry4, ('%' + entrez_id + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))
    if author:
        cursor.execute(qry5, ('%' + author + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))
    if screen_title:
        cursor.execute(qry6, ('%' + screen_title + '%',))
        results = []
        for row in cursor:
            results.append({'label': row[0], 'value': row[0]})
        print(json.dumps(results))

    conn.close()

if __name__ == '__main__':
    main()
