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



connection.close()






