Voici le tutoriel d’installation et d’utilisation de notre programme 
---------------------------------------------------------------------

Dézipper l’archive SAE105_Laadnani_Carree dans votre répertoire personnel.


 Une fois l’archive dézippée il faudra vous placer dans le répertoire : 

SAE105_Laadnani_Carree/Icalendar_Innocupation_des_salles

Une fois que vous vous trouvez dans le répertoire contenant le programme python il vous faudra exécuter la commande suivante :

python3 planning_innocupation.py --salle “salle de votre choix, ex : RT04”  --date-debut “année-mois-jour” --date-fin “année-mois-jour” --input-file "Chemin  vers le fichier d’entré Icalendar à exploiter" --output-dir "Chemin vers le répertoire de sortie où l’on veut sauvegarder nos pages HTML"

Exemple d’une commande : 

python3 planning_inoccupation.py --salle RT14 --date-debut 2024-10-13 --date-fin 2025-04-10 --input-file ~/SAE105_Laadnani_Carree/data/ADECal (1).ics --output-dir ~/SAE105_Laadnani_Carree/html/

Une fois que la commande a été exécuté avec les paramètres voulus, un fichier HTML contenant les résultats sera créer dans le répertoire de sortie spécifié





Pour l’arborescence du projet : 

Vous retrouverez le fichier Icalendar d’emploi du temps des salles dans le répertoire “data”.

L’ensemble de la documentation du projet dans le répertoire “docs” qui contiendra la page html générée par sphinx ainsi que le diagramme UML de cas d’utilisation

Le programme se retrouvera quant à lui dans le répertoire  “Icalendar_Inoccupation_des_salles”. Vous pourrez y retrouver tous nos modules ainsi que le programme principal.

Pour plus d'informations, je vous invite à consulter la documentation du projet.
