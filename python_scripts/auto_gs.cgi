#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

# Similar script as auto_au.cgi

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    if form.getvalue('term'):
        term = form.getvalue('term')

    # Use your database login information here
    conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')
    cursor = conn.cursor()

    qry2 = """
            SELECT DISTINCT gene_symbol
            FROM  human_screen_data
            WHERE gene_symbol LIKE %s
            LIMIT 5
    """

    cursor.execute(qry2, ('%' + term + '%',))
    results = []
    for row in cursor:
        results.append({'label': row[0], 'value': row[0]})

    conn.close()
    print(json.dumps(results))
if __name__ == '__main__':
    main()
