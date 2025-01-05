import sys
sys.path.append('/home/etudiant/SAE105_Laadnani_Carree/Icalendar_Inoccupation_des_salles')
from datetime import datetime, date
from extraction_evenements import extraction_evenements, ajuster_heure
from trouver_plages_libres import trouver_plages_libres
from creer_html import creer_html, convertir_duree



def test_ajuster_heure():
    
    date_hiver = datetime(2024, 1, 1, 8, 0)
    resultat_hiver = ajuster_heure(date_hiver)
    assert resultat_hiver == datetime(2024, 1, 1, 9, 0), f"Erreur heure d'hiver"

    
    date_ete = datetime(2024, 7, 1, 8, 0)
    resultat_ete = ajuster_heure(date_ete)
    assert resultat_ete == datetime(2024, 7, 1, 10, 0), f"Erreur heure d'été"
    print("Test ajuster_heure réussi")

def test_extraction_evenements():
    exemple_ics = [
        "BEGIN:VEVENT",
        "DTSTART:20240320T080000Z",
        "DTEND:20240320T100000Z",
        "LOCATION:RT04",
        "END:VEVENT"
    ]
    
    heures_debut, heures_fin = extraction_evenements(exemple_ics, "RT04")
    
    assert len(heures_debut) == 1, f"Nombre incorrect d'heures de début: {len(heures_debut)} au lieu de 1"
    assert len(heures_fin) == 1, f"Nombre incorrect d'heures de fin: {len(heures_fin)} au lieu de 1"
    assert heures_debut[0] == datetime(2024, 3, 20, 9, 0), f"Heure de début incorrecte: {heures_debut[0]}"
    assert heures_fin[0] == datetime(2024, 3, 20, 11, 0), f"Heure de fin incorrecte: {heures_fin[0]}"
    print("Test extraction_evenements réussi")

def test_trouver_plages_libres():
    
    heures_debut = [datetime(2024, 3, 20, 10, 0)]
    heures_fin = [datetime(2024, 3, 20, 12, 0)]
    
    plages = trouver_plages_libres(heures_debut, heures_fin)
    
    assert len(plages) == 2, f"Nombre incorrect de plages: {len(plages)} au lieu de 2"
    assert plages[0][0] == date(2024, 3, 20), "Date incorrecte pour la plage du matin"
    assert plages[0][1] == "07:30", f"Heure de début incorrecte: {plages[0][1]} au lieu de 07:30"
    assert plages[0][2] == "10:00", f"Heure de fin incorrecte: {plages[0][2]} au lieu de 10:00"
    assert plages[1][1] == "12:00", f"Heure de début incorrecte: {plages[1][1]} au lieu de 12:00"
    assert plages[1][2] == "18:00", f"Heure de fin incorrecte: {plages[1][2]} au lieu de 18:00"
    print("Test trouver_plages_libres réussi")

def test_convertir_duree():
    
    assert convertir_duree(1.5) == "1:30", f"Erreur conversion 1.5h: obtenu {convertir_duree(1.5)}"
    assert convertir_duree(2.0) == "2:00", f"Erreur conversion 2.0h: obtenu {convertir_duree(2.0)}"
    assert convertir_duree(0.5) == "0:30", f"Erreur conversion 0.5h: obtenu {convertir_duree(0.5)}"
    print("Test convertir_duree réussi")

def test_creer_html():
   
    plages = [(date(2024, 3, 20), "08:00", "10:00", 2.0)]
    html = creer_html("RT04", plages)
    assert "RT04" in html, "La salle n'apparaît pas dans le HTML"
    assert "08:00" in html, "L'heure de début n'apparaît pas dans le HTML"
    print("Test creer_html réussi")

def exec_tests():
    
    test_ajuster_heure()
    test_extraction_evenements()
    test_trouver_plages_libres()
    test_convertir_duree()
    test_creer_html()
    print("Tout marche bien")


exec_tests()

