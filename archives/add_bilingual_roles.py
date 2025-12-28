"""
Add bilingual roles to people_involved in events.
"""
import json

# Role translations English to Spanish
role_translations = {
    # Century 1
    "executed": "ejecutado",
    "Roman prefect, ordered execution": "prefecto romano, ordenó ejecución",
    "High priest, Jewish authority": "sumo sacerdote, autoridad judía",
    "Tetrarch of Galilee, mentioned in trial": "tetrarca de Galilea, mencionado en juicio",
    "Apostle and missionary": "apóstol y misionero",
    "Companion on first journey": "compañero en primer viaje",
    "Companion on second journey": "compañero en segundo viaje",
    "Protégé and fellow worker": "protegido y colaborador",
    "Physician and companion": "médico y compañero",
    "Leader of Jerusalem church": "líder de iglesia de Jerusalén",
    "Apostle, advocate for Gentiles": "apóstol, defensor de gentiles",
    "Apostle to Gentiles": "apóstol a los gentiles",
    "Paul's companion": "compañero de Pablo",
    "Apostle, executed": "apóstol, ejecutado",
    "Roman Emperor": "emperador romano",
    "Roman general, led siege": "general romano, lideró asedio",
    "Roman Emperor, father of Titus": "emperador romano, padre de Tito",
    "Jewish historian, eyewitness": "historiador judío, testigo ocular",
    "Roman Emperor, ordered persecution": "emperador romano, ordenó persecución",
    "Apostle, traditionally martyred": "apóstol, tradicionalmente martirizado",
    "Historian who recorded events": "historiador que registró eventos",
    "Roman Emperor, issued edict": "emperador romano, emitió edicto",
    "Jewish Christian expelled from Rome": "cristiano judío expulsado de Roma",
    "Traditionally attributed author": "autor tradicionalmente atribuido",
    "Tradition says Mark's source": "tradición dice fuente de Marcos",
    "Subject of the gospel": "sujeto del evangelio",
    "Dedicatee of work": "dedicatario de la obra",
    "Possible author": "posible autor",
    "Christian group, likely authors": "grupo cristiano, probables autores",
    
    # Century 2
    "Bishop, martyr, author": "obispo, mártir, autor",
    "Roman Emperor during persecution": "emperador romano durante persecución",
    "Bishop of Smyrna, recipient of letter": "obispo de Esmirna, destinatario de carta",
    "Heresiarch, proposed radical canon": "heresiarca, propuso canon radical",
    "Bishop of Lyons, refuted Marcion": "obispo de Lyon, refutó a Marción",
    "Apologist, wrote Against Marcion": "apologista, escribió Contra Marción",
    "Bishop, martyr, disciple of John": "obispo, mártir, discípulo de Juan",
    "Proconsul who condemned him": "procónsul que lo condenó",
    "Wrote martyrdom account": "escribió relato de martirio",
    "Philosopher, apologist, martyr": "filósofo, apologista, mártir",
    "Prefect of Rome who condemned him": "prefecto de Roma que lo condenó",
    "Emperor, addressee of First Apology": "emperador, destinatario de Primera Apología",
    "Emperor during his martyrdom": "emperador durante su martirio",
    "Bishop, theologian, author": "obispo, teólogo, autor",
    "Irenaeus' teacher, link to apostles": "maestro de Ireneo, enlace con apóstoles",
    "Gnostic teacher refuted by Irenaeus": "maestro gnóstico refutado por Ireneo",
    "Slave woman, martyr": "mujer esclava, mártir",
    "Bishop of Lyons, martyr": "obispo de Lyon, mártir",
    "Deacon, martyr": "diácono, mártir",
    "Roman Emperor during persecution": "emperador romano durante persecución"
}

def add_bilingual_roles(events_file):
    # Read events
    with open(events_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update people_involved roles
    for event in data['events']:
        if 'people_involved' in event and event['people_involved']:
            for person in event['people_involved']:
                if 'role' in person and isinstance(person['role'], str):
                    role_en = person['role']
                    role_es = role_translations.get(role_en, role_en)
                    
                    # Replace single role with bilingual structure
                    person['role_en'] = role_en
                    person['role_es'] = role_es
                    del person['role']
    
    # Write back
    with open(events_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Updated {events_file}")

# Update both centuries
add_bilingual_roles('christianity_century_1/events.json')
add_bilingual_roles('christianity_century_2/events.json')

print("✓ All people roles now bilingual")
