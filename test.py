class Personne:
    def __init__(self, nom: str, age: int) -> None:
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

humain1 = Personne("Pierre", 16)
humain1.se_presenter()