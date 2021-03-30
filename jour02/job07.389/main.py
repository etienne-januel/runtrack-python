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


class Auteur(Personne):
  def __init__(self, prenom, nom):
    self.collection = []
    Personne.__init__(self, prenom, nom)

  def listerCollection(self):
    for livre in self.collection :
      print(livre.get_titre())

  def ecrireUnLivre(self, titre):
    self.ajouterLivreDansCollection(Livre(titre, self))

  def ajouterLivreDansCollection(self, livre):
    self.collection.append(livre)

  def get_collection(self):
    return self.collection


class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def get_titre(self):
    return self.titre


class Client(Personne):
  def __init__(self, prenom, nom):
    self.collection = []
    Personne.__init__(self, prenom, nom)

  def afficherCollection(self):
    print('--- Inventaire Client: ')
    for livre in self.collection:
      print(livre['titre'])

  def remove_collection(self, item):
    self.collection.remove(item)

  def set_collection(self, item):
    self.collection.append(item)
  
  def get_collection(self):
    return self.collection


class Bibliotheque:
  def __init__(self, nom):
    self.nom = nom
    self.catalogue = []

  def acheterLivre(self, auteur: Auteur, nomLivre, quantiteLivre):
    if any(nomLivre in livre.get_titre() for livre in auteur.get_collection()):
      item = dict()
      item['titre'] = nomLivre
      item['quantite'] = quantiteLivre
      self.catalogue.append(item)

  def inventaire(self):
    if len(self.catalogue) != 0:
      print('--- Inventaire Bibliothèque: ')
      for item in self.catalogue:
        print(item['titre'] + ' *' + str(item['quantite']))

  def louer(self, client: Client, nomLivre):
    if len(self.catalogue) != 0:
      for livre in self.catalogue:
        if nomLivre == livre['titre']:
          if livre['quantite'] > 0:
            client.set_collection(livre)
            livre['quantite'] -= 1

  def rendreLivres(self, client: Client):
    for livreClient in client.get_collection():
      for livreBibliotheque in self.catalogue:
        if livreBibliotheque['titre'] == livreClient['titre']:
          client.remove_collection(livreClient)
          livreBibliotheque['quantite'] += 1
    

zola = Auteur('Emile', 'Zola')
zola.ecrireUnLivre('En Bande Organisée')
zola.ecrireUnLivre('Dor et de platine')

clinss = Client('Shun', 'Lassal')
alcasar = Bibliotheque('alcasar')
alcasar.acheterLivre(zola, 'En Bande Organisée', 2)
alcasar.acheterLivre(zola, 'Dor et de platine', 1)
alcasar.inventaire()

alcasar.louer(clinss, 'En Bande Organisée')
clinss.afficherCollection()

alcasar.inventaire()

alcasar.rendreLivres(clinss)

clinss.afficherCollection()
alcasar.inventaire()
clinss.sePresenter()