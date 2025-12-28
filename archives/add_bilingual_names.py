"""
Add bilingual names to people_involved in events.
"""
import json

# Name translations English to Spanish
name_translations = {
    # New Testament figures
    "Jesús de Nazaret": "Jesús de Nazaret",  # Already Spanish
    "Jesus of Nazareth": "Jesús de Nazaret",
    "Jesus": "Jesús",
    "Poncio Pilato": "Poncio Pilato",  # Already Spanish
    "Pontius Pilate": "Poncio Pilato",
    "Caifás": "Caifás",  # Already Spanish
    "Caiaphas": "Caifás",
    "Herodes Antipas": "Herodes Antipas",  # Already Spanish
    "Herod Antipas": "Herodes Antipas",
    "Paul of Tarsus": "Pablo de Tarso",
    "Barnabas": "Bernabé",
    "Silas": "Silas",
    "Timothy": "Timoteo",
    "Luke": "Lucas",
    "Luke (trad.)": "Lucas (trad.)",
    "James (brother of Jesus)": "Santiago (hermano de Jesús)",
    "Peter (Simon)": "Pedro (Simón)",
    "Peter": "Pedro",
    "Nero": "Nerón",
    "Titus": "Tito",
    "Vespasian": "Vespasiano",
    "Josephus": "Josefo",
    "Tacitus": "Tácito",
    "Claudius": "Claudio",
    "Aquila": "Áquila",
    "Priscilla (Prisca)": "Priscila (Prisca)",
    "Mark (John Mark)": "Marcos (Juan Marcos)",
    "Matthew (trad.)": "Mateo (trad.)",
    "Theophilus": "Teófilo",
    "John (the Elder)": "Juan (el Anciano)",
    "Johannine community": "comunidad joánica",
    
    # Century 2 figures
    "Ignatius of Antioch": "Ignacio de Antioquía",
    "Trajan": "Trajano",
    "Polycarp": "Policarpo",
    "Polycarp of Smyrna": "Policarpo de Esmirna",
    "Marcion of Sinope": "Marción de Sinope",
    "Irenaeus": "Ireneo",
    "Irenaeus of Lyons": "Ireneo de Lyon",
    "Tertullian": "Tertuliano",
    "Philip of Tralles": "Felipe de Tralles",
    "Church of Smyrna": "Iglesia de Esmirna",
    "Justin Martyr": "Justino Mártir",
    "Rusticus": "Rústico",
    "Antoninus Pius": "Antonino Pío",
    "Marcus Aurelius": "Marco Aurelio",
    "Valentinus": "Valentín",
    "Blandina": "Blandina",
    "Pothinus": "Potino",
    "Sanctus": "Sancto"
}

def add_bilingual_names(events_file):
    # Read events
    with open(events_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update people_involved names
    for event in data['events']:
        if 'people_involved' in event and event['people_involved']:
            for person in event['people_involved']:
                # Check if name is already split into name_en/name_es
                if 'name' in person and isinstance(person['name'], str):
                    name_current = person['name']
                    
                    # Determine if current name is in Spanish or English
                    # If it's in the translations as a key (English), translate it
                    if name_current in name_translations:
                        name_en = name_current
                        name_es = name_translations[name_current]
                    # If it's already Spanish (in values), find its English equivalent
                    elif name_current in name_translations.values():
                        # Find the English key for this Spanish value
                        name_es = name_current
                        name_en = next((k for k, v in name_translations.items() if v == name_current), name_current)
                    else:
                        # Not in dictionary, keep as is for both
                        name_en = name_current
                        name_es = name_current
                    
                    # Replace with bilingual structure
                    person['name_en'] = name_en
                    person['name_es'] = name_es
                    del person['name']
    
    # Write back
    with open(events_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Updated {events_file}")

# Update both centuries
add_bilingual_names('christianity_century_1/events.json')
add_bilingual_names('christianity_century_2/events.json')

print("✓ All people names now bilingual")
