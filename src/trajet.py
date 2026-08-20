from datetime import datetime as dt, time
import vehicule

historique = []

class trajet:
  moyen_de_transport = object
  distance = 0
  heure = object
  prix = 0

  def __init__(self, distance, v): # v vehicule du trajet
    self.distance = distance
    self.heure = self.set_heure_trajet()

    self.calculer_prix_trajet(v)
    print(self.afficher_recapitulatif(v))

  def set_heure_trajet(self):
    return dt.now()

  def est_heure_de_pointe(self):
      heure = self.heure.time()

      return (
          time(7, 0) <= heure <= time(8, 45)
          or time(11, 45) <= heure <= time(13, 0)
          or time(17, 0) <= heure <= time(19, 0)
      )

  def calculer_prix_trajet(self, v):
      self.prix = v.tarif_de_base + v.prix_au_km * self.distance

      if self.est_heure_de_pointe():
          self.prix += self.prix * v.majoration_heure_de_pointe

      self.arrondir_prix()
      return self.prix

  def arrondir_prix(self):
     self.prix = round(self.prix / 25) * 25

  def afficher_recapitulatif(self, v):
    return(f"""
    Moyen de transport : {v.nom}
    Distance du trajet : {self.distance}
    Heure de Pointe :    {"Oui" if self.est_heure_de_pointe() else "Non"}
    Prix du trajet :     {self.prix}
    """)

  def ajouter_a_historique(self, v): # nom:  nom du moyen de déplacement 
    self.moyen_de_transport = v.nom
    historique.append(self)

  def afficher_historique():
     for t in historique:
        print(t.afficher_recapitulatif(self, v))
    
