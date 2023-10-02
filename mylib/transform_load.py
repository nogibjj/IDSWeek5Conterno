"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,
avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/IDSWeek5Conterno/data/movies.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('moviesDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS moviesDB")
    c.execute("""CREATE TABLE moviesDB (
                Film TEXT, 
                Genre TEXT, 
                Lead_Studio TEXT, 
                Audience_score INTEGER,
                Profitability REAL,
                Rotten_Tomatoes INTEGER,
                Worldwide_Gross TEXT,
                Year INTEGER)""")
    #insert
    next(payload)
    c.executemany("INSERT INTO moviesDB VALUES (?,?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "moviesDB.db"

