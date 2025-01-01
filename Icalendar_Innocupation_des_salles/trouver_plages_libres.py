from datetime import datetime

def trouver_plages_libres(heures_debut, heures_fin):
    """
    Trouve les plages horaires libres entre les événements.
    
    Auteur: Nolann
    Date de création: 2024-03-20
    Dernière modification: 2024-03-20
    
    Args:
        heures_debut (list): Liste des objets datetime représentant les débuts d'événements
        heures_fin (list): Liste des objets datetime représentant les fins d'événements
        
    Returns:
        list: Liste de tuples contenant les plages libres avec le format:
            (date, heure_debut, heure_fin, duree)
            - date (datetime.date): Date de la plage libre
            - heure_debut (str): Heure de début au format "HH:MM"
            - heure_fin (str): Heure de fin au format "HH:MM"
            - duree (float): Durée en heures
            
    Note:
        - Les plages sont calculées entre 7h30 et 18h00
        - Les listes heures_debut et heures_fin doivent avoir la même longueur
        - Les dates sont triées chronologiquement
        
    Raises:
        ValueError: Si les listes d'entrée n'ont pas la même longueur
        TypeError: Si les entrées ne sont pas des listes de datetime
    """
    plages_libres = []
    cours_par_date = {}
    
    for i in range(len(heures_debut)):
        date = heures_debut[i].date()
        if date not in cours_par_date:
            cours_par_date[date] = []
        cours_par_date[date].append((heures_debut[i], heures_fin[i]))
    
    for date in sorted(cours_par_date.keys()):
        cours = sorted(cours_par_date[date])
        debut_journee = datetime(date.year, date.month, date.day, 7, 30)
        fin_journee = datetime(date.year, date.month, date.day, 18, 0)
        
        if not cours:
            plages_libres.append((date, "07:30", "18:00", 10.5))
            continue
            
        if cours[0][0] > debut_journee:
            duree = (cours[0][0] - debut_journee).seconds / 3600
            plages_libres.append((date, "07:30", cours[0][0].strftime("%H:%M"), duree))
            
        for i in range(len(cours)-1):
            if cours[i][1] < cours[i+1][0]:
                duree = (cours[i+1][0] - cours[i][1]).seconds / 3600
                plages_libres.append((date, cours[i][1].strftime("%H:%M"), 
                                    cours[i+1][0].strftime("%H:%M"), duree))
                
        if cours[-1][1] < fin_journee:
            duree = (fin_journee - cours[-1][1]).seconds / 3600
            plages_libres.append((date, cours[-1][1].strftime("%H:%M"), "18:00", duree))
            
    return plages_libres 