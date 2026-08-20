# Constantes
TARIF_DE_BASE_ZEMIDJAN = 150
TARIF_DE_BASE_TAXI = 200
PRIX_AU_KM_TAXI = 100
PRIX_AU_KM_ZEMIDJAN = 75
TAUX_DE_MAJORATION_TAXI = 0.25
TAUX_DE_MAJORATION_ZEMIDJAN = 0.15

class vehicule:
  nom = ""
  tarif_de_base = 0
  prix_au_km = 0
  majoration_heure_de_pointe = 0

  def __init__(self, nom, tarif_base, prix, majoration):
    self.nom = nom
    self.tarif_de_base = tarif_base
    self.prix_au_km = prix
    self.majoration_heure_de_pointe = majoration

# Creation des objets zed et taxi
zed = vehicule("Zémidjan", TARIF_DE_BASE_ZEMIDJAN, PRIX_AU_KM_ZEMIDJAN, TAUX_DE_MAJORATION_ZEMIDJAN)
taxi = vehicule("Taxi", TARIF_DE_BASE_TAXI, PRIX_AU_KM_TAXI, TAUX_DE_MAJORATION_TAXI)