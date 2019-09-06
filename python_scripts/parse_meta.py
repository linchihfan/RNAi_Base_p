#!/usr/bin/python3

import re
import mysql.connector
import csv


def main():

    # Use your database login information here
    conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')
    cursor = conn.cursor()
    row = []
    for line in open('./data/fly_meta.txt'):
        if len(row) == 19:
            qry = """
                    INSERT INTO fly_screens (stable_id, screen_title, publication_title, authors, publication_year, pubmed_id, organism, screen_type, biosource, biomodel, assay, method, library_manufacturer, library, scope, reagent_type, score_type, cutoff, notes)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            cursor.execute(qry, (row))
            row = []
            continue
        m = re.search(r'.+=(.*)', line)
        if m:
            row.append(m.group(1))

    conn.close()

    print('Done!')


if __name__ == '__main__':
    main()
