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
    ('Deadpool', 'Action/Comedy', 2016, 'Tim Miller', '20th Century Fox', 'R'),
    ('Sinners', 'Horror', 2025, 'Ryan Coogler', 'Warner Bros. Pictures', 'R')
]

c.executemany('''INSERT INTO Media
              (title, genre, year, director, studio, age_rating)
              VALUES (?,?,?,?,?,?)''', movies)

reviews = [
    (1, 'loved when i was younger, now, not as much. not bad as a debut for mcu spider-man but it relies too much on iron man and the avengers. solid 6.5/10'),
    (2, 'IMPECCABLE animated movie. great message, fun watch with family, incredible art direction. still feel a bit childish watching it tho. 7/10'),
    (3, 'contender for my favorite movie ever. its like if a really good burger spot was a film. great soundtrack, acting, everything just top notch. 100/10'),
    (4, 'i like this movie but incredibly annoying people also like this movie. which means i have to dock points. 5.5/10'),
    (5, 'great movie all around. tastefully done comedic scenes, great action, mediocre horror. scary concepts for sure but the scares moreso end up being startling due to the noise rather than the scene. killing klansmen is awesome tho. 8.5/10')
]

c.executemany('INSERT INTO Reviews VALUES (?,?)', reviews)

conn.commit()
conn.close()
print("just reassurance that it did the thing its supposed to")