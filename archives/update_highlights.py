"""
Add highlights and images to centuries 1-3 to match century 4 structure.
"""
import json
from pathlib import Path

def update_century_1():
    """Update Century 1 events with highlights and images."""
    file_path = Path(__file__).parent / 'christianity_century_1' / 'events.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update each event
    for event in data['events']:
        event_id = event['id']
        
        # EVT_0030_CRUCIFIXION - foundational historical event
        if event_id == 'EVT_0030_CRUCIFIXION':
            event['highlight'] = 'historical_event'
            # Already has image
        
        # EVT_0048_PAUL_MISSION - major historical event
        elif event_id == 'EVT_0048_PAUL_MISSION':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Caravaggio_-_St._Paul_the_Apostle.jpg/800px-Caravaggio_-_St._Paul_the_Apostle.jpg'
        
        # EVT_0050_JERUSALEM_COUNCIL - first council, doctrine established
        elif event_id == 'EVT_0050_JERUSALEM_COUNCIL':
            event['highlight'] = 'doctrine_established'
            event['event_type'] = 'Council'
            event['doctrine'] = {
                "name": {
                    "en": "Gentile Inclusion: Faith Not Law",
                    "es": "Inclusión de Gentiles: Fe No Ley"
                },
                "summary": {
                    "en": "Gentile converts do not need circumcision or full observance of Mosaic law; salvation by faith, not law",
                    "es": "Los conversos gentiles no necesitan circuncisión ni observancia completa de la ley mosaica; salvación por fe, no ley"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Jouvenet%2C_Jean-Baptiste_-_The_Apostles_Peter_and_John_Healing_the_Lame_Man_at_the_Gate_of_the_Temple_-_Google_Art_Project.jpg/800px-Jouvenet%2C_Jean-Baptiste_-_The_Apostles_Peter_and_John_Healing_the_Lame_Man_at_the_Gate_of_the_Temple_-_Google_Art_Project.jpg'
        
        # EVT_0062_PAUL_DEATH - martyrdom
        elif event_id == 'EVT_0062_PAUL_DEATH':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Rembrandt_-_The_Apostle_Paul_-_WGA19120.jpg/800px-Rembrandt_-_The_Apostle_Paul_-_WGA19120.jpg'
        
        # EVT_0064_NERO_PERSECUTION - major historical event
        elif event_id == 'EVT_0064_NERO_PERSECUTION':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Siemiradzki_Fackeln.jpg/1024px-Siemiradzki_Fackeln.jpg'
        
        # EVT_0070_TEMPLE - major historical event
        elif event_id == 'EVT_0070_TEMPLE':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Francesco_Hayez_017.jpg/1024px-Francesco_Hayez_017.jpg'
        
        # Gospel compositions - doctrine established (canon formation)
        elif event_id == 'EVT_0070_MARK':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Gospel of Mark: First Written Gospel",
                    "es": "Evangelio de Marcos: Primer Evangelio Escrito"
                },
                "summary": {
                    "en": "First narrative gospel, establishes the passion narrative structure and Jesus as suffering messiah",
                    "es": "Primer evangelio narrativo, establece la estructura de la narrativa de la pasión y Jesús como mesías sufriente"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Saint_Mark_painting.jpg/800px-Saint_Mark_painting.jpg'
        
        elif event_id == 'EVT_0085_MATTHEW':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Gospel of Matthew: Jesus as Jewish Messiah",
                    "es": "Evangelio de Mateo: Jesús como Mesías Judío"
                },
                "summary": {
                    "en": "Presents Jesus as fulfillment of Jewish prophecy, includes Sermon on the Mount and Great Commission",
                    "es": "Presenta a Jesús como cumplimiento de profecía judía, incluye Sermón del Monte y Gran Comisión"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Caravaggio_-_San_Matteo_e_l%27angelo.jpg/800px-Caravaggio_-_San_Matteo_e_l%27angelo.jpg'
        
        elif event_id == 'EVT_0085_LUKE':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Gospel of Luke: Jesus as Universal Savior",
                    "es": "Evangelio de Lucas: Jesús como Salvador Universal"
                },
                "summary": {
                    "en": "Emphasizes Jesus's concern for outcasts, women, and Gentiles; includes parables of mercy",
                    "es": "Enfatiza la preocupación de Jesús por marginados, mujeres y gentiles; incluye parábolas de misericordia"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Guercino_-_San_Luca.jpg/800px-Guercino_-_San_Luca.jpg'
        
        elif event_id == 'EVT_0095_JOHN':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Gospel of John: High Christology",
                    "es": "Evangelio de Juan: Alta Cristología"
                },
                "summary": {
                    "en": "Presents Jesus as pre-existent divine Word (Logos), 'I AM' statements, emphasis on Jesus's divinity",
                    "es": "Presenta a Jesús como Verbo divino preexistente (Logos), declaraciones 'YO SOY', énfasis en divinidad de Jesús"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/El_Greco_-_St._John_the_Evangelist.jpg/800px-El_Greco_-_St._John_the_Evangelist.jpg'
        
        # EVT_0049_CLAUDIUS_EXPULSION - historical event
        elif event_id == 'EVT_0049_CLAUDIUS_EXPULSION':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Claudius_Pio-Clementino_Inv243.jpg/800px-Claudius_Pio-Clementino_Inv243.jpg'
    
    # Write updated data
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Century 1 updated")

def update_century_2():
    """Update Century 2 events with highlights and images."""
    file_path = Path(__file__).parent / 'christianity_century_2' / 'events.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for event in data['events']:
        event_id = event['id']
        
        # All century 2 martyrdoms are historical events
        if event_id == 'EVT_0110_IGNATIUS':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Ignatius_of_Antioch_%28Menologion_of_Basil_II%29.jpg/800px-Ignatius_of_Antioch_%28Menologion_of_Basil_II%29.jpg'
        
        elif event_id == 'EVT_0144_MARCION':
            event['highlight'] = 'historical_event'
            event['heresy_condemned'] = {
                "name": {
                    "en": "Marcionism",
                    "es": "Marcionismo"
                },
                "summary": {
                    "en": "Rejection of the Old Testament and belief in two gods: the inferior creator God and the superior God revealed by Jesus",
                    "es": "Rechazo del Antiguo Testamento y creencia en dos dioses: el Dios creador inferior y el Dios superior revelado por Jesús"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Marcion_of_Sinope.jpg/800px-Marcion_of_Sinope.jpg'
        
        elif event_id == 'EVT_0155_POLYCARP':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Polycarp_of_Smyrna.jpg/800px-Polycarp_of_Smyrna.jpg'
        
        elif event_id == 'EVT_0165_JUSTIN_MARTYR':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Saint_Justin_Martyr.jpg/800px-Saint_Justin_Martyr.jpg'
        
        elif event_id == 'EVT_0180_IRENAEUS':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Orthodox Canon and Apostolic Succession",
                    "es": "Canon Ortodoxo y Sucesión Apostólica"
                },
                "summary": {
                    "en": "Established four canonical gospels, apostolic succession as criterion of authority, and unity of Old and New Testaments",
                    "es": "Estableció cuatro evangelios canónicos, sucesión apostólica como criterio de autoridad, y unidad de Antiguo y Nuevo Testamentos"
                }
            }
            event['heresy_condemned'] = {
                "name": {
                    "en": "Gnosticism (Valentinianism)",
                    "es": "Gnosticismo (Valentinianismo)"
                },
                "summary": {
                    "en": "Rejection of material world as evil, secret knowledge (gnosis) for salvation, and denial of Christ's true humanity",
                    "es": "Rechazo del mundo material como malo, conocimiento secreto (gnosis) para salvación, y negación de verdadera humanidad de Cristo"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Irenaeus.jpg/800px-Irenaeus.jpg'
        
        elif event_id == 'EVT_0177_LYON_MARTYRS':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Eug%C3%A8ne_Thirion_-_Saint_Blandina_-_1894.jpg/1024px-Eug%C3%A8ne_Thirion_-_Saint_Blandina_-_1894.jpg'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Century 2 updated")

def update_century_3():
    """Update Century 3 events with highlights and images."""
    file_path = Path(__file__).parent / 'christianity_century_3' / 'events.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for event in data['events']:
        event_id = event['id']
        
        if event_id == 'EVT_0203_ORIGEN_YOUTH':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Origen.jpg/800px-Origen.jpg'
        
        elif event_id == 'EVT_0250_DECIAN_PERSECUTION':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Decius_from_Palazzo_Nuovo.jpg/800px-Decius_from_Palazzo_Nuovo.jpg'
        
        elif event_id == 'EVT_0258_CYPRIAN':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Cyprian_of_Carthage.jpg/800px-Cyprian_of_Carthage.jpg'
        
        elif event_id == 'EVT_0270_ANTHONY':
            event['highlight'] = 'doctrine_established'
            event['doctrine'] = {
                "name": {
                    "en": "Christian Monasticism: Desert Asceticism",
                    "es": "Monasticismo Cristiano: Ascetismo del Desierto"
                },
                "summary": {
                    "en": "Established the monastic ideal of withdrawal from the world for contemplation and spiritual warfare against demons",
                    "es": "Estableció el ideal monástico de retiro del mundo para contemplación y guerra espiritual contra demonios"
                }
            }
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Saint_Anthony_the_Great.jpg/800px-Saint_Anthony_the_Great.jpg'
        
        elif event_id == 'EVT_0303_DIOCLETIAN':
            event['highlight'] = 'historical_event'
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Diocletian_argenteus_reverse.png/800px-Diocletian_argenteus_reverse.png'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Century 3 updated")

def add_century_4_images():
    """Add images to Century 4 events that don't have them."""
    file_path = Path(__file__).parent / 'christianity_century_4' / 'events.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for event in data['events']:
        event_id = event['id']
        
        if event_id == 'EVT_0303_DIOCLETIAN_END':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Diocletian_argenteus_reverse.png/800px-Diocletian_argenteus_reverse.png'
        
        elif event_id == 'EVT_0312_CONSTANTINE_CONVERSION':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Constantine_Chiaramonti_Inv1749.jpg/800px-Constantine_Chiaramonti_Inv1749.jpg'
        
        elif event_id == 'EVT_0313_EDICT_MILAN':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/RIC_VI_Trier_433_Constantine.jpg/800px-RIC_VI_Trier_433_Constantine.jpg'
        
        elif event_id == 'EVT_0325_NICAEA':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Constantine_burning_Arian_books.jpg/1024px-Constantine_burning_Arian_books.jpg'
        
        elif event_id == 'EVT_0380_NICENE_STATE':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Theodosius_I%27s_empire.png/1024px-Theodosius_I%27s_empire.png'
        
        elif event_id == 'EVT_0381_CONSTANTINOPLE':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Gregory_of_Nazianzus.jpg/800px-Gregory_of_Nazianzus.jpg'
        
        elif event_id == 'EVT_0386_JEROME_VULGATE':
            event['image_url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Saint_Jerome_by_Caravaggio.jpg/800px-Saint_Jerome_by_Caravaggio.jpg'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Century 4 images added")

if __name__ == "__main__":
    print("=" * 60)
    print("UPDATING CENTURIES 1-4 WITH HIGHLIGHTS AND IMAGES")
    print("=" * 60)
    
    update_century_1()
    update_century_2()
    update_century_3()
    add_century_4_images()
    
    print("\n" + "=" * 60)
    print("✓ ALL CENTURIES UPDATED!")
    print("=" * 60)
    print("\nChanges made:")
    print("  • Added highlight fields (doctrine_established, historical_event)")
    print("  • Added doctrine and heresy_condemned details where applicable")
    print("  • Added image URLs from Wikimedia Commons for all events")
    print("\nNext: Run 'python backend/reseed_db.py' to update the database")
