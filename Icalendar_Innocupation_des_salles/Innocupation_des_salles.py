
from datetime import datetime  

def extraction_evenements(lines, salle):
    """
    Extrait les heures de début et de fin des événements pour une salle donnée.
    
    Args:
        lines (list): Liste des lignes du fichier ICS
        salle (str): Identifiant de la salle à rechercher
        
    Returns:
        tuple: Deux listes contenant les heures de début et de fin des événements
    """
    heures_debut = []  # Liste pour stocker les heures de début
    heures_fin = []    # Liste pour stocker les heures de fin
    
    for i in range(len(lines)):  # Parcours de toutes les lignes du fichier
        ligne = lines[i].strip()  # Supprime les espaces en début et fin de ligne
        if "LOCATION:" in ligne and salle in ligne:  # Si on trouve la salle recherchée
            # Parcours des lignes autour de la ligne LOCATION (5 avant et 5 après)
            for j in range(i-5, i+5):
                if j >= 0 and j < len(lines):  # Vérifie que l'index est valide
                    if "DTSTART:" in lines[j]:  # Si c'est une ligne d'heure de début
                        # Conversion de la date du format ICS en objet datetime
                        date = datetime.strptime(lines[j][8:].strip(), "%Y%m%dT%H%M%SZ")
                        # Ajout de 2 heures pour la correction du fuseau horaire
                        date = datetime(date.year, date.month, date.day, 
                                     date.hour + 2, date.minute)
                        heures_debut.append(date)
                    elif "DTEND:" in lines[j]:  # Si c'est une ligne d'heure de fin
                        # Même traitement pour l'heure de fin
                        date = datetime.strptime(lines[j][6:].strip(), "%Y%m%dT%H%M%SZ")
                        date = datetime(date.year, date.month, date.day, 
                                     date.hour + 2, date.minute)
                        heures_fin.append(date)
    return heures_debut, heures_fin

def trouver_plages_libres(heures_debut, heures_fin):
    """
    Trouve les plages horaires libres entre les événements.
    
    Args:
        heures_debut (list): Liste des heures de début des événements
        heures_fin (list): Liste des heures de fin des événements
        
    Returns:
        list: Liste des plages libres avec date, heure début, heure fin et durée
    """
    plages_libres = []  # Liste pour stocker les plages libres trouvées
    cours_par_date = {}  # Dictionnaire pour regrouper les cours par date
    
    # Regroupement des cours par date
    for i in range(len(heures_debut)):
        date = heures_debut[i].date()  # Extraction de la date sans l'heure
        if date not in cours_par_date:
            cours_par_date[date] = []
        cours_par_date[date].append((heures_debut[i], heures_fin[i]))
    
    # Traitement de chaque date
    for date in sorted(cours_par_date.keys()):  # Parcours des dates dans l'ordre
        cours = sorted(cours_par_date[date])    # Tri des cours par heure de début
        # Définition des limites de la journée (7h30 - 18h00)
        debut_journee = datetime(date.year, date.month, date.day, 7, 30)
        fin_journee = datetime(date.year, date.month, date.day, 18, 0)
        
        # Si aucun cours ce jour-là
        if not cours:
            plages_libres.append((date, "07:30", "18:00", 10.5))
            continue
            
        # Vérification de la plage libre avant le premier cours
        if cours[0][0] > debut_journee:
            duree = (cours[0][0] - debut_journee).seconds / 3600
            plages_libres.append((date, "07:30", cours[0][0].strftime("%H:%M"), duree))
            
        # Vérification des plages libres entre les cours
        for i in range(len(cours)-1):
            if cours[i][1] < cours[i+1][0]:  # S'il y a un intervalle entre deux cours
                duree = (cours[i+1][0] - cours[i][1]).seconds / 3600
                plages_libres.append((date, cours[i][1].strftime("%H:%M"), 
                                    cours[i+1][0].strftime("%H:%M"), duree))
                
        # Vérification de la plage libre après le dernier cours
        if cours[-1][1] < fin_journee:
            duree = (fin_journee - cours[-1][1]).seconds / 3600
            plages_libres.append((date, cours[-1][1].strftime("%H:%M"), "18:00", duree))
            
    return plages_libres

def convertir_duree(duree):
    """
    Convertit une durée décimale en format Heures:Minutes.
    
    Args:
        duree (float): Durée en heures décimales
        
    Returns:
        str: Durée formatée en "HH:MM"
    """
    heures = int(duree)  # Partie entière pour les heures
    minutes = int((duree - heures) * 60)  # Conversion des décimales en minutes
    return f"{heures}:{minutes:02d}"

def creer_html(salle, plages_libres):
    """
    Crée une page HTML présentant les plages libres.
    
    Args:
        salle (str): Identifiant de la salle
        plages_libres (list): Liste des plages libres à afficher
        
    Returns:
        str: Contenu HTML formaté
    """
   
    html = f"""
    <html>
    <head>
        <title>Plages libres - Salle {salle}</title>
        <style>
            table {{ border-collapse: collapse; }}
            td, th {{ border: 1px solid black; padding: 5px; }}
        </style>
    </head>
    <body>
        <h2>Plages d'inoccupation - Salle {salle}</h2>
        <table>
            <tr><th>Date</th><th>Début</th><th>Fin</th><th>Durée</th></tr>
    """
    
    # Ajout des lignes pour chaque plage libre
    for date, debut, fin, duree in plages_libres:
        duree_formatee = convertir_duree(duree)
        html += f"<tr><td>{date}</td><td>{debut}</td><td>{fin}</td><td>{duree_formatee}</td></tr>\n"
    
    html += "</table></body></html>"
    return html

with open("/home/etudiant/SAE105_Laadnani_Carree/data/ADECal (1).ics", "r") as f:
    lines = f.readlines()


salle = "RT12"  # Définition de la salle à analyser
heures_debut, heures_fin = extraction_evenements(lines, salle)  
plages_libres = trouver_plages_libres(heures_debut, heures_fin)  


html = creer_html(salle, plages_libres)
with open("/home/etudiant/SAE105_Laadnani_Carree/html/plages_libres.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fichier HTML créé")  
