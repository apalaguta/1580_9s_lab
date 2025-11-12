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
    print("Введены не корректные данные")
