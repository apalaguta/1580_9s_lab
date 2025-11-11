def razdel(vrem):
    minuti=vrem[vrem.find(":")+1:]
    chasi=vrem[:vrem.find(":")]
    minuti=int(minuti)
    chasi=int(chasi)
    return(chasi, minuti)
def naz_minut(minuta):
    if minuta==0:
        return("ровно",2)
    else:
        if minuta>=5 and minuta<=20:
            return(str(minuta)+" минут",1)
        elif minuta%10==1:
            return(str(minuta)+" минута",1)
        elif minuta%10>=2 and minuta%10<=4:
            return(str(minuta)+" минуты",1)
        else:
            return(str(minuta)+" минут",1)
def naz_chas(chasi):
    if chasi==0:
        vrem_sutok=0
    elif chasi>=1 and chasi<=5:
        vrem_sutok=1
    elif chasi>=6 and chasi<=11:
        vrem_sutok=2 
    elif chasi==12:
        vrem_sutok=3    
    elif chasi>=13 and chasi<=17:
        vrem_sutok=4
    else:
        vrem_sutok=5
    if chasi!=12:
        chasi=chasi%12
    if chasi==1:
        return("1 час",vrem_sutok)
    elif chasi>=2 and chasi<=4:
        return(str(chasi)+" часа",vrem_sutok)
    else:
        return(str(chasi)+" часов",vrem_sutok)

vremina_sutok=["ночи","ночи","утра","дня","дня","вечера"]
a=input()
chas,minut=razdel(a)
if chas>=0 and chas<24 and minut>=0 and minut<61:
    minut_text,param_min=naz_minut(minut)
    chas_text,param_chas=naz_chas(chas)
    if param_min==2 and param_chas==0:
        print("полночь")
    elif param_min==2 and param_chas==3:
        print("полдень")
    elif param_min==2:
        print(chas_text,vremina_sutok[param_chas],"ровно")
    else:
        print(chas_text,minut_text,vremina_sutok[param_chas])
else:
    if chas<0 or chas>23:
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
    if minut<0 or minut>61:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59")
