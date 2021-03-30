# Personne
class Personne:
  def __init__(self, prenom = 'John', nom = 'Doe'):
    self.prenom = prenom
    self.nom = nom

  def sePresenter(self):
    print('Moi ' + self.nom + ' ' + self.prenom)

  #Getters and Setters
  def get_nom(self):
    return self.nom

  def set_nom(self, nom):
    self.nom = nom

  def get_prenom(self):
    return self.prenom

  def set_prenom(self, prenom):
    self.prenom = prenom


# Auteur
class Auteur(Personne):
  def __init__(self, prenom, nom):
    self.collection = []
    Personne.__init__(self, prenom, nom)

  def listerCollection(self):
    for livre in self.collection :
      print(livre.afficherDetails())

  def ecrireUnLivre(self, titre):
    self.ajouterLivreDansCollection(Livre(titre, self))

  def ajouterLivreDansCollection(self, livre):
    self.collection.append(livre)

# Livre
class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def afficherDetails(self):
    return self.titre


zola = Auteur('Emile', 'Zola')
zola.ecrireUnLivre('En Bande Organisée')
zola.ecrireUnLivre('Dor et de platine')
zola.listerCollection()