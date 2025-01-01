from datetime import datetime

def extraction_evenements(lines, salle):
    """
    Extrait les heures de début et de fin des événements pour une salle donnée.
    
    Auteur: Ahmed
    Date de création: 2024-03-20
    Dernière modification: 2024-03-20
    
    Args:
        lines (list): Liste des lignes du fichier ICS
        salle (str): Identifiant de la salle à rechercher (ex: "RT04")
        
    Returns:
        tuple: Deux listes contenant les heures de début et de fin des événements
            - heures_debut (list): Liste des objets datetime pour les débuts d'événements
            - heures_fin (list): Liste des objets datetime pour les fins d'événements
            
    Raises:
        ValueError: Si le format de date dans le fichier ICS est invalide
        
    Note:
        - Le fichier ICS doit être au format standard iCalendar
        - Les dates sont automatiquement ajustées au fuseau horaire (+2 heures)
    """
    heures_debut = []
    heures_fin = []
    
    for i in range(len(lines)):
        ligne = lines[i].strip()
        if "LOCATION:" in ligne and salle in ligne:
            for j in range(i-5, i+5):
                if j >= 0 and j < len(lines):
                    if "DTSTART:" in lines[j]:
                        date = datetime.strptime(lines[j][8:].strip(), "%Y%m%dT%H%M%SZ")
                        date = datetime(date.year, date.month, date.day, 
                                     date.hour + 2, date.minute)
                        heures_debut.append(date)
                    elif "DTEND:" in lines[j]:
                        date = datetime.strptime(lines[j][6:].strip(), "%Y%m%dT%H%M%SZ")
                        date = datetime(date.year, date.month, date.day, 
                                     date.hour + 2, date.minute)
                        heures_fin.append(date)
    return heures_debut, heures_fin 