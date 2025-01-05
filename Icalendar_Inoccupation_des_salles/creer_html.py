
def convertir_duree(duree):
    """
     Cette fonction prend une durée en heures décimales et la convertit
    en format horaire  (HH:MM).

    Arguments:
        duree (float): Durée en heures (ex: 1.5 pour 1h30)

    Returns:
        str: Durée formatée (ex: "1:30" pour 1.5 heures)
    """
    heures = int(duree)
    minutes = int((duree - heures) * 60)
    return f"{heures}:{minutes:02d}"

def creer_html(salle, plages_libres):
    """
    Cette fonction crée un tableau HTML contenant toutes les plages
    d'inoccupation de la salle, avec leurs dates, heures et durées.

    Arguments:
        salle (str): Identifiant de la salle (ex: "RT04")
        plages_libres (list[tuple]): Liste des plages libres contenant :
            - date (datetime.date): Date de la plage
            - heure_debut (str): Heure de début "HH:MM"
            - heure_fin (str): Heure de fin "HH:MM"
            - duree (float): Durée en heures

    Returns:
        str: Code HTML complet de la page
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
