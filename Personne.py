class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom= nom
        self.__prenom= prenom
        self.__age= age
    def se_presenter(self):
        #attention f avant le message
        return (f"mon nom est {self.__nom} mon prenom est {self.__prenom} mon age est {self.__age}")
P1= Personne("ali", "ahmed", 22)
print (P1.se_presenter())
