def convertir_duree(duree):
    """
    Convertit une durée décimale en format Heures:Minutes.
    
    Auteur: Ahmed
    Date de création: 2024-03-20
    Dernière modification: 2024-03-20
    
    Args:
        duree (float): Durée en heures décimales (ex: 1.5 pour 1h30)
        
    Returns:
        str: Durée formatée en "HH:MM"
        
        
    """
    heures = int(duree)
    minutes = int((duree - heures) * 60)
    return f"{heures}:{minutes:02d}"

def creer_html(salle, plages_libres):
    """
    Crée une page HTML présentant les plages libres.
    
    Auteur: Ahmed
    Date de création: 2024-03-20
    Dernière modification: 2024-03-20
    
    Args:
        salle (str): Identifiant de la salle
        plages_libres (list): Liste des plages libres au format:
            [(date, heure_debut, heure_fin, duree), ...]
            - date (datetime.date): Date de la plage
            - heure_debut (str): Heure de début "HH:MM"
            - heure_fin (str): Heure de fin "HH:MM"
            - duree (float): Durée en heures
            
    Returns:
        str: Code HTML formaté contenant le tableau des plages libres
        
    Raises:
        ValueError: Si le format des plages libres est incorrect
        
    Note:
        Le HTML généré inclut un style CSS basique pour le tableau
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
    
    for date, debut, fin, duree in plages_libres:
        duree_formatee = convertir_duree(duree)
        html += f"<tr><td>{date}</td><td>{debut}</td><td>{fin}</td><td>{duree_formatee}</td></tr>\n"
    
    html += "</table></body></html>"
    return html 