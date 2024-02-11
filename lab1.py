#ex1#1 найти кол-во чисел, взаимно простых с заданным.
'''
def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
def is_coprime(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
def q_coprime(x):
    q=0
    for i in range(2, x):
        a = i
        b= x
        while a!=b:
            if a>b:
                a-=b
            else:
                b-=a
        if a==1:
            q+=1
            return q
#print(q_coprime(8))
#2 найти сумму цифр числа, делящихся на три
def sum1(x):
    s=0
    while x>0:
        digit=x % 10;
        if digit%3==0:
            s+=digit
        x//=10
        return s
#print(sum1(35))
#3 найти делитель числа, являющийся взаимно простым с последней цифрой данного числа
def find(x):
    digit = x % 10;
    for i in range(2, x+1):
        if x%i == 0:
            if is_coprime(digit, i) == 1:
                return i
                return 1
#print(find(27))
#ex2-4 (2, 10, 17)

print("Введите номер задания")
while True:
    n = int(input())
    if n in [2,10,17]:
        break
    else:
        n = int(input())
if n == 2:
    #2 Дана строка, состоящая из символов латиницы. Необходимо проверить, упорядочены ли строчные символы этой строки по возрастанию.
    str = input("Введите строку")
    if str == sorted(str):
        print(True)
    else:
        print(False)
if n == 10:
    #10 Дана строка. Необходимо подсчитать количество букв "А" в этой строке.
    str = input("Введите строку")
    print(str.count('a'))
if n == 17:
    #17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения.
    str = input("Введите строку ")
    print(str.split('/')[-1].split('.')[0]
#ex5
#Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007"
str = input("Введите строку")
import re
print(re.findall(r'\d{1,2} \w{3,8} \d\d\d\d', str))

#ex6-8 (2, 10, 17)
print("Введите номер задания")
while True:
    n = int(input())
    if n in [2,10,17]:
        break
    else:
        n = int(input())
if n == 2:
    #2 Дана строка. Необходимо найти все строчные символы латиницы, которые в ней используются.
    str = input("Введите строку")
    s=''
    for el in str:
        if el.islower() and el in 'qwertyuioplkjhgfdsazxcvbnm':
            s += el
    print(s)
if n == 10:
    #10 Дана строка. Необходимо найти количество задействованных символов латиницы в этой строке (без дубликатов).
    q = 0
    str = input("Введите строку")
    str = str.lower()
    for el in 'qwertyuioplkjhgfdsazxcvbnm':
        if el in str:
            q+=1
            str = str.replace(el, '')
            print(str)
    print(q)
if n == 17:
    #17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения.
    str = input("Введите строку ")
    print(str.split('/')[-1].split('.')[0])

#task9 Прочитать список строк с клавиатуры. Упорядочить по длине строки

n = int(input("Введите количество строк "))
input_str = []

for i in range(n):
    input_str.append(input("Введите строку: "))
print(sorted(input_str, key=len))

#task10 Дан список строк с клавиатуры. Упорядочить по количеству слов в строке

n = int(input("Введите количество строк "))
input_str = []

for i in range(n):
    input_str.append(input("Введите строку: "))
for i in range(n):
    input_str[i]=input_str[i].split(' ')
input_str = sorted(input_str, key=len)
for i in range(n):
    input_str[i]=' '.join(input_str[i])
print(input_str)

#ex11-14 (2, 4, 8, 10)
n = int(input("Введите номер задания: "))
while True:
    if n in [2, 4, 8, 10]:
        break
    else:
        n = int(input("Введите номер задания: "))

q = int(input("Введите количество строк "))
input_str = []
for i in range(q):
    input_str.append(input("Введите строку: "))

def getValue(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])
    return sum

if n == 2:
    #2 В порядке увеличения среднего веса ASCII-кода символа строки.
    def sortStrings(arr, num):
        v = []
        for i in range(num):
            val = getValue(arr[i])
            v.append([val/len(arr[i]), arr[i]])
        v = sorted(v)
        return v
    print(sortStrings(input_str, q))
if n == 4:
    #4 В порядке увеличения квадратичного отклонения среднего веса
    #ASCII-кода символа строки от среднего веса ASCII-кода символа первой
    #строки.
    def sortStrings2(arr, num):
        v = []
        val1 = getValue(arr[0])
        for i in range(num):
            val = getValue(arr[i])
            v.append([(val/len(arr[i])-val1/len(arr[0]))**2, arr[i]])
        v = sorted(v)
        return v
    print(sortStrings2(input_str, q))
if n == 8:
    #8 В порядке увеличения квадратичного отклонения между средним
    #весом ASCII-кода символа в строке и максимально среднего ASCII-кода
    #тройки подряд идущих символов в строке.
    def sortStrings3(arr, num):
        v = []
        for i in range(num):
            val = getValue(arr[i])
            max_w = 0
            for j in range(len(arr[i])-2):
                if (ord(arr[i][j]) + ord(arr[i][j+1]) + ord(arr[i][j+2]))>max_w:
                    max_w = ord(arr[i][j]) + ord(arr[i][j+1]) + ord(arr[i][j+2])
            v.append([(val / len(arr[i]) - max_w / 3) ** 2, arr[i]])
        v = sorted(v)
        return v
    print(sortStrings3(input_str, q))
if n == 10:
    #10 В порядке увеличения среднего количества «зеркальных» троек (например, «ada») символов в строке.
    def sortStrings4(arr, num):
        v = []
        for i in range(num):
            mirrored_three = 0
            for j in range(len(arr[i]) - 2):
                if arr[i][j]==arr[i][j + 2]:
                    mirrored_three+=1
            v.append([mirrored_three, arr[i]])
        v = sorted(v)
        return v
    print(sortStrings4(input_str, q))
'''

