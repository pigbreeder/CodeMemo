import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("""create table jp2cn
                (id INTEGER primary key  AUTOINCREMENT,
                jp TEXT  UNIQ NOT NULL,
                cn TEXT NOT NULL,
                UNIQUE(jp, cn))""")