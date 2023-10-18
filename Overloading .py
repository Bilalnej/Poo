#ABSTRACTION
from abc import ABC, abstractmethod
class Vehicule(ABC):
    def __init__(self, marque, couleur, capacite):
        self.marque = marque
        self.couleur = couleur
        self.capacite = capacite
    @abstractmethod   
    def afficherInfo(self):
        pass
    
class Voiture(Vehicule):
    def __init__(self, marque, couleur, capacite,modele, nombreDePortes):
        super().__init__( marque, couleur, capacite)
        self.modele = modele
        self.NombreDePort = nombreDePortes
        
    def afficherInfo(self):
        if self.couleur == "rouge":
            print(f" voiture {self.marque}, modele {self.modele},de couleur: Royal, capacite: {self.capacite},{self.NombreDePort}")
        elif self.couleur == "vert":
            print(f" voiture {self.marque}, modele {self.modele},de couleur: La nature, capacite: {self.capacite},{self.NombreDePort}")
        else:
            print(f" voiture {self.marque}, modele {self.modele},de couleur: {self.couleur}, capacite: {self.capacite},{self.NombreDePort}")
        
        
class Moto(Vehicule):
    def __init__(self, marque, couleur, capacite, cylindre):
        super().__init__( marque, couleur, capacite)
        self.cylindre = cylindre
        
    def afficherInfo(self):
        print(f"cet moto {self.marque},de couleur {self.couleur},de capacite {self.capacite}, numbre de cylindre {self.cylindre}")
        
        
Car01 = Voiture("peugeot", "rouge", "2.0L", 2022, "5 Port")
Car02 = Voiture("peugeot", "vert", "2.0L", 2022, "5 Port")
Moto01 = Moto("sym", "vert", "1.5L", "4 cylindre")

Car01.afficherInfo()
Car02.afficherInfo()
Moto01.afficherInfo()


































"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre_point):
        return Point(self.x + autre_point.x, self.y + autre_point.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
point04 = Point(9, 6)
point3 = point1 + point2+point04
print(point3.x, point3.y)








class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    def __str__(self):
        return "({1}, {0})".format(self.x, self.y)
 
    def __add__(self, p):
        a = self.x + p.x
        b = self.y + p.y
        return Point(a, b)
 
 
p1 = Point(2, 4)
p2 = Point(9, 5)
p5 = Point(10, 0)
p3 = p1+p5+p2"""




"""class Personne:
    def __init__(self,nom):
        self.nom=nom
     
    def affiche(self):
        print("je suis une personne")
 
class Etudiant(Personne):
    def __init__(self,nom,cne):
        super().__init__(nom)  
        self.cne=cne
     
    def affiche(self):
        print("je suis un etudiant")
 
class Professeur(Personne):
    def __init__(self,nom,ppr):
        super().__init__(nom)  
        self.ppr=ppr
     
    def affiche(self):
        print("je suis un professeur")
 
 
def ShowMe(obj):
    obj.affiche()
 
etd=Etudiant('Kayouh',123444)
prf=Professeur('ESSADDOUKI',123123123)
 
ShowMe(etd)
ShowMe(prf)"""
