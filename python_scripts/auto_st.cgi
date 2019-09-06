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

    qry = """
            SELECT DISTINCT screen_title
            FROM  human_screens
            WHERE screen_title LIKE %s
            LIMIT 5
    """

    cursor.execute(qry, ('%' + term + '%',))
    results = []
    for row in cursor:
        results.append({'label': row[0], 'value': row[0]})

    conn.close()
    print(json.dumps(results))
if __name__ == '__main__':
    main()
