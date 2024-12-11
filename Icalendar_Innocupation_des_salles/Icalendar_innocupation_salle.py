#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:27:07 2024

@author: etudiant
"""

import datetime

f = open("/home/etudiant/SAE105_Laadnani_Carree/data/ADECalBUT1.ics", 'r')
lines = f.readlines()

format_str = "%Y%m%dT%H%M%SZ"






def extraction_de_donnees(salle):
    
    """
       Fonction qui prend une salle en parametre et qui en ressort deux listes,
        une avec les dates de debuts de chaques cours,
        une avec les dates de fins de chaques cours.
        
    """
    heur_de_debut, heur_de_fin, location, dt_start, dt_end = [], [], [], [], []
    
    for i in range (len(lines)):
        if "LOCATION" in lines[i]:
            location.append(lines[i])
            print(location)
        if "DTSTART" in lines[i]:
            dt_start.append(lines[i])
        if "DTEND" in lines[i]:
            dt_end.append(lines[i])  
            
            
    for i in range(len(location)):
        if salle in location[i]:
            heur_de_debut.append(dt_start[i])
            heur_de_fin.append(dt_end[i])
       
    return heur_de_debut, heur_de_fin



    
    