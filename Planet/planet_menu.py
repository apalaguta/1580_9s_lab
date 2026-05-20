from planeti import Planet
import csv

planets = []

def dobavl():
    nazv = input("Введедите название планеты - ")
    radius = input("Введети радус планеты (в км) - ")
    while not(radius.isdigit()):
        radius = input("Введены не корректные данные. Повторите попытку - ")
    massa = input("Введите массу планеты в кг - ")
    while not(massa.isdigit()):
        massa = input("Введенны не корректные данные. Повторите попытку - ")
    sp_vidov = ["газовый гигант","каменная","ледяной гигант"]
    print("Виды планет: газовый гигант, каменная, ледяной гигант")
    vid = input("Введите тип планеты из списка : ").lower()
    while vid not in sp_vidov:
        vid = input("Введенный тип планеты отсутсвует. Повторите попытку - ").lower()
    rast = input("Введети расстояние планеты до солнца (в млн км) - ")
    while not(rast.isdigit):
        rast = input("Введены не корректные данные. Повторите попытку - ")
    planeta = Planet(nazv,radius,massa,vid,rast)
    planets.append(planetа)
    print("Новая планета усаешно создана")
    
def delet():
    nazvanie = input("Введите название планеты, которую хотите удалить - ")
    for i in planets:
        if i.nazv.lower() == nazvanie:
            planets.remove(i)
            print("Планета успешно удалена")
            return
    print("Планета не найдена.")
    return
        
def vigruz():
    with open("baza_danix.txt", 'w', encoding='utf-8') as zapis:
        for i in planets:
            print(f"{i.nazv}:{i.radius},:{i.massa}:{i.tip}:{i.rastdosol}",file = zapis)
    print("База данных экспоортированва в текстовый файл")
    
def zagrux():
    with open("baza_danix.txt", 'r', encoding='utf-8') as zapis:
        for i in zapis:
            new_planeta = Planet(i.split(":"))
            planets.append(new_planet)
        print("База данных выгружена")
        
def csv():
    with open('baza_danix.csv', 'w', newline='') as csv_file:
        zapis = csv.writer(csv_file)
        zapis.writerows(planets)
    
def menu():
    print("----Меню----")
    print("1. Добавление новой планеты")
    print("2. Удаление планеты")
    print("3. Загрузка планет в файл")
    print("4. Получение планет из файла")
    print("5. Экспорт в CSV")
    print("6. Сортировка планет")
    print("7. Поиск")
    print("8. Выход")
    
    vibor = input("Напишите выбранный пункт : ")
    while not(vibor in ["1","2","3","4","5","6","7","8"]):
        print("Не правильный выбор, повторите попытку")
        vibor = input("Повторный выбор: ")
    if vibor == "1":
        dobavl()
    if vibor == "2":
        delet()
    if vibor == "3":
        vigruz()
    if vibor == "4":
        zagrux()
    if vibor == "5":
        csv()
        
a = menu()
