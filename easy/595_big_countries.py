# Write your MySql query statement below
import sqlite3

conn = sqlite3.connect('coutries.sqlite')
cur = conn.cursor()

# Make some fresh table using cur.executescript()
cur.executescript('''
DROP TABLE IF EXISTS World;

CREATE TABLE World (
    name  TEXT NOT NULL PRIMARY KEY UNIQUE,
    continent   TEXT,
    area    INTEGER,
    population  INTEGER,
    gdp INTEGER
)
''')
world = [ ('Afghanistan', 'Asia', 652230, 25500100, 20343000),
        ('Albania', 'Europe', 28748, 2831741, 12960000),
        ('Algeria', 'Africa', 2381741, 37100000, 188681000),
        ('Andorra', 'Europe', 468, 78115, 3712000 ),
        ('Angola', 'Africa', 1246700, 20609294, 100990000 )
        ]

for entry in world:
    cur.execute('''INSERT INTO World (name, continent, area, population, gdp)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( entry[0], entry[1], entry[2], entry[3], entry[4]) )

cur.execute('''SELECT name, population, area FROM World
        WHERE area > 3000000 or population > 25000000''')
print(cur.fetchall())
