#!/usr/bin/python3

import mysql.connector
import csv


def main():
    # Initiate i so I can keep track of how many qry has been sent
    i = 0
    # Connect to MySQL server
    # Use your database login information here
    conn = mysql.connector.connect(user='USER-NAME', password='PASSWORD', host='localhost', database='DATABASE')
    cursor = conn.cursor()

    # Start reading the tsv file with csv module using tab as delimiter
    with open('./data/human_data.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        # Execute the query for each row
        for row in reader:

            qry = """
                    INSERT INTO screen_data (screen_id, stable_id, entrez_id, gene_id, gene_symbol, reagent_id, score, phenotype, conditions, follow_up,comment)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(qry, (row))
            # Print i every 100k data entered
            i += 1
            if i % 100000 == 0:
                print(i)
    conn.close()

    print('Done!')


if __name__ == '__main__':
    main()
