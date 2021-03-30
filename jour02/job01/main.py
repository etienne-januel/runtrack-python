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

john = Personne()
john.sePresenter()

jeff = Personne('Jeff', 'Bezos')
jeff.sePresenter()
jeff.set_nom('Pesos')
jeff.sePresenter()