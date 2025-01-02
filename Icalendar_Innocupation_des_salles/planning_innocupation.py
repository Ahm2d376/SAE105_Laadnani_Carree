

from datetime import datetime
import os
import sys
from extraction_evenements import extraction_evenements
from trouver_plages_libres import trouver_plages_libres
from creer_html import creer_html




def main():
	"""
Programme principal d'éxecution qui va analyser les plages d'inoccupation des salles à partir du fichier ICS. il est en quelque sorte le programme final qui va utiliser tout les modules
que nous avons crées pour arriver à ses fins.


 
Arguments du programme:
    --salle SALLE           Identifiant de la salle à analyser (ex: "RT14")
    --date-debut DATE      Date de début de l'analyse (format: YYYY-MM-DD)
    --date-fin DATE        Date de fin de l'analyse (format: YYYY-MM-DD)
    --input-file FICHIER   Chemin vers le fichier ICS à analyser
    --output-dir DOSSIER   Dossier où sauvegarder le rapport HTML
 

Exemple d'utilisation:
    python3 planning_innocupation.py --salle RT14 --date-debut 2024-10-01 --date-fin 2024-12-31 
                         --input-file "ADECal (1).ics" --output-dir resultats

Sortie:
    - Crée un fichier HTML dans le dossier HTML    
    - Le rapport liste toutes les plages d'inoccupation par date

"""
   
	
input_file = "ADECal (1).ics"
output_dir = "output"
salle = None
date_debut = None
date_fin = None

    # Récupération des arguments
for i in range(len(sys.argv)):
       if sys.argv[i] == "--salle":
           salle = sys.argv[i + 1]
       elif sys.argv[i] == "--input-file":
           input_file = sys.argv[i + 1]
       elif sys.argv[i] == "--output-dir":
           output_dir = sys.argv[i + 1]
       elif sys.argv[i] == "--date-debut":
           date_debut = datetime.strptime(sys.argv[i + 1], "%Y-%m-%d")
       elif sys.argv[i] == "--date-fin":
           date_fin = datetime.strptime(sys.argv[i + 1], "%Y-%m-%d")

    
with open(input_file, "r") as f:
    lines = f.readlines()

    heures_debut, heures_fin = extraction_evenements(lines, salle)
    plages_libres = trouver_plages_libres(heures_debut, heures_fin)
    plages_filtrees = [p for p in plages_libres if date_debut.date() <= p[0] <= date_fin.date()]

    # Création du fichier HTML
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    html = creer_html(salle, plages_filtrees)
    with open(os.path.join(output_dir, f"plages_libres_{salle}.html"), "w", encoding="utf-8") as f:
        f.write(html)


main()