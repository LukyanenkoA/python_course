#!/usr/bin/env python
import cgi, cgitb

from lab6.db import Database
from lab6.schemas import Dance, Artist, Performance

db = Database()


def display_dances():
    dances = db.get_dances()
    print("<h2>Танцы</h2>")

    # Обработка данных из формы
    form = cgi.FieldStorage()
    if form.getvalue('dance_name') and form.getvalue('caption') and form.getvalue('native_name') and form.getvalue(
            'genre') and form.getvalue('year') and form.getvalue('origin'):
        db.add_dance(Dance(dance_name=form.getvalue('dance_name'), caption=form.getvalue('caption'),
                           native_name=form.getvalue('native_name'), genre=form.getvalue('genre'),
                           year=int(form.getvalue('year')), origin=form.getvalue('origin')))
        print("<p>Танец добавлен успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название танца: <input type="text" name="dance_name"><br>')
    print('Описание: <input type="text" name="caption"><br>')
    print('Название на языке оригинала: <input type="text" name="native_name"><br>')
    print('Жанр: <input type="text" name="genre"><br>')
    print('Год: <input type="text" name="year"><br>')
    print('Место возникновения: <input type="text" name="origin"><br>')
    print('<input type="submit" value="Добавить танец">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for dance in dances:
        print(f"<li>{dance.name} - Описание: {dance.caption}, "
              f"Описание: {dance.caption}, "
              f"Название на языке оригинала: {dance.native_name}, "
              f"Жанр: {dance.genre}, "
              f"Год: {dance.year}, "
              f"Место возникновения: {dance.origin}</li>")
    print("</ul>")


def display_artists():
    artists = db.get_artists()
    print("<h2>Артисты</h2>")

    # Обработка данных из формы
    form = cgi.FieldStorage()
    if form.getvalue('name') and form.getvalue('surname') and form.getvalue('country') and form.getvalue(
            'gender') and form.getvalue('dance_style'):
        db.add_artist(Artist(name=form.getvalue('name'), surname=form.getvalue('surname'),
                             country=form.getvalue('country'), gender=form.getvalue('gender'),
                             dance_style=int(form.getvalue('dance_style'))))
        print("<p>Артист добавлен успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Имя: <input type="text" name="name"><br>')
    print('Фамилия: <input type="text" name="surname"><br>')
    print('Страна: <input type="text" name="country"><br>')
    print('Пол: <input type="text" name="gender"><br>')
    print('Стиль танца: <input type="text" name="dance_style"><br>')
    print('<input type="submit" value="Добавить артиста">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for artist in artists:
        dance = db.get_dance_by_id(artist.dance_style)
        print(f"<li>Имя:{artist.name},"
              f"Фамилия: {artist.caption}, "
              f"Страна: {artist.country}, "
              f"Пол: {artist.native_name}, "
              f"Стиль танца: {dance.dance_name}</li>")
    print("</ul>")


def display_performances():
    performances = db.get_performances()
    print("<h2>Выступления</h2>")

    # Обработка данных из формы
    form = cgi.FieldStorage()
    if form.getvalue('title') and form.getvalue('date') and form.getvalue('country') and form.getvalue(
            'dance_style') and form.getvalue('artist'):
        db.add_performance(Performance(title=form.getvalue('title'), date=form.getvalue('date'),
                                       country=form.getvalue('country'), dance_style=form.getvalue('dance_style'),
                                       artist=int(form.getvalue('artist'))))
        print("<p>Выступление добавлено успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="title"><br>')
    print('Дата: <input type="text" name="date"><br>')
    print('Страна: <input type="text" name="country"><br>')
    print('Стиль танца: <input type="text" name="dance_style"><br>')
    print('Артист: <input type="text" name="artist"><br>')
    print('<input type="submit" value="Добавить выступление">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for performance in performances:
        dance = db.get_dance_by_id(performance.dance_style)
        artist = db.get_artist_by_id(performance.artist)
        print(f"<li>Название:{performance.title},"
              f"Дата: {performance.date}, "
              f"Страна: {performance.country}, "
              f"Стиль танца: {dance.dance_name}, "
              f"Артист: {artist.surname}</li>")
    print("</ul>")


cgitb.enable()
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Танцы</title>")
print("</head>")
print("<body>")
print('<header><a href="http://localhost:8000/cgi-bin/import.py">Импорт/Экспорт</a></header>')
display_dances()
display_artists()
display_performances()
print("</body>")
print("</html>")
