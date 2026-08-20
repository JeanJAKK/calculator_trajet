import vehicule as vh
import trajet

while True:
  print("#" * 50)
  print("Choisir un moyen de transport\n")
  print("1. Zémidjan")
  print("2. Taxi")
  print("3. Quitter")
  print("#" * 50 + "\n")

  try:
    choix = int(input("\nVotre choix :"))

    if choix in (1, 2):
      distance_trajet = float(input("\nLa distance du trajet :"))

  except Exception as e:
    print(f"Erreur lors de la saisie : {e}")


  if choix == 1:
    trajet.trajet(distance_trajet, vh.zed)
  elif choix == 2:
    trajet.trajet(distance_trajet, vh.taxi)
    
  elif choix == 3:
    print("Au revoir")
    break
  else :
    print("Choix invalide")