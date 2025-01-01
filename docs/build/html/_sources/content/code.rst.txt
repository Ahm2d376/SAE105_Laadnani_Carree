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

Module d'extraction des évènements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: extraction_evenements.extraction_evenements
   

Module de calcul des plages libres
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: trouver_plages_libres.trouver_plages_libres
   





