import unittest
import sqlite3
from mylib.query import query, user_query

class TestDatabaseFunctions(unittest.TestCase):

    def test_query(self):
        conn = sqlite3.connect("moviesDB.db")
        c = conn.cursor()
        c.execute("INSERT INTO moviesDB (Film, Year) VALUES (?, ?)", ("Test Movie", 2020))
        conn.commit()
        conn.close()

        result = query("Test Movie")
        self.assertEqual(result[0][0], "Test Movie")

    def test_user_query(self):
        conn = sqlite3.connect("moviesDB.db")
        c = conn.cursor()
        c.execute("INSERT INTO moviesDB (Film, Year) VALUES (?, ?)", ("Test Movie 2", 2021))
        conn.commit()
        conn.close()

        def mock_input(prompt):
            return "SELECT * FROM moviesDB WHERE Film='Test Movie 2'"

        # Mock the input function so it returns our test query
        user_query.__globals__['input'] = mock_input
        result = user_query()
        self.assertEqual(result[0][0], "Test Movie 2")

    def tearDown(self):
        conn = sqlite3.connect("moviesDB.db")
        c = conn.cursor()
        c.execute("DELETE FROM moviesDB WHERE Film='Test Movie'")
        c.execute("DELETE FROM moviesDB WHERE Film='Test Movie 2'")
        conn.commit()
        conn.close()

if __name__ == "__main__":
    unittest.main()
