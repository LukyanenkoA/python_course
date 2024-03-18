#!/usr/bin/env python
import cgi, cgitb

from lab6.db import Database
from lab6.schemas import Dance, Artist, Performance

db = Database()


def display_dances():
    dances = db.get_dances()
    print("<h2>Планеты</h2>")

    # Обработка данных из формы
    form = cgi.FieldStorage()
    if form.getvalue('dance_name') and form.getvalue('caption') and form.getvalue('native_name') and form.getvalue('genre') and form.getvalue('year') and form.getvalue('origin'):
        db.add_planet(Dance(dance_name=form.getvalue('star_id'), caption=form.getvalue('caption'),
                            native_name=form.getvalue('native_name'), genre=form.getvalue('genre'),
                            year=int(form.getvalue('year')), year=form.getvalue('origin')))
        print("<p>Танец добавлен успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название танца: <input type="text" name="dance_name"><br>')
    print('Описание: <input type="text" name="caption"><br>')
    print('Название на языке оригинала: <input type="text" name="native_name"><br>')
    print('Жанр: <input type="text" name="genre"><br>')
    print('Год: <input type="text" name="year"><br>')
    print('Место возникновения: <input type="text" name="year"><br>')
    print('<input type="submit" value="Добавить танец">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for dance in dances:
        star = db.get_star_by_id(dance.star_id)
        print(f"<li>{dance.name} - Радиус: {dance.radius} km, Звезда: {star.name}</li>")
    print("</ul>")


def display_moons():
    moons = db.get_moons()
    print("<h2>Спутники</h2>")

    # Обработка данных из формы
    moons_form = cgi.FieldStorage()
    if moons_form.getvalue('name') and moons_form.getvalue('planet_id'):
        db.add_moon(MoonRequest(planet_id=int(moons_form.getvalue('planet_id')), name=moons_form.getvalue('name')))
        print("<p>Спутник добавлен успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="name"><br>')
    print('Id планеты: <input type="text" name="planet_id"><br>')
    print('<input type="submit" value="Добавить спутник">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for moon in moons:
        planet = db.get_planet_by_id(moon.planet_id)
        print(f"<li>{moon.name} - Спутник планеты: {planet.name}</li>")
    print("</ul>")


def display_stars():
    stars = db.get_stars()
    print("<h2>Звезды</h2>")

    # Обработка данных из формы
    stars_form = cgi.FieldStorage()
    if stars_form.getvalue('name') and stars_form.getvalue('mass'):
        db.add_star(StarRequest(mass=int(stars_form.getvalue('mass')), name=stars_form.getvalue('name')))
        print("<p>Звезда добавлена успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="name"><br>')
    print('Масса: <input type="text" name="mass"><br>')
    print('<input type="submit" value="Добавить звезду">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for star in stars:
        print(f"<li>{star.name} - Масса: {star.mass}</li>")
    print("</ul>")


cgitb.enable()
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Космос</title>")
print("</head>")
print("<body>")
print('<header><a href="http://localhost:8000/cgi-bin/import.py">Импорт/Экспорт</a></header>')
display_dances()
display_stars()
display_moons()
print("</body>")
print("</html>")