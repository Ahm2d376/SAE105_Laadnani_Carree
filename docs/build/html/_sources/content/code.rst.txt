Innocupation des salles
=======================

Introduction
------------

Ce programme permet de trouver les plages d'innocupation des salles du département et de les organiser dans un tableau qui sera affiché grâce à une page HTML. Nous pourront choisir la salle qui nous intéresse mais aussi choisir deux dates entre lequel nous voulont connaître les plages d'innocupation ainsi que leurs durée.

Utilisation du programme
------------------------

Pour utiliser ce programme:

1. Il nous faudra python installé sur le PC.
2. Il faudra ce placer dans le répertoire contenant le programme.
3. Exécuter le programme principal avec la commande suivante :

   python3 planning_innocupation.py --salle RTxx --date-debut AAAA-MM-J --date-fin AAAA-MM-J --input-file "chemin vers le fichier Icalendar" --output-dir "chemin vers le répertoire où vous voulez sauvegarder votre page HTML"

      

4. Une fois que cela est fait une page HTML contenant les résultats sera placée dans le répertoire HTML.

Documentations des fonctions des modules
----------------------------------------

Module principal (planning_innocupation.py)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: planning_innocupation.main







Module d'extraction des évènements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: extraction_evenements.extraction_evenements



.. autofunction:: extraction_evenements.ajuster_heure


   

Module de calcul des plages libres
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: trouver_plages_libres.trouver_plages_libres





Module de génération des pages HTML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. autofunction:: creer_html.creer_html

.. autofunction:: creer_html.convertir_duree








   





