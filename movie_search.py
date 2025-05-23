import sqlite3

# behind the sceens (so proud of ts)
def show_recent_movies():
    with sqlite3.connect('media.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT title, year, age_rating
                     FROM Media
                     ORDER BY year DESC
                     LIMIT 4''')
        print("\n4 recent movies (supposedly):")
        for title, year, rating in c.fetchall():
            print(f"- {title} ({year}) [{rating}]")

# menu options riddles with homestuck referential nonsense (why??)
def full_search():
    with sqlite3.connect('media.db') as conn:
        c = conn.cursor()

        print("\n search optiones:")
        print("1. Allllllll of the movies ::::) \n2. BY G3NR3\n3. bY YEAR,,,\n4. BY DIRECTOR\n5. by 2tudiio\n6. By Age Rating")
        choice = input("Choose search type (1-6): ")

        query = '''SELECT m.title, m.year, m.genre, m.director, r.review
                   FROM Media m
                            LEFT JOIN Reviews r ON m.id = r.media_id'''
        params = []

        if choice == '2':
            genre = input("EnTeR gEnRe: ")
            query += " WHERE m.genre LIKE ?"
            params.append(f'%{genre}%')
        elif choice == '3':
            year = input("--Enter year: ")
            query += " WHERE m.year = ?"
            params.append(int(year))
        elif choice == '4':
            director = input("enter direct0r: ")
            query += " WHERE m.director LIKE ?"
            params.append(f'%{director}%')
        elif choice == '5':
            studio = input("enter studio: ")
            query += " WHERE m.studio LIKE ?"
            params.append(f'%{studio}%')
        elif choice == '6':
            rating = input("D --> Enter age rating (e%: PG-13): ")
            query += " WHERE m.age_rating = ?"
            params.append(rating)

        c.execute(query, params)

        print("\nResults:")
        for title, year, genre, director, review in c.fetchall():
            print(f"{title} ({year})")
            print(f"Genre: {genre} | Director: {director}")
            print(f"Review: {review or 'nuffn yet'}\n")


# user menu
print(r"""
  __      _                _ _      ______                                            _           ___ 
 / _|    (_)              | | |     | ___ \                                          | |     _   |_  |
| |_ _ __ _  ___ _ __   __| | |_   _| |_/ /___  ___ ___ ___  _ __ ___   ___ _ __   __| |    (_)    | |
|  _| '__| |/ _ \ '_ \ / _` | | | | |    // _ \/ __/ __/ _ \| '_ ` _ \ / _ \ '_ \ / _` |           | |
| | | |  | |  __/ | | | (_| | | |_| | |\ \  __/ (_| (_| (_) | | | | | |  __/ | | | (_| |     _     | |
|_| |_|  |_|\___|_| |_|\__,_|_|\__, \_| \_\___|\___\___\___/|_| |_| |_|\___|_| |_|\__,_|    (_)   _| |
                                __/ |                                                            |___|
                               |___/                                                                  
""")

while True:
    print("\n1. search!\n2. four \"recent\" movies \n3. end service")
    choice = input("Choose option: ")

    if choice == '1':
        full_search()
    elif choice == '2':
        show_recent_movies()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")

print("\nthank u for using friendlyRecommend!")