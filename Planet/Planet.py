class Planet:
    _idplan = 0
    def __init__(self,nazv,radius,massa,tip,rastdosol):
        self.nazv = nazv
        self.radius = radius
        self.massa = massa
        self.rastdosol = rastdosol
        self.tip = tip
        self.__idplane = _idplan
        
    
    def __str__(self):
        return(f"Планета-'{self.nazv}' Id-'{self.__idplane}'  Радиус планеты-'{self.radius}' Масса-'{self.massa}' Тип планеты-'{self.tip}' Растояние до солнца'{self.rastdosol}'")
    
    def __repr__(self):
        return(f"Planet(name='{self.nazv}', Id='{self.__idplane}', Radius ='{self.radius}', Massa='{self.massa}' Tip='{self.tip}', Rastdo='{self.rastdosol}')")
    def __copy__(self):
        
