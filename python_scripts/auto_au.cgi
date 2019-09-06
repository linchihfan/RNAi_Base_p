#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    # Get the term value from jquery autocomplete
    if form.getvalue('term'):
        term = form.getvalue('term')

    # Connect to MySQL server
    # Use your database login information here
    conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')
    cursor = conn.cursor()

    # Query for the autocomplete
    qry = """
            SELECT DISTINCT authors
            FROM  human_screens
            WHERE authors LIKE %s
            LIMIT 5
    """
    # Execute the qry
    cursor.execute(qry, ('%' + term + '%',))
    results = []
    # Append the results in a json format
    for row in cursor:
        results.append({'label': row[0], 'value': row[0]})

    # Clean up connection
    conn.close()
    # Print out the json to autocomplete
    print(json.dumps(results))
if __name__ == '__main__':
    main()
