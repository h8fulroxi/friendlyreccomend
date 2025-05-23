# i swear to god this was the only way i could get it to work UGHHGHHHHFBGFHBGSVJHVGEFGHGG
# RUN THIS BEFORE RUNNING MOVIE SEARCH!!!! IT CREATES THE TABLE
# I COULDNT GET THE TABLES WORKING ANY OTHER WAY AT LEAST ON MY END
# THERE WAS LITERALLY NO RESULTS ON THIS ERROR SO IMMA CHALK IT UP TO THE GAME

import sqlite3

conn = sqlite3.connect('media.db')
c = conn.cursor()

# media table :P
c.execute('''CREATE TABLE IF NOT EXISTS Media
             (id INTEGER PRIMARY KEY,
              title TEXT NOT NULL,
              genre TEXT,
              year INTEGER,
              director TEXT,
              studio TEXT,
              age_rating TEXT,
              platform TEXT DEFAULT 'Unknown',
              length INTEGER DEFAULT 0)''')

# reviews tabel
c.execute('''CREATE TABLE IF NOT EXISTS Reviews
             (media_id INTEGER,
              review TEXT,
              FOREIGN KEY(media_id) REFERENCES Media(id))''')

# base data (ive likely added more than this in tha actual file but this is where it all started)
movies = [
    ('Spider-Man: Homecoming', 'Superhero', 2017, 'Jon Watts', 'Marvel Studios', 'PG-13'),
    ('Puss in Boots: The Last Wish', 'Animated', 2022, 'Joel Crawford', 'DreamWorks', 'PG'),
    ('Baby Driver', 'Action', 2017, 'Edgar Wright', 'Big Talk Productions', 'R'),
    ('Deadpool', 'Action/Comedy', 2016, 'Tim Miller', '20th Century Fox', 'R')
    ('Sinners', 'Horror', 2025, 'Ryan Coogler', 'Warner Bros. Pictures', 'R')
]

c.executemany('''INSERT INTO Media
              (title, genre, year, director, studio, age_rating)
              VALUES (?,?,?,?,?,?)''', movies)

conn.commit()
conn.close()
print("just reassurance that it did the thing its supposed to")