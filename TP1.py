class Voiture:
    def __init__(self, marque, model, couleur):
        #rendre les attributs prive
        self.__marque = marque
        self.__model = model
        self.__couleur = couleur
v1 = Voiture("Dacia", 1989, "Noir")
    

#getter (accesseurs)
    def get_marque(self):
        return self.__marque
        return self.__model
        return self.__couleur
    def afficher_info(self)
print (v1.__marque)
print (v1.__model)
print (v1.__couleur)
