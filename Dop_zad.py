from datetime import*
import time

def padezh_minut(minuta):
    if minuta >=5 and minuta <= 20:
        return(" минут")
    elif minuta % 10 == 1:
        return(" минута")
    elif minuta % 10 >= 2  and minuta % 10 <= 4:
        return(" минуты")
    else:
        return(" минут")
    
def naz_minut(minut):
    ed = ("ноль","одна","две","три","четыре","пять","шесть","семь","восемь","девять")
    desitki = ("десять","двадцать","тридцать","сорок","пятьдеят")
    if minut // 10 == 1 and minut % 10 != 0:
        if minut % 10 == 1:
            text = "одиннадцать"
        elif minut % 10 == 2 or minut % 10 == 3 :
            text = ed[minut % 10] + "надцать"
        else:
            a = ed[minut%10]
            a = a[:len(a) - 1]
            text = a + "надцать"
    else:
        if minut // 10 == 0:
            text = ed[minut]
        elif minut % 10 == 0:
            text = desitki[minut // 10 -1]
        else:
            text = desitki[minut // 10 - 1 ] +  " "  + ed[minut % 10]
    text = text + padezh_minut(minut)
    
    return(text)
    
def naz_chas(chas):
    ed = ("ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять")
    if chas // 10 == 1:
        if chas % 10 == 2:
            return("двенадцать часов")
        elif chas % 10 == 1 or chas % 10 == 3:
            return(ed[(chas % 10)] + "надцать часов")
        else:
            a = ed [chas % 10]
            a = a[:len(a) - 1]
            return(a + "надцать часов")
    elif chas // 10 == 2:
        tex = "двадцать " + ed [chas % 10]
    else:
        tex=ed[chas % 10 ]
        
    if chas % 10 == 1:
        return(tex + " час")
    elif chas % 10 >=2 and chas % 10 <=4:
        return(tex + " часа")
    else:
        return(tex + " часов")
print("Вас приветствует программа будильник! Введети время на которое нужно поставить будильник в формате часы минуты")
vhod_dan = input().split()
if len(vhod_dan) == 2 and vhod_dan[0].isdigit()  and vhod_dan[1].isdigit():
    chas = int(vhod_dan[0])
    minuti = int(vhod_dan[1])
    if minuti >= 0 and minuti < 60 and chas>=0 and chas <= 23:
        print("Будильник установлен на",naz_chas(chas),naz_minut(minuti))
        tek_vrem = str(datetime.now())
        tek_vrem = tek_vrem[ tek_vrem.find(" ") : tek_vrem.rfind(":") ]
        tek_chas = int(tek_vrem[ : tek_vrem.find(":")])
        tek_min = int(tek_vrem[ tek_vrem.find(":") + 1:])
        tek_vr_min = tek_chas * 60 + tek_min
        vr_min= chas * 60 + minuti
        razn = vr_min - tek_vr_min
        if razn < 0:
            razn += 1440
        time.sleep(razn * 60)
        print("Дзынь-Дзынь!!")
    else:
        print("Введено неправильное время")
else:
    print("Введены не корректные данные")
"""
Получаем данные от пользователя
Проверяем, что пользователь ввел 2 параметра и оба из них числа
Если введеные данные прошли проверку то:
     Перевести числвое значение времени в текстовое представление
     Вывести: будильник установленн на  (время пользователя в текстовом формате)
     Узнать текущее системное время
     Расчитать разницу между данными пользователя и текущиим системным временем
     Если текущее системное время больше времени данных пользователя:
         Прибавить к разнице 24 часа
    Ожидать расчитанную разницу 
    Вывести: Дзынь-Дзынь!!
Если же данные не прошли проверку:
     Вывести:ошибка, введены не корректные данные
""" 
    
