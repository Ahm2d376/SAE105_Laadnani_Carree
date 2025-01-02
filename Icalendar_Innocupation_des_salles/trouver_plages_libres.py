
from datetime import datetime, timedelta

def trouver_plages_libres(heures_debut, heures_fin):
    """
    Trouve et calcule toutes les plages horaires libres entre les événements donnés.

    Cette fonction analyse les événements fournis et détermine les périodes d'inoccupation
    entre 7h30 et 18h00 pour chaque jour. Elle prend en compte :
    - Les plages libres en début de journée (avant le premier cours)
    - Les plages libres entre les cours
    - Les plages libres en fin de journée (après le dernier cours)
    - Les journées complètement libres

    Args:
        heures_debut (list[datetime]): Liste des dates et heures de début des événements
        heures_fin (list[datetime]): Liste des dates et heures de fin des événements

    Returns:
        list[tuple]: Liste des plages libres, chaque plage étant un tuple contenant :
            - date (datetime.date): La date de la plage libre
            - heure_debut (str): L'heure de début au format "HH:MM"
            - heure_fin (str): L'heure de fin au format "HH:MM"
            - duree (float): La durée de la plage en heures
    """
    plages_libres = []
    cours_par_date = {}
    dates_uniques = set()
    
    # Collecter toutes les dates uniques et regrouper les cours par date
    for i in range(len(heures_debut)):
        date = heures_debut[i].date()
        dates_uniques.add(date)
        if date not in cours_par_date:
            cours_par_date[date] = []
        cours_par_date[date].append((heures_debut[i], heures_fin[i]))
    
    # Trouver la première et dernière date
    if heures_debut:
        date_debut = min(dates_uniques)
        date_fin = max(dates_uniques)
        
        # Parcourir toutes les dates dans la plage
        date_courante = date_debut
        while date_courante <= date_fin:
            debut_journee = datetime.combine(date_courante, datetime.strptime("07:30", "%H:%M").time())
            fin_journee = datetime.combine(date_courante, datetime.strptime("18:00", "%H:%M").time())
            
            # Si pas de cours ce jour-là
            if date_courante not in cours_par_date:
                plages_libres.append((date_courante, "07:30", "18:00", 10.5))
            else:
                cours = sorted(cours_par_date[date_courante])
                
                # Plage du matin
                if cours[0][0] > debut_journee:
                    duree_en_secondes = (cours[0][0] - debut_journee).seconds
                    duree_en_heures = duree_en_secondes / 3600
                    plages_libres.append((date_courante, "07:30", cours[0][0].strftime("%H:%M"), duree_en_heures))
                
                # Plages entre les cours
                for i in range(len(cours)-1):
                    if cours[i][1] < cours[i+1][0]:
                        duree_en_secondes = (cours[i+1][0] - cours[i][1]).seconds
                        duree_en_heures = duree_en_secondes / 3600
                        plages_libres.append((date_courante, 
                                            cours[i][1].strftime("%H:%M"),
                                            cours[i+1][0].strftime("%H:%M"), 
                                            duree_en_heures))
                
                # Plage de fin de journée
                if cours[-1][1] < fin_journee:
                    duree_en_secondes = (fin_journee - cours[-1][1]).seconds
                    duree_en_heures = duree_en_secondes / 3600
                    plages_libres.append((date_courante, 
                                        cours[-1][1].strftime("%H:%M"),
                                        "18:00", 
                                        duree_en_heures))
            
            date_courante += timedelta(days=1)
    
    return plages_libres
