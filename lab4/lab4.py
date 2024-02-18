#вариант 8
'''
for file in '27-123a.txt', '27-123b.txt':
    f = open(file)
    n, k, v = map(int, f.readline().split())
    a = [0] * k

    k_del, ost  = k // 2, k % 2

    for i in range(n):
        kilometer_num, kolvo = map(int, f.readline().split())
        a[kilometer_num % k] = kolvo // v + (kolvo % v > 0)

    min_sum = 10**25
    s = 0
    # Считаем минимальную сумму доставки, если завод стоит на нулевом километре
    for i in range(1, k):
        s += a[i] * (2*k_del + ost - abs(2*(i-k_del) - ost)) // 2

    d = a[0] + sum(a[k_del + 2:k]) - sum(a[1:k_del + 1])

    for i in range(1, k):
        s += d
        d += 2 * a[i] - a[(k_del + i) % k] - a[(k_del + i + ost) % k]
        min_sum = min(min_sum, s)
    print('Ответ для файла', file,':', min_sum)

Ответ для файла 27-123a.txt : 1268077
Ответ для файла 27-123b.txt : 457260989979
'''
#2
#8 Дан файл, содержащий текст на русском языке и некоторые
#два слова. Определить, сколько раз они встречаются в тексте и сколько из них –
#непосредственно друг за другом.
word1 = input('Введите первое слово на русском языке для поиска')
word2 = input('Введите второе слово на русском языке для поиска')
f = open('text.txt', encoding = 'utf-8', mode = 'r')
arr = []
while f.readline():
    arr += f.readline().split()
print(arr)
for i in range(len(arr)):
    str = arr[i]
    result = ''.join(c for c in str if c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    #print(result)
    arr[i] = result.lower()
print(arr)
ans = arr.count(word1) + arr.count(word2)
conseq = 0
for i in range(len(arr)-1):
    if (arr[i]==word1 and arr[i+1]==word2) or (arr[i]==word2 and arr[i+1]==word1):
        conseq+=1
print('Эти два слова встречаются в тексте', ans, 'раз; последовательно встречаются', conseq, 'раз')