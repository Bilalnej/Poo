class Cercle:
    def __init__(self, rayon, couleur):
        self.__rayon = rayon
        self.__couleur = couleur
    def aire(self):
        return 3.14*self.__rayon*self.__rayon
    def primetre(self):
        return 2*3.14*self.__rayon

cle = Cercle(25,"red")
print("L'aire est:", cle.aire())
print("Primetre est:", cle.primetre())
   