#ex15-19 (8, 20, 32, 44, 56)

n = int(input("Введите номер задания: "))
while True:
    if n in [8, 20, 32, 44, 56]:
        break
    else:
        n = int(input("Введите номер задания: "))
def enter_array():
    arr = []
    q = int(input("Введите количество элементов массива: "))
    for i in range(q):
        a = float(input("Введите элемент: "))
        if int(a) == a:
            arr.append(int(a))
        else:
            arr.append(a)
    return arr
if n == 8:
    #8 Дан целочисленный массив. Необходимо найти индексы двух наименьших элементов массива.
    arr = enter_array()
    def two_mins(a):
        return sorted(a)[:2]
    print(*two_mins(arr))

if n == 20:
    #20 Дан целочисленный массив. Необходимо найти все пропущенные числа.
    arr = enter_array()
    def find(arr):
        arr2=[]
        ans = []
        m = max(*arr)
        for i in range (m+1):
            arr2.append(i)
        for el in arr2:
            if el not in arr:
                ans.append(el)
        return ans
    print(find(arr))


if n == 32:
    #32 Дан целочисленный массив. Найти количество его локальных максимумов.
    arr = enter_array()
    q = len(arr)
    def findLocalMaxima(n, arr):
        mx = []
        if (arr[0] > arr[1]):
            mx.append(0)
        for i in range(1, n - 1):
            if (arr[i - 1] < arr[i] > arr[i + 1]):
                mx.append(i)

        if (arr[-1] > arr[-2]):
            mx.append(n - 1)
        if (len(mx) > 0):
            print("Points of Local maxima" \
                  " are : ", end='')
            print(*mx)
        else:
            print("There are no points of" \
                  " Local maxima.")
    findLocalMaxima(q, arr)

if n == 44:
    #44 Дан массив чисел. Необходимо проверить, чередуются ли в нем целые и вещественные числа.
    arr = enter_array()
    def is_alternating(arr):
        for i in range(len(arr)-1):
            if (type(arr[i]) is int and type(arr[i+1]) is float) or (type(arr[i]) is float and type(arr[i+1]) is int):
                return True
            else:
                return False
    print(is_alternating(arr))

if n == 56:
    #Для введенного списка посчитать среднее арифметическое
    #непростых элементов, которые больше, чем среднее арифметическое простых.
    arr = enter_array()
    temp = []
    def cond_avg(arr):
        for el in arr:
            if is_prime(el):
                temp.append(el)
        avg = sum(temp)/len(temp)

        for el in arr:
            if el > avg and not is_prime(el):
                temp.append(el)
        return sum(temp)/len(temp)
    print(cond_avg(arr))
    