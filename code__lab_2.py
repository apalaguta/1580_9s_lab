import random

def sozd():
    print("Вы можете создать список вручную(для этого введите цифру 1) или программа может создать список, а вы потом его измените(для этого введите цифру 2)")
    typ_spiska = input()
    while typ_spiska != "1" and typ_spiska != "2":
        print("Введенно не корректное значение, повторите попытку")
        typ_spiska = input()
        
    if typ_spiska == "1":
        print("Введите список")
        prov = True
        odno_chislo = True
        sp = input().split()
        while prov:
            odno_chislo = True
            if len(sp) == 0:
                print("Введен пустой список, повторите попытку")
                odno_chislo = False
            else:
                for i in sp:
                    if not(i.isdigit() or (i[0] == "-" and i[1:].isdigit())):
                        print(i,"Не является числом") 
                        odno_chislo = False
                        
            if odno_chislo:
                prov = False
            else:
                print("Повторите попытку")
                sp = input().split()
                
        sp = list(map(int,sp))
        return(sp)
            
    elif typ_spiska == "2":
        colvo = input("Сколько чисел будет в списке? ")
        while not(colvo.isdigit()):
            print("Введенно некорректное значение повторите попытку")
            colvo=input()
        colvo=int(colvo)
        sp = [random.randint(0, 99) for _ in range(colvo)]
        print("Созданный список - ", *sp)
        print("Если он вас не устраивает введите порядковый номер(нумерация начинаеться с нуля) и значение, если все устраивает введите 0")
        
        a = input().split()
        
        while not(len(a) == 1 and a[0] != "0") :
            if not(len(a) == 2 and (a[0].isdigit() or (a[1][0] == "-" and i[1][1:].isdigit())) and a[0].isdigit() and int(a[0]) < colvo):
                print("Не корректный ввод")
            else:
                sp[int(a[0])] = int(a[1])
                print("Измененый список", *sp)
            print("Если он вас не устраивает введите порядковый номер(нумерация начинаеться с нуля) и значение, если все устраивает введите 0")
            a = input().split()
    return(sp)

def buble_s(bu):
    pere_b = 0
    srav_b = 0
    dl_b = len(bu)
    for i in range(dl_b - 1):
        for j in range(dl_b - i - 1):
            srav_b += 1
            if bu[j] > bu[j + 1]: 
                pere_b += 1
                bu[j], bu[j + 1] = bu[j + 1], bu[j]  
    return(pere_b,srav_b,bu)

def selection_s(sel):
    pere_s = 0
    srav_s = 0
    dl_s = len(sel)
    for i in range(dl_s - 1):
        mn = i
        for j in range(i + 1, dl_s):
            srav_s += 1
            if sel[j] < sel[mn]:
                mn = j
        if mn != i: 
            pere_s += 1
            sel[i], sel[mn] = sel[mn], sel[i]
    return(pere_s,srav_s,sel)

def rasch(ra):
    peres_r = 0
    srav_r = 0
    dl = len(ra)
    rast = dl - 1
    while rast >= 1:
        nom = 0
        while nom + rast <dl:
            srav_r += 1
            if ra[nom] >= ra[nom+rast]:
                ra[nom],ra[nom+rast] = ra[nom+rast],ra[nom]
                peres_r += 1
            nom += 1
        rast = int(rast / 1.3)
    return(peres_r,srav_r,ra)

def main():
    print("Вас приветствует программа сортировка")
    print("У нас есть два режима: Демонстративный и Интерактивный")
    print("Для Демонстративного режима введите 1, для Интерактивного режима 2, для выхода 0")
    rezim=input()
    while rezim != "0":
        if rezim != "1" and rezim != "2":
            print("Введены не корректные данные, попробуйте занвово")
            rezim = input()
            continue
        else:
            if rezim == "1":
                print("Вы выбрали Демонстративный режим")
                colvo_chisel = input("Введите количество чисел ")
                while not(colvo_chisel.isdigit()):
                    print("Введенно не корректнрое значение, повторите попытку")
                    colvo_chisel = input()
                spisok =  [random.randint(0, 99) for _ in range(int(colvo_chisel))]
                print("Сгенированный список:", *spisok)
            if rezim == "2":
                print("Вы выбрали Интерактивный режим")
                spisok = sozd()
            rasc = rasch(spisok.copy())
            buble = buble_s(spisok.copy())
            select = selection_s(spisok.copy())
            dlin_vtor_ctolb = max(len(str(rasc[1])), len(str(buble[1])), len(str(select[1])), 19)
            dlin_treti_ctolb = max(len(rasc[2]), len(buble[2]), len(select[2]), 16)
            print("")
            print("Отсортированный массив:",*select[2])
            print("-"*(21 + dlin_vtor_ctolb+ dlin_treti_ctolb))
            print("Метод сортировки|","кол-во перестановок".rjust(dlin_vtor_ctolb),"|","кол-во сравнений".rjust(dlin_treti_ctolb))
            print("-"*(21 + dlin_vtor_ctolb+ dlin_treti_ctolb))
            print("Пузырьковая".rjust(16)+"|",str(buble[0]).rjust(dlin_vtor_ctolb),"|",str(buble[1]).rjust(dlin_treti_ctolb))
            print("-"*(21 + dlin_vtor_ctolb+ dlin_treti_ctolb))
            print("Расческой".rjust(16)+"|",str(rasc[0]).rjust(dlin_vtor_ctolb),"|",str(rasc[1]).rjust(dlin_treti_ctolb))
            print("-"*(21 + dlin_vtor_ctolb+ dlin_treti_ctolb))
            print("Выбором".rjust(16)+"|",str(select[0]).rjust(dlin_vtor_ctolb),"|",str(select[1]).rjust(dlin_treti_ctolb))
            print("-"*(21 + dlin_vtor_ctolb+ dlin_treti_ctolb))
if __name__ == "__main__":
    main()
