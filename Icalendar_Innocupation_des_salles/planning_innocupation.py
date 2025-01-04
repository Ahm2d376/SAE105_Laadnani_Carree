from datetime import datetime
import os
from extraction_evenements import extraction_evenements
from trouver_plages_libres import trouver_plages_libres
from creer_html import creer_html
import argparse

def main():
    """
    Fonction principale du programme.

    Cette fonction :
    1. Traite les arguments de ligne de commande
    2. Lit le fichier ICS d'emploi du temps
    3. Extrait les événements de la salle spécifiée
    4. Calcule les plages libres
    5. Génère un fichier HTML avec les résultats

    Arguments en ligne de commande :
        --salle: Identifiant de la salle (ex: "RT04")
        --input-file: Chemin du fichier ICS (ex: "ADECal (1).ics")
        --output-dir: Dossier de sortie (ex: "html")
        --date-debut: Date de début (format: YYYY-MM-DD)
        --date-fin: Date de fin (format: YYYY-MM-DD)

    Returns:
        Notre page html avec les résultat souhaité.
    """
    
    parser = argparse.ArgumentParser(
        description="Analyse des plages d'inoccupation des salles à partir du fichier ICS"
    )

    # Définition des arguments
    parser.add_argument(
        "--salle",
        required=True,
        help="Identifiant de la salle (ex: RT04)"
    )
    parser.add_argument(
        "--input-file",
        required=True,
        help="Chemin vers le fichier ICS"
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Dossier de sortie"
    )
    parser.add_argument(
        "--date-debut",
        required=True,
        type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
        help="Date de début au format YYYY-MM-DD"
    )
    parser.add_argument(
        "--date-fin",
        required=True,
        type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
        help="Date de fin au format YYYY-MM-DD"
    )

   
    args = parser.parse_args()

    # Lecture du fichier ICS
    with open(args.input_file, "r") as f:
        lines = f.readlines()

    
    heures_debut, heures_fin = extraction_evenements(lines, args.salle)
    plages_libres = trouver_plages_libres(heures_debut, heures_fin)
    plages_filtrees = [p for p in plages_libres if args.date_debut.date() <= p[0] <= args.date_fin.date()]

    # Création du fichier HTML
    os.makedirs(args.output_dir, exist_ok=True)
    with open(os.path.join(args.output_dir, f"plages_libres_{args.salle}.html"), "w", encoding="utf-8") as f:
        f.write(creer_html(args.salle, plages_filtrees))


if __name__ == '__main__':
    main()