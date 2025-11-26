def razdel(vxod):
    vrem=vxod.split()
    if len(vrem)==2 and vrem[0].isdigit() and vrem[1].isdigit():
        minuti=int(vrem[1])
        chasi=int(vrem[0])
        return(chasi,minuti)
    elif len(vrem)==3 and vrem[0].isdigit() and vrem[2].isdigit() and vrem[1]==":":
        minuti=int(vrem[2])
        chasi=int(vrem[0])
        return(chasi,minuti)
    else:
        return(25,66)
    
def naz_minut(minuta):
        if minuta>=5 and minuta<=20:
            return(str(minuta)+" минут")
        elif minuta%10==1:
            return(str(minuta)+" минута")
        elif minuta%10>=2 and minuta%10<=4:
            return(str(minuta)+" минуты")
        else:
            return(str(minuta)+" минут")
        
def naz_chas(chasi):
    if chasi>=0 and chasi<6:
        vrem_sutok=0
    elif chasi>=6 and chasi<12:
        vrem_sutok=1     
    elif chasi>=12 and chasi<18:
        vrem_sutok=2
    else:
        vrem_sutok=3
        
    if chasi!=12:
        chasi=chasi%12
    if chasi==1:
        return("1 час",vrem_sutok)
    elif chasi>=2 and chasi<=4:
        return(str(chasi)+" часа",vrem_sutok)
    else:
        return(str(chasi)+" часов",vrem_sutok)

vremina_sutok=["ночи","утра","дня","вечера"]
vhodnie_dannie=input("введетите время в формате xx xx либо xx:xx   ")
chas,minut=razdel(vhodnie_dannie)
if chas>=0 and chas<24 and minut>=0 and minut<60:
    if minut==0:
        if chas==0:
            print("полночь")
        elif chas==12:
            print("полдень")
        else:
            chas_text,param_chas=naz_chas(chas)
            print(chas_text,vremina_sutok[param_chas],"ровно")
    else:
        chas_text,param_chas=naz_chas(chas)
        minut_text=naz_minut(minut)
        print(chas_text,minut_text,vremina_sutok[param_chas])
else:
    if  (minut<0 or minut>59) and (chas<0 or chas>23):
        print("Введены не корректные данные")
    elif minut<0 or minut>59:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
    elif chas<0 or chas>23:
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
