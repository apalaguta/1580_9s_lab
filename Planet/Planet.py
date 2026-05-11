class Planet:
    idplan = 0
    def __init__(self,nazv,radius,massa,tip,rastdosol):
        self.nazv = nazv
        self.radius = radius
        self.massa = massa
        self.rastdosol = rastdosol
        self.tip = tip
        self.idplane = Planet.idplan
        print("Cоздание планеты с ID -",self.idplane)
        Planet.idplan += 1
        
    
    def __str__(self):
        return(f"Планета - {self.nazv}\nId - {self.idplane}\nРадиус планеты - {self.radius} км\nМасса - {self.massa} кг\nТип планеты - {self.tip}\nРастояние до солнца {self.rastdosol} млн км")
    def __repr__(self):
        return(f"Planet(name='{self.nazv}', Id='{self.__idplane}', Radius ='{self.radius}', Massa='{self.massa}' Tip='{self.tip}', Rastdo='{self.rastdosol}')")
    def __copy__(self):
        return(self.nazv,self.radius,self.radius, self.massa, self.tip,self.rastdosol)
    def __del__(self):
        print("Удаление планеты с ID -",self.idplane)
    
    def __lt__(self,other):
        return(self.rastdosol < other.rastdosol)
    def __gt__(self,other):
        return(self.rastdosol > other.rastdosol)
    def __eq__(self,other):
        return(self.nazv == other.nazv)
