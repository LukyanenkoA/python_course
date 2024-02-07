#ex1#1 найти кол-во чисел, взаимно простых с заданным.
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
def sum(x):
    s=0
    while x>0:
        digit=x % 10;
        if digit%3==0:
            s+=digit
        x//=10
        return s
#print(sum(35))
#2 найти делитель числа, являющийся взаимно простым с последней цифрой данного числа
def find(x):
    digit = x % 10;
    for i in range(2, x+1):
        if x%i == 0:
            if is_coprime(digit, i) == 1:
                return i
                return 1
#print(find(27))
