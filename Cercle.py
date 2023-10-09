class cercle:
    def __init__(self, rayon, couleur):
       self.__rayon = rayon
       self.__couleur = couleur
    def aire(self):
     return  3.14*self.__rayon*self.__rayon

cercle1=cercle(10,"rouge")
print(cercle1.aire())

