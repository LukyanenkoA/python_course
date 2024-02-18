#вариант 8
#8 Triangle Tetragon move, is_included
import abc
import math


class Figure(abc.ABC):

    @abc.abstractmethod
    def move(self, dx, dy):
        pass


class Point(object):
    def __init__(self, x, y):
        try:
            if(type(y) is int or type(x) is int):
                self.X = x
                self.Y = y
            else:
                raise Exception('Необходимо ввести числа')
        except Exception:
            print('Введите другие данные. Необходим численный тип')

    def move(self, dx, dy):
        try:
            self.X = self.X + dx
            self.Y = self.Y + dy
        except:
            print('Ошибка! Неверный тип данных, необходим численный тип')

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

class Triangle(Figure):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def move(self, dx, dy):
        self.point_a.move(dx, dy)
        self.point_b.move(dx, dy)
        self.point_c.move(dx, dy)

    def get_id(self):
        print(id(self))

class Tetragon(Figure):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def move(self, dx, dy):
        self.point_a.move(dx, dy)
        self.point_b.move(dx, dy)
        self.point_c.move(dx, dy)
        self.point_d.move(dx, dy)

    def get_id(self):
        print(id(self))

def is_included(t1: Tetragon, t2: Triangle):
    try:
        f = True
        arr1x = [t1.point_a.X, t1.point_b.X, t1.point_c.X, t1.point_d.X]
        arr1y = [t1.point_a.Y, t1.point_b.Y, t1.point_c.Y, t1.point_d.Y]
        arr2x = [t2.point_a.X, t2.point_b.X, t2.point_c.X]
        arr2y = [t2.point_a.Y, t2.point_b.Y, t2.point_c.Y]
        for i in range(3):
            if arr2x[i]+arr2y[i] <=min(arr1x) + min(arr1y) or arr2x[i] + arr2y[i] >=max(arr1x) + max(arr1y):
                f = False
        return f
    except:
        print('Неверные данные, проверяет включение треугольника в четырехугольник')


p_a = Point('d;;;', 'll')
p_b = Point(3, 7)
p_c = Point(4, 2)

tr = Triangle(p_a, p_b, p_c)
#tr.move(10, 10)

p_a = Point(1, 1)
p_b = Point(6, 1)
p_c = Point(1, 5)
p_d = Point(5, 6)

tet = Tetragon(p_a, p_b, p_c, p_d)
#print(is_included(tet, tr))
'''
p_a = Point('d;;;', 'll')
Введите другие данные. Необходим численный тип

tr.move(10, 's')
Ошибка! Неверный тип данных, необходим численный тип

print(is_included(tet, 1))
Неверные данные, проверяет включение треугольника в четырехугольник
None

'''