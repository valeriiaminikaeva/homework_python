import string


def text(t):
    d = {}
    t = t.lower()
    for q in string.punctuation:
        t.replace(q, '')
    splitted = t.split()
    for value in set(splitted):
        d[value] = splitted.count(value)
    top = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Топ 10 слов:")
    for u in range(10):
        print(str(u+1) + "). " + str(top[u][0]) + ", кол-во: " + str(top[u][1]))
    return d


f = open('kut.txt', 'r')
lines = ' '.join(f.readlines())
text(lines)
f.close()