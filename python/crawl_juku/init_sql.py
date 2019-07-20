import sqlite3
sql_file = 'test.db'
conn = sqlite3.connect(sql_file)
cur = conn.cursor()
cur.execute("""create table jp2cn
                (id INTEGER primary key  AUTOINCREMENT,
                jp TEXT  UNIQ NOT NULL,
                cn TEXT NOT NULL,
                UNIQUE(jp, cn))""")