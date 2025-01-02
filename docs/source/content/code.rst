Innocupation des salles
=======================

Introduction
------------

Ce programme permet de trouver les plages d'innocupation des salles du département et de les organiser dans un tableau qui sera affiché grâce à une page HTML. Nous pourront choisir la salle qui nous intéresse mais aussi choisir deux dates entre lequel nous voulont connaître les plages d'innocupation ainsi que leurs durée.

Utilisation du programme
------------------------

Pour utiliser ce programme, suivez ces étapes :

1. Il nous faudra python installé sur le PC.
2. Il faudra ce placer dans le répertoire contenant le programme.
3. Exécuter le programme principal avec la commande suivante :

   python3 planning_innocupation.py --salle RTxx --date-debut AAAA-MM-J --date-fin AAAA-MM-J --input-file ~/SAE105_Laadnani_Carree/data/ADECal\ \(1\).ics --output-dir ~/SAE105_Laadnani_Carree/html/

      

4. Une fois que cela est fait une page HTML contenant les résultats sera placée dans le répertoire HTML.

Description des modules
-----------------------

Module principal (planning_innocupation.py)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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







Module d'extraction des évènements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: extraction_evenements.extraction_evenements






   

Module de calcul des plages libres
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: trouver_plages_libres.trouver_plages_libres





Module de génération des pages HTML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. automodule:: creer_html.creer_html

.. autofunction:: creer_html.convertir_duree







   





