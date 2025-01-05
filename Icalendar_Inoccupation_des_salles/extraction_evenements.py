from datetime import datetime, timedelta

def ajuster_heure(date):
    """
   Cette fonction convertit une heure UTC en heure locale française en appliquant :
    - UTC+1 pendant l'heure d'hiver
    - UTC+2 pendant l'heure d'été

    Arguments:
        date (datetime): Date et heure en UTC à convertir

    Returns:
        datetime: Date et heure convertie en heure locale française
    """
    debut_ete = datetime(2024, 3, 31)
    debut_hiver = datetime(2024, 10, 27)
    if debut_ete <= date < debut_hiver:
        return date + timedelta(hours=2)
    else:
        return date + timedelta(hours=1)

def extraction_evenements(lines, salle):
    """
    Cette fonction parcourt le fichier ICS pour trouver tous les événements
    correspondant à la salle spécifiée et en extrait les heures de début et de fin.

    Arguments:
        lines (list): Liste des lignes du fichier ICS
        salle (str): Identifiant de la salle à rechercher (ex: "RT04")

    Returns:
        tuple: Deux listes contenant :
            - heures_debut (list[datetime]): Heures de début des événements
            - heures_fin (list[datetime]): Heures de fin des événements
    """
    heures_debut = []
    heures_fin = []
    
    for i in range(len(lines)):
        ligne = lines[i].strip()
        if "LOCATION:" in ligne and salle in ligne:
            for j in range(i-5, i+5):
                if j >= 0 and j < len(lines):
                    if "DTSTART:" in lines[j]:
                        date_str = lines[j][8:].strip()
                        date = datetime.strptime(date_str, "%Y%m%dT%H%M%SZ")
                        date = ajuster_heure(date)
                        heures_debut.append(date)
                    elif "DTEND:" in lines[j]:
                        date_str = lines[j][6:].strip()
                        date = datetime.strptime(date_str, "%Y%m%dT%H%M%SZ")
                        date = ajuster_heure(date)
                        heures_fin.append(date)
    
    return heures_debut, heures_fin 
    
