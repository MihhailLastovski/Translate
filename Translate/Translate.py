from random import*
from module1 import*
ang=[]
rus=[]
filetolist("ang.txt",ang)
filetolist("rus.txt",rus)
while 1:
    print("1. Вывод всех слов")
    print("2. Перевод")
    print("3. Добавить новое слово")
    print("4. Исправление ошибок")
    print("5. Тест")
    print("6. Озвучить слово")
    print("7. Выход")
    choise=input("Выберите пункт: ")
    print()
    check(choise)
    if str(choise)== "1":
        for i in range(len(ang)):
            print(rus[i]+"-"+ang[i])
        print()
    elif str(choise)== "2":
        word=input("Введите слово, которое хотите перевести: ").lower()
        if word not in ang and word not in rus:
            print(f'Слово "{word}" нет в словаре')
        elif word in ang:
            print(f"{word} - {rus[ang.index(word)]}")
        elif word in rus:
            print(f"{word} - {ang[rus.index(word)]}")
    elif str(choise)== "3":
        word=input("Введите слово на русском, которое хотите добавить: ")
        wordeng=input("Введите его перевод: ")
        if word in rus or wordeng in ang:
            print(f'Слово "{word}" уже есть в словаре')
        else:
            new_word("ang.txt",wordeng,ang)
            new_word("rus.txt",word,rus)
    elif str(choise)== "4":
        wrong=input("Какое слово неправильное ang/rus?: ")
        if wrong=="ang":
            word=input("Напишите слово с ошибкой в английском словаре: ")
            correct(word,ang)
        elif wrong=="rus":
            word=input("Напишите слово с ошибкой в русском словаре: ")
            correct(word,rus)
        else:
            print("Вы ввели некорректно!")
    elif str(choise)=="5":
        print("Напишите правильный перевод слова")
        result=0
        for i in range(len(rus)):
            number=randint(1,2)
            if number==1:
                result=test(result,rus,ang)
            else:
                result=test(result,ang,rus)
        grade=result*100/len(rus)
        print(f"Вы ответили правильно на {result} из {len(rus)}")
        if grade>=90:
            print("Ваша оценка: 5")
        elif grade>=75 and grade<=90:
            print("Ваша оценка: 4")
        elif grade>=50 and grade<=75:
            print("Ваша оценка: 3")
        else:
            print("Ваша оценка: 2")
    elif str(choise)=="6":
        sound()
    elif str(choise)=="7":
        break