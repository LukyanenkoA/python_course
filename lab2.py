#вариант 8 (7)
#1
def num_game():
    n = int(input("Введите максимальное число\n"))
    all_nums = set(range(1, n + 1))
    possible_nums = all_nums
    while True:
        guess = input("Введите догадку\n")
        if guess == 'HELP':
            break
        guess = {int(x) for x in guess.split()}
        answer = input("Введите ответ (YES/NO)\n")
        if answer == 'YES':
            possible_nums &= guess
        else:
            possible_nums &= all_nums - guess

    print(' '.join([str(x) for x in sorted(possible_nums)]))
#num_game()
'''
Введите максимальное число
10
Введите догадку
1 2 3 4 5
Введите ответ (YES/NO)
YES
Введите догадку
2 4 6 8 10
Введите ответ (YES/NO)
NO
Введите догадку
HELP
1 3 5
'''
#2
def find_country():
    motherland = {}
    for i in range(int(input("Введите количество стран:\n"))):
        country, *cities = input("Введите страну и ее города:\n").split()
        for city in cities:
            motherland[city] = country

    for i in range(int(input("Введите количество городов:\n"))):
        print(motherland[input("Введите город для поиска страны:\n")])
    print(motherland)
find_country()
'''
Введите количество стран:
2
Введите страну и ее города:
Russia Moscow Petersburg Novgorod Kaluga
Введите страну и ее города:
Ukraine Kiev Donetsk Odessa
Введите количество городов:
3
Введите город для поиска страны:
Odessa
Ukraine
Введите город для поиска страны:
Moscow
Russia
Введите город для поиска страны:
Novgorod
Russia
'''