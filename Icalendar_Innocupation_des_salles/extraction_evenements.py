
from datetime import datetime, timedelta

def extraction_evenements(lines, salle):
    """
    Extrait les heures de début et de fin des événements pour une salle donnée.
    
    Args:
        lines (list): Liste des lignes du fichier ICS
        salle (str): Identifiant de la salle à rechercher (ex: "RT04")
        
    Returns:
        tuple: Deux listes contenant les heures de début et de fin des événements
        
	Ajuster_heure :
		
		Cette fonction ajuste l'heure selon la période été/hiver        
        
    """
    heures_debut = []
    heures_fin = []
    
    def ajuster_heure(date):
        """Ajuste l'heure selon la période été/hiver"""
        debut_ete = datetime(2024, 3, 31)  
        debut_hiver = datetime(2024, 10, 27)  
        
        if debut_ete <= date < debut_hiver:
            return date + timedelta(hours=2)  
        else:
            return date + timedelta(hours=1)  
    
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
