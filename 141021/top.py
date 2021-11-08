import operator
import string

str_ = 'One day, a good King and his beautiful Queen have a baby. They are very happy. "Let’s have a party," says the King. The King and Queen invite their friends to the party. They also invite seven good fairies. Today is the party! Everybody gives a present to the baby princess. The fairies also give presents. Their presents are very special. "You will be beautiful," says the first fairy. "You will be clever," says the second fairy. "You will be kind," says the third fairy. "You will sing," says the fourth fairy. "You will dance," says the fifth fairy. "You will always be happy," says the sixth fairy. Suddenly, somebody knocks on the palace door.'



b = str_.split()


def clean_text(words_list):
    result = []
    for word in words_list:
        new_word = ''
        has_punch_mark = False
        for ch in string.punctuation:
            if ch in word:
                has_punch_mark = True
                pos = word.find(ch)
                if pos == len(word) - 1:
                    new_word = word[:pos]
                else:
                    new_word = word[:pos] + word[pos + 1:]
        if not has_punch_mark:
               new_word = word
               result.append(new_word.lower())
    return result
a = clean_text(b)
def count_words(words):
       words_set = set(words)
       words_dict = {}
       for word in words_set:
              words_dict[word] = words.count(word)
       return words_dict

c = sorted(count_words(a).items(), key=lambda x : x[1], reverse=True)
d = list(c)[:10]
for word, num in d:
    print(word, ': ', num)