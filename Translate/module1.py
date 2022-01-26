from random import*
import os
import gtts
from playsound import playsound
def filetolist(f:str,l_f:list):
    """Переносит данные из файлы в список
    :param str f: файл
    :param list l_f: список, в который будут вноситься данные
    :rtype: list
    """
    fail=open(f,"r",encoding="utf-8-sig")
    for rida in fail:
        l_f.append(rida.strip())
    fail.close()
    return l_f

def check(x:str):
    """Функция проверки, если пользователь ввел не то значение
    Применяется только к типу str
    :param str x: текст, который нужно проверить
    """
    while x not in ["1","2","3","4","5","6","7"]:
        try:
            x=input("Вы ввели неверное значение! Попробуйте еще раз: ")
        except:
            TypeError

def new_word(f:str,word:str,l_word:list):
    """Добавляет новое слово в список и в файл
    :param str f: файл
    :param str word: слово
    :param list l_word: список
    """
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(word + "\n")
    l_word.append(word)

def correct(word:str,l:list):
    """Заменяет слово в списке на новое (с файлом сделать не получилось)
    :param str word: слово, которое вы хотите изменить
    :param list l: список
    """
    for i in range(len(l)):
        if l[i]==word:
            newword=word.replace(word,input("Правильное слово: "))
            l.insert(i,newword)
            l.remove(word)
            print(f'Старое слово "{word}" заменилось на "{newword}"')

def test(result:int,l:list,l2:list):
    """Функция берет случайное слово из списка. Пользователь вводит перевод, затем функция сравнивает его
    :param int result: количество правильных ответов
    :param list l: русский словарь
    :param list l2: английский словарь
    :rtype: int
    """
    word=choice(l)
    answer=input(f"{word} --> ")
    if answer in l2: 
        if l2.index(answer) == l.index(word):
            result += 1
            print("Правильно")
    else:
        print("Неправильно")
    return result

def sound():
    """Функция для озвучивания текста, введенного пользователем (работает один раз, потом появляется ошибка)
    """
    print("На каком языке будет озвучка слова? rus/eng")
    valik=input("")
    if valik=="rus":
        text=input("Введите слово для озвучки на русском: ")
        tts=gtts.gTTS(text, lang="ru")
        tts.save("sound_.mp3")
        playsound("sound_.mp3")
    elif valik=="eng":
        text=input("Введите слово для озвучки на английском: ")
        tts=gtts.gTTS(text, lang="en")
        tts.save("wordsound.mp3")
        playsound("wordsound.mp3")
    else:
        print("Вы ввели неправильно")