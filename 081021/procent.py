import random
import string
print("Введите количество букв в строчке")
n = int(input())

def gen(n):
    s=''
    for i in range(n):
        s=s + random.choice(string.ascii_letters)
    return s

def f1(gen1):
    string = gen1
    print(string)
    string1 = string.lower()
    small, long = 0,0
    for i,j in zip(string,string1):
        if i == j:
            small +=1
        else:
            long +=1
    if small == long:
        return 0
    elif small > long:
        return -1
    else:
        return 1100

print("Введите количество строк в массиве")
l = int(input())
massiv = [gen(n) for i in range(l)]

def proverka(massiv):
    kol = 0
    ravno, small1, long1 = 0, 0, 0
    for i in range(len(massiv)):
        kol = f1(massiv[i])
        if kol == 0:
            ravno += 1
        elif kol == -1:
            small1 += 1
        else:
            long1 +=1
    lenmassiv = len(massiv)
    print("Процент строк с большим количеством маленьких букв", small1/lenmassiv*100)
    print("Процент строк с большим количеством больших букв", long1/lenmassiv*100)
    print("Процент строк с равным количеством маленьких и больших букв", ravno/lenmassiv*100)
    print(ravno, small1, long1)

proverka(massiv)