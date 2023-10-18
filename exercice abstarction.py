from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, couleur, capacite):
            self.marque = marque
            self.couleur = couleur
            self.capacite = capacite
    
       
    @abstractmethod
    def afficher_infos(self):
        pass

class Voiture(Vehicule):
    def __init__(self, marque, couleur, capacite, modele, nombre_de_portes):
        super().__init__(marque, couleur, capacite)
        self.modele = modele
        self.nombre_de_portes = nombre_de_portes

    def afficher_infos(self):
            if self.couleur=="vert":
                self.couleur="la nature"
            if self.couleur=="rouge":
                self.couleur="l'amour"
            if self.nombre_de_portes==2:
                self.nombre_de_portes="sport"
            if self.nombre_de_portes==4:
                self.nombre_de_portes="classique"
            print(f"Voiture {self.marque} {self.modele} couleur: {self.couleur} {self.capacite} places {self.nombre_de_portes} ")   

class Moto(Vehicule):
    def __init__(self, marque, couleur, capacite, cylindre):
        super().__init__(marque, couleur, capacite)
        self.cylindre = cylindre

    def afficher_infos(self):
        print(f"Moto {self.marque} {self.couleur} {self.capacite} places {self.cylindre} cylindres")

# Création d'une instance de la classe Voiture
voiture1 = Voiture("Renault", "vert", 8,1990, 2)
voiture2 = Voiture("Renault", "rouge", 8,1990,4)
# Création d'une instance de la classe Moto
moto = Moto("Honda", "CBF 600", 2, 599)

# Appel de la méthode afficher_infos() sur chaque instance
voiture1.afficher_infos()
voiture2.afficher_infos()
