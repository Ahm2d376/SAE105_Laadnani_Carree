

from datetime import datetime
import os
import sys
from extraction_evenements import extraction_evenements
from trouver_plages_libres import trouver_plages_libres
from html import creer_html

# Initialisation des variables
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



# Traitement
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