"""Query the database"""

import sqlite3



def query(specific_film=None):
    conn = sqlite3.connect("moviesDB.db")
    c = conn.cursor()
    if specific_film:
        c.execute("SELECT * FROM moviesDB WHERE Film=?", (specific_film,))
    else:
        c.execute("SELECT * FROM moviesDB LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows

def user_query():
    conn = sqlite3.connect("moviesDB.db")
    c = conn.cursor()
    
    # Fetch the user query
    user_input = input("Enter your SQL query: ")
    
    try:
        c.execute(user_input)
        conn.commit()
        # If the query was a SELECT, fetch and print results
        if user_input.strip().lower().startswith("select"):
            results = c.fetchall()
            for row in results:
                print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
    finally:
        conn.close()

    return results