
import sqlite3

def create_db():
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sentiment_results
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         url TEXT NOT NULL UNIQUE,
         bias REAL NOT NULL,
         political_leaning REAL NOT NULL,
         attitude REAL NOT NULL)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
