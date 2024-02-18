#вариант 8
# Создать БД Танцы

import sqlite3

#1
connection = sqlite3.connect('dance_database.db')
cursor = connection.cursor()

#2
cursor.execute('''
CREATE TABLE IF NOT EXISTS Dance (
dance_id INTEGER PRIMARY KEY,
dance_name TEXT NOT NULL,
caption TEXT NOT NULL,
native_name TEXT NOT NULL,
genre TEXT NOT NULL,
year INTEGER NOT NULL,
origin TEXT NOT NULL
);''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Artist (
artist_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
surname TEXT NOT NULL,
country TEXT NOT NULL,
gender TEXT NOT NULL,
dance_style INTEGER NOT NULL,
FOREIGN KEY(dance_style) REFERENCES Dance(dance_id)
);''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Performance (
performance_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
date TEXT NOT NULL,
country TEXT NOT NULL,
dance_style INTEGER NOT NULL,
artist INTEGER NOT NULL,
FOREIGN KEY(dance_style) REFERENCES Dance(dance_id)
FOREIGN KEY(artist) REFERENCES Artist(artist_id)
);''')
connection.commit()

#3
query = '''INSERT INTO Dance (dance_name, caption, native_name, genre, year, origin) VALUES (?, ?, ?, ?, ?, ?);'''
insert_dances = [
    ("Танго", "парный танец свободной композиции, исполняемый под характерную музыку", "tango", "латиноамериканские танцы", 1850, "Южная Америка"),
    ("Балет", "спектакль, содержание которого воплощается в музыкально-хореографических образах", "ballet", "театральное искусство", 1700, "Франция"),
    ("Бальный танец", "танец, который служит для массового развлечения и исполняется парой или большим количеством участников на танцевальных вечерах", "ball", "парный танец", 1600, "Италия"),
    ("Акробатический танец", "вид спорта, в котором спортсмены соревнуются в техническом мастерстве и выразительности исполнения под музыку сложных акробатических движений и танцевальных элементов.", "acro dance", "парный танец", 1900, "США"),
    ("Уличный танец", "танцевальный стиль, который развивался вне танцевальной студии", "street dance", "импровизация", 1890, "США")
]
cursor.executemany(query, insert_dances)

query2 = '''INSERT INTO Artist (name, surname, country, gender, dance_style) VALUES (?, ?, ?, ?, ?);'''
insert_artists= [
('Joe', 'Ricks', 'USA', 'male', 1),
('Xi', 'Zhitu', 'China', 'male', 2),
('Ivan', 'Petrov', 'Russia', 'male', 5),
('Jessi', 'Kim', 'South Korea', 'female', 3),
('Rodrigo', 'Este', 'Spain', 'male', 4)
]
cursor.executemany(query2, insert_artists)

query3 = '''INSERT INTO Performance (title, date, country, dance_style, artist) VALUES (?, ?, ?, ?, ?);'''

insert_perfomances = [
('Grand concert', '2021-11-01', 'USA', 1, 1),
('Dance battle', '2022-11-30', 'China', 2, 2),
('Street beat style', '2023-01-01', 'France', 5, 3),
('Special performance', '2021-12-01', 'Spain', 3, 4),
('Great ball', '2021-11-01', 'USA', 4, 5)
]
cursor.executemany(query3, insert_perfomances)

connection.commit()

#4
cursor.execute('SELECT name, surname, dance_name FROM Artist, Dance WHERE Dance.dance_id = Artist.dance_style')
results = cursor.fetchall()
for row in results:
    print("Name: ", row[0])
    print("Surname: ", row[1])
    print("Dance style: ", row[2])

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
cursor.execute('SELECT * FROM Performance')
results = cursor.fetchall()
for row in results:
    print(row)
'''
(1, 'Grand concert', '2021-11-01', 'USA', 1, 1)
(2, 'Dance battle', '2022-11-30', 'China', 2, 2)
(3, 'Street beat style', '2023-01-01', 'France', 5, 3)
(4, 'Special performance', '2021-12-01', 'Spain', 3, 4)
(5, 'Great ball', '2021-11-01', 'USA', 4, 5)
'''
cursor.execute('SELECT name, surname, dance_name, title, date FROM Artist, Dance, Performance WHERE Dance.dance_id = Performance.dance_style and Performance.artist = Artist.artist_id')
results = cursor.fetchall()
for row in results:
    print("Name: ", row[0])
    print("Surname: ", row[1])
    print("Dance style: ", row[2])
    print("Performance: ", row[3])
    print("Date of performance: ", row[4])
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
connection.close()
