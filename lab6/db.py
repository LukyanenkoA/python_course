#вариант 8
# Создать БД Танцы

import sqlite3
import time
from lab6.schemas import *
from xml.dom.minidom import Document, parseString
#1
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def export_to_xml(self):
        doc = Document()
        root = doc.createElement('data')
        dances_elements = doc.createElement("dances")
        artists_elements = doc.createElement("artists")
        performances_elements = doc.createElement("performances")

        for dance in self.get_dances():
            dance_element = doc.createElement("dance")

            dance_id = doc.createElement("dance_id")
            dance_id.appendChild(doc.createTextNode(str(dance.dance_id)))
            dance_name = doc.createElement("dance_name")
            dance_name.appendChild(doc.createTextNode(dance.dance_name))
            caption = doc.createElement("caption")
            caption.appendChild(doc.createTextNode(str(dance.caption)))
            native_name = doc.createElement("native_name")
            native_name.appendChild(doc.createTextNode(str(dance.native_name)))
            genre = doc.createElement("genre")
            genre.appendChild(doc.createTextNode(str(dance.genre)))
            year = doc.createElement("year")
            year.appendChild(doc.createTextNode(str(dance.year)))
            origin = doc.createElement("origin")
            origin.appendChild(doc.createTextNode(str(dance.origin)))

            dance_element.appendChild(dance_id)
            dance_element.appendChild(dance_name)
            dance_element.appendChild(caption)
            dance_element.appendChild(native_name)
            dance_element.appendChild(genre)
            dance_element.appendChild(year)
            dance_element.appendChild(origin)
            dances_elements.appendChild(dance_element)
            
            for artist in self.get_artists():
                artist_element = doc.createElement("artist")
    
                artist_id = doc.createElement("artist_id")
                artist_id.appendChild(doc.createTextNode(str(artist.artist_id)))
                name = doc.createElement("name")
                name.appendChild(doc.createTextNode(artist.name))
                surname = doc.createElement("surname")
                surname.appendChild(doc.createTextNode(artist.surname))
                country = doc.createElement("country")
                country.appendChild(doc.createTextNode(artist.country))
                gender = doc.createElement("gender")
                gender.appendChild(doc.createTextNode(artist.gender))
                dance_style = doc.createElement("dance_style")
                dance_style.appendChild(doc.createTextNode(str(artist.dance_style)))
    
                artist_element.appendChild(artist_id)
                artist_element.appendChild(name)
                artist_element.appendChild(surname)
                artist_element.appendChild(country)
                artist_element.appendChild(gender)
                artist_element.appendChild(dance_style)
                artists_elements.appendChild(artist_element)
    
            for performance in self.get_performances():
                performance_element = doc.createElement("performance")
    
                performance_id = doc.createElement("performance_id")
                performance_id.appendChild(doc.createTextNode(str(performance.performance_id)))
                title = doc.createElement("title")
                title.appendChild(doc.createTextNode(performance.title))
                date = doc.createElement("date")
                date.appendChild(doc.createTextNode(performance.date))
                country = doc.createElement("country")
                country.appendChild(doc.createTextNode(performance.country))
                dance_style = doc.createElement("dance_style")
                dance_style.appendChild(doc.createTextNode(str(performance.dance_style)))
                artist = doc.createElement("artist")
                artist.appendChild(doc.createTextNode(str(performance.artist)))
    
                performance_element.appendChild(performance_id)
                performance_element.appendChild(title)
                performance_element.appendChild(date)
                performance_element.appendChild(country)
                performance_element.appendChild(dance_style)
                performance_element.appendChild(artist)
                performances_elements.appendChild(performance_element)
    
            root.appendChild(dances_elements)
            root.appendChild(performances_elements)
            root.appendChild(artists_elements)
            doc.appendChild(root)
            name = f"temp/export_{int(time.time())}.xml"
            with open(name, "w") as f:
                f.write(doc.toprettyxml())
            return name

    def import_xml(self, binary):
        dom = parseString(binary)
        dances = dom.getElementsByTagName("dance")
        artists = dom.getElementsByTagName("artist")
        performances = dom.getElementsByTagName("performance")
        for dance in dances:
            dance_id = int(dance.getElementsByTagName("dance_id")[0].firstChild.nodeValue)
            dance_name = dance.getElementsByTagName("dance_name")[0].firstChild.nodeValue
            dance_caption = dance.getElementsByTagName("caption")[0].firstChild.nodeValue
            dance_native_name = dance.getElementsByTagName("native_name")[0].firstChild.nodeValue
            dance_genre = dance.getElementsByTagName("genre")[0].firstChild.nodeValue
            dance_year = int(dance.getElementsByTagName("year")[0].firstChild.nodeValue)
            dance_origin = dance.getElementsByTagName("origin")[0].firstChild.nodeValue
            self.save_dance(dance(dance_id=dance_id, dance_name=dance_name, caption=dance_caption, native_name=dance_native_name, genre=dance_genre, year=dance_year, origin=dance_origin))

        for artist in artists:
            artist_id = int(artist.getElementsByTagName("artist_id")[0].firstChild.nodeValue)
            artist_name = artist.getElementsByTagName("name")[0].firstChild.nodeValue
            artist_surname = artist.getElementsByTagName("surname")[0].firstChild.nodeValue
            artist_country = artist.getElementsByTagName("country")[0].firstChild.nodeValue
            artist_gender= artist.getElementsByTagName("gender")[0].firstChild.nodeValue
            artist_dance_style = int(artist.getElementsByTagName("dance_style")[0].firstChild.nodeValue)
            self.save_artist(artist(id=artist_id, name=artist_name, surname=artist_surname, country=artist_country, gender=artist_gender, dance_style=artist_dance_style))

        for performance in performances:
            performance_id = int(performance.getElementsByTagName("id")[0].firstChild.nodeValue)
            performance_title = performance.getElementsByTagName("title")[0].firstChild.nodeValue
            performance_date = performance.getElementsByTagName("date")[0].firstChild.nodeValue
            performance_country = performance.getElementsByTagName("country")[0].firstChild.nodeValue
            performance_dance_style = int(performance.getElementsByTagName("dance_style")[0].firstChild.nodeValue)
            performance_artist = int(performance.getElementsByTagName("artist")[0].firstChild.nodeValue)
            self.save_performance(performance(id=performance_id, title=performance_title, date=performance_date, country=performance_country, dance_style=performance_dance_style, artist=performance_artist))

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dances (
                            dance_id INTEGER PRIMARY KEY,
                            dance_name TEXT NOT NULL,
                            caption TEXT NOT NULL,
                            native_name TEXT NOT NULL,
                            genre TEXT NOT NULL,
                            year INTEGER NOT NULL,
                            origin TEXT NOT NULL
                            );''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS artists (
                            artist_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            country TEXT NOT NULL,
                            gender TEXT NOT NULL,
                            dance_style INTEGER NOT NULL,
                            FOREIGN KEY(dance_style) REFERENCES dances(dance_id)
                            );''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS performances (
                            performance_id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            date TEXT NOT NULL,
                            country TEXT NOT NULL,
                            dance_style INTEGER NOT NULL,
                            artist INTEGER NOT NULL,
                            FOREIGN KEY(dance_style) REFERENCES dances(dance_id)
                            FOREIGN KEY(artist) REFERENCES artists(artist_id)
                            );''')

        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS dances_id ON dances(dance_id);')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS performances_id ON performances(performance_id);')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS artists_id ON artists(artist_id);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS artists_dance_styles ON artists(dance_style);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS performances_dance_styles ON performances(dance_style);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS performances_artists ON performances(artist);')

        self.connection.commit()

    def add_dance(self, dance: Dance):
        self.cursor.execute('''INSERT INTO dances (dance_name, caption, native_name, genre, year, origin) VALUES (?, 
        ?, ?, ?, ?, ?);''', (
            dance.dance_id, dance.name, dance.caption, dance.native_name, dance.genre, dance.year, dance.origin))
        self.connection.commit()

    def add_artist(self, artist: Artist):
        self.cursor.execute('''INSERT INTO Artist (name, surname, country, gender, dance_style) VALUES (?, ?, ?, ?, 
        ?);''', (
            artist.artist_id, artist.name, artist.surname, artist.country, artist.gender, artist.dance_style))
        self.connection.commit()

    def add_performance(self, performance: Performance):
        self.cursor.execute('''INSERT INTO Performance (title, date, country, dance_style, artist) VALUES (?, ?, ?, ?, ?);''', (
            performance.performance_id, performance.date, performance.country, performance.dance_style, performance.artist))
        self.connection.commit()


    def get_dances(self) -> list[Dance]:
        dances = self.cursor.execute("SELECT * FROM dances").fetchall()
        return list(map(Dance.mapper, dances))

    def get_dance_by_id(self, id: int) -> Dance:
        dance = self.cursor.execute("SELECT * FROM dances WHERE dance_id=?", (id,)).fetchone()
        return Dance.mapper(dance)

    def get_artists(self) -> list[Artist]:
        artists = self.cursor.execute("SELECT * FROM artists").fetchall()
        return list(map(Artist.mapper, artists))

    def get_artist_by_id(self, id: int) -> Artist:
        artist = self.cursor.execute("SELECT * FROM artists WHERE artist_id=?", (id,)).fetchone()
        return Artist.mapper(artist)

    def get_artists_by_dance_id(self, dance_id: int) -> list[Artist]:
        artists = self.cursor.execute("SELECT * FROM artists WHERE dance_id=?", (dance_id,)).fetchall()
        return list(map(Artist.mapper, artists))

    def get_performance_by_id(self, id: int) -> Performance:
        performance = self.cursor.execute("SELECT * FROM performances WHERE performance_id=?", (id,)).fetchone()
        return Performance.mapper(performance)

    def get_performances(self) -> list[Performance]:
        performances = self.cursor.execute("SELECT * FROM performances").fetchall()
        return list(map(Performance.mapper, performances))

    def close(self):
        self.connection.commit()
        self.connection.close()


#3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
query = '''INSERT INTO dances (dance_name, caption, native_name, genre, year, origin) VALUES (?, ?, ?, ?, ?, ?);'''
insert_dances = [
    ("Танго", "парный танец свободной композиции, исполняемый под характерную музыку", "tango", "латиноамериканские танцы", 1850, "Южная Америка"),
    ("Балет", "спектакль, содержание которого воплощается в музыкально-хореографических образах", "ballet", "театральное искусство", 1700, "Франция"),
    ("Бальный танец", "танец, который служит для массового развлечения и исполняется парой или большим количеством участников на танцевальных вечерах", "ball", "парный танец", 1600, "Италия"),
    ("Акробатический танец", "вид спорта, в котором спортсмены соревнуются в техническом мастерстве и выразительности исполнения под музыку сложных акробатических движений и танцевальных элементов.", "acro dance", "парный танец", 1900, "США"),
    ("Уличный танец", "танцевальный стиль, который развивался вне танцевальной студии", "street dance", "импровизация", 1890, "США")
]

cursor.executemany(query, insert_dances)
query2 = '''INSERT INTO artists (name, surname, country, gender, dance_style) VALUES (?, ?, ?, ?, ?);'''
insert_artists= [
('Joe', 'Ricks', 'USA', 'male', 1),
('Xi', 'Zhitu', 'China', 'male', 2),
('Ivan', 'Petrov', 'Russia', 'male', 5),
('Jessi', 'Kim', 'South Korea', 'female', 3),
('Rodrigo', 'Este', 'Spain', 'male', 4)
]

cursor.executemany(query2, insert_artists)
query3 = '''INSERT INTO performances (title, date, country, dance_style, artist) VALUES (?, ?, ?, ?, ?);'''
insert_perfomances = [
('Grand concert', '2021-11-01', 'USA', 1, 1),
('Dance battle', '2022-11-30', 'China', 2, 2),
('Street beat style', '2023-01-01', 'France', 5, 3),
('Special performance', '2021-12-01', 'Spain', 3, 4),
('Great ball', '2021-11-01', 'USA', 4, 5)
]

cursor.executemany(query3, insert_perfomances)

connection.commit()
connection.close()
db = Database()
results = db.get_artists()
print(results)

'''
Name:  Joe
Surname:  Ricks
Dance style:  Танго
Name:  Xi
Surname:  Zhitu
Dance style:  Балет
Name:  Ivan
Surname:  Petrov
Dance style:  Уличный танец
Name:  Jessi
Surname:  Kim
Dance style:  Бальный танец
Name:  Rodrigo
Surname:  Este
Dance style:  Акробатический танец
'''
results = db.get_performances()
for row in results:
    print(row)
'''
(1, 'Grand concert', '2021-11-01', 'USA', 1, 1)
(2, 'Dance battle', '2022-11-30', 'China', 2, 2)
(3, 'Street beat style', '2023-01-01', 'France', 5, 3)
(4, 'Special performance', '2021-12-01', 'Spain', 3, 4)
(5, 'Great ball', '2021-11-01', 'USA', 4, 5)
'''
results = db.get_artists()
print(results)
'''
Name:  Joe
Surname:  Ricks
Dance style:  Танго
Performance:  Grand concert
Date of performance:  2021-11-01
Name:  Xi
Surname:  Zhitu
Dance style:  Балет
Performance:  Dance battle
Date of performance:  2022-11-30
Name:  Ivan
Surname:  Petrov
Dance style:  Уличный танец
Performance:  Street beat style
Date of performance:  2023-01-01
Name:  Jessi
Surname:  Kim
Dance style:  Бальный танец
Performance:  Special performance
Date of performance:  2021-12-01
Name:  Rodrigo
Surname:  Este
Dance style:  Акробатический танец
Performance:  Great ball
Date of performance:  2021-11-01
'''


