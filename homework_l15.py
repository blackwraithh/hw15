from typing import Any
import re
import collections


# Решить задачи, выложить .py файл с решениями на github. В личный кабинет прикрепить .txt файл с ссылкой на репозиторий.


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
# def count_unique_elems(arr: list[Any]) -> int:
#     return len(Counter(arr).keys())



# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
#def get_10_popular_password(file: str) -> Any:

#test1 (slow count)

# file = open("pwd.txt", "r")
# frequent_word = ""
# frequency = 0
# words = []
# for line in file:
#     line_word = line.lower().split(";")
#     for w in line_word:
#         words.append(w)
# for i in range(0, len(words)):
#     count = 1
#     for j in range(i + 1, len(words)):
#         if (words[i] == words[j]):
#             count = count + 1
#     if (count > frequency):
#         frequency = count
#         frequent_word = words[i]

# test2

# txtFile = open("pwd.txt", encoding="utf8"  )
# word_counter = {}
# for word in txtFile:
#     word.lower().split(".ru;")
#     #txtFile = [word[word.find(";") + 1:-1] for word in words]
#     if len(word) > 0 and word != '\r\n':
#         if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
#             word_counter[word] = 1
#         else:
#             word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1
# for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:10]):
#     print("%s: %s - %s" % (i + 1, word, word_counter[word]))
# def get_10_popular_password(file: str) -> Any:
#     with open("pwd.txt", 'r', encoding='utf-8') as file:
#         s = file.readlines()
#         arr = []
#         for n, i in enumerate(s, start=0):
#             x = i.split(';')
#             print(f'{n}:  {x[-1]}', end=' ')
#             arr.append(x[-1])
#         print('-----------------------')
#         count = Counter(arr)
#         print(count.most_common(10))


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# https://example.com/smth/else заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
#def censor_link(string: str) -> str:


text = [
'www.site.com',
'http://example.su',
'vk.ru',
'https://example.com/smth/else'
'www.ok.ru'
    ]

text[:5] = 5 * ["*****"]
print(text)

# Здесь писать тесты для функций с решениями
def main():
    # arr = ['panamera', 'macan', 'taycan', 'cayenne', 'macan']
    # print(count_unique_elems(arr))
    # print("Most repeated password: " + frequent_word)
    # print("Frequency: " + str(frequency))
    # for i, word in enumerate(sorted(word_counter, key=word_counter.get, reverse=True)[:10]):
    #     print("%s: %s - %s" % (i + 1, word, word_counter[word]))
    # file.close()
    #print(get_10_popular_password(10))
    pass

if __name__ == '__main__':
    main()
