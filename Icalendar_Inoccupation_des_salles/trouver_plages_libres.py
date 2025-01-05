
from datetime import datetime, timedelta

def trouver_plages_libres(heures_debut, heures_fin):
   """
    Cette fonction analyse les événements fournis et détermine les périodes d'inoccupation
    entre 7h30 et 18h00 pour chaque jour. Elle identifie :
    - Les plages libres en début de journée
    - Les plages libres entre les cours
    - Les plages libres en fin de journée
    - Les journées complètement libres

    Arguments:
        heures_debut (list[datetime]): Liste des dates et heures de début des événements
        heures_fin (list[datetime]): Liste des dates et heures de fin des événements

    Returns:
        list[tuple]: Liste des plages libres, chaque plage contenant :
            - date (datetime.date): Date de la plage libre
            - heure_debut (str): Heure de début au format "HH:MM"
            - heure_fin (str): Heure de fin au format "HH:MM"
            - duree (float): Durée de la plage en heures
    """
   if not heures_debut:
        return []

   plages_libres = []
   cours_par_date = {}
    
   for i in range(len(heures_debut)):
        date = heures_debut[i].date()
        if date not in cours_par_date:
            cours_par_date[date] = []
        cours_par_date[date].append((heures_debut[i], heures_fin[i]))
    
   date_courante = min(d.date() for d in heures_debut)
   date_fin = max(d.date() for d in heures_debut)
    
   while date_courante <= date_fin:
        debut_journee = datetime.combine(date_courante, datetime.strptime("07:30", "%H:%M").time())
        fin_journee = datetime.combine(date_courante, datetime.strptime("18:00", "%H:%M").time())
        
        if date_courante not in cours_par_date:
            plages_libres.append((date_courante, "07:30", "18:00", 10.5))
        else:
            cours = sorted(cours_par_date[date_courante])
            
            if cours[0][0] > debut_journee:
                duree = (cours[0][0] - debut_journee).seconds / 3600
                plages_libres.append((date_courante, "07:30", cours[0][0].strftime("%H:%M"), duree))
            
            for i in range(len(cours)-1):
                if cours[i][1] < cours[i+1][0]:
                    duree = (cours[i+1][0] - cours[i][1]).seconds / 3600
                    plages_libres.append((
                        date_courante,
                        cours[i][1].strftime("%H:%M"),
                        cours[i+1][0].strftime("%H:%M"),
                        duree
                    ))
            
            if cours[-1][1] < fin_journee:
                duree = (fin_journee - cours[-1][1]).seconds / 3600
                plages_libres.append((
                    date_courante,
                    cours[-1][1].strftime("%H:%M"),
                    "18:00",
                    duree
                ))
        
        date_courante += timedelta(days=1)
    
   return plages_libres