class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def se_presenter(self):
        return (f"Mon nom est {self.__nom} mon prénom est: {self.__prenom} mon âge est: {self.__age}")

P1 = Personne("Ali", "hazoka", "23")

print(P1.se_presenter())

