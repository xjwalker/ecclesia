"""
Convert sources to bilingual format for both centuries.
"""
import json

# Helper function to convert a sources file
def convert_sources_bilingual(sources_file, output_file):
    with open(sources_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Type translations
    type_trans = {
        "primary": {"en": "primary", "es": "primaria"},
        "secondary": {"en": "secondary", "es": "secundaria"},
        "scholarly": {"en": "scholarly", "es": "académica"}
    }
    
    # Language translations
    lang_trans = {
        "Greek": {"en": "Greek", "es": "Griego"},
        "Latin": {"en": "Latin", "es": "Latín"},
        "English": {"en": "English", "es": "Inglés"},
        "Aramaic": {"en": "Aramaic", "es": "Arameo"},
        "Hebrew": {"en": "Hebrew", "es": "Hebreo"}
    }
    
    # Author name translations
    author_trans = {
        "Paul of Tarsus": {"en": "Paul of Tarsus", "es": "Pablo de Tarso"},
        "Flavius Josephus": {"en": "Flavius Josephus", "es": "Flavio Josefo"},
        "Tacitus": {"en": "Tacitus", "es": "Tácito"},
        "Pliny the Younger": {"en": "Pliny the Younger", "es": "Plinio el Joven"},
        "Suetonius": {"en": "Suetonius", "es": "Suetonio"},
        "Anonymous (trad. Luke)": {"en": "Anonymous (trad. Luke)", "es": "Anónimo (trad. Lucas)"},
        "Synoptic Gospels": {"en": "Synoptic Gospels", "es": "Evangelios Sinópticos"},
        "Gospel of John": {"en": "Gospel of John", "es": "Evangelio de Juan"},
        "Bart D. Ehrman": {"en": "Bart D. Ehrman", "es": "Bart D. Ehrman"},
        "E.P. Sanders": {"en": "E.P. Sanders", "es": "E.P. Sanders"},
        "Raymond E. Brown": {"en": "Raymond E. Brown", "es": "Raymond E. Brown"},
        "John P. Meier": {"en": "John P. Meier", "es": "John P. Meier"},
        "James D.G. Dunn": {"en": "James D.G. Dunn", "es": "James D.G. Dunn"},
        "John Dominic Crossan": {"en": "John Dominic Crossan", "es": "John Dominic Crossan"},
        "N.T. Wright": {"en": "N.T. Wright", "es": "N.T. Wright"},
        "Richard Bauckham": {"en": "Richard Bauckham", "es": "Richard Bauckham"},
        "Martin Hengel": {"en": "Martin Hengel", "es": "Martin Hengel"},
        "Dale C. Allison Jr.": {"en": "Dale C. Allison Jr.", "es": "Dale C. Allison Jr."},
        "Larry W. Hurtado": {"en": "Larry W. Hurtado", "es": "Larry W. Hurtado"},
        "Ignatius of Antioch": {"en": "Ignatius of Antioch", "es": "Ignacio de Antioquía"},
        "Justin Martyr": {"en": "Justin Martyr", "es": "Justino Mártir"},
        "Irenaeus of Lyons": {"en": "Irenaeus of Lyons", "es": "Ireneo de Lyon"},
        "Tertullian": {"en": "Tertullian", "es": "Tertuliano"},
        "Church of Smyrna": {"en": "Church of Smyrna", "es": "Iglesia de Esmirna"},
        "Unknown (2nd century)": {"en": "Unknown (2nd century)", "es": "Desconocido (siglo II)"},
        "W.H.C. Frend": {"en": "W.H.C. Frend", "es": "W.H.C. Frend"},
        "Michael Grant": {"en": "Michael Grant", "es": "Michael Grant"},
        "Walter Bauer": {"en": "Walter Bauer", "es": "Walter Bauer"}
    }
    
    for source in data['sources']:
        # Type
        if source.get('type'):
            type_val = source['type']
            if type_val in type_trans:
                source['type'] = type_trans[type_val]
            else:
                source['type'] = {"en": type_val, "es": type_val}
        
        # Author
        if source.get('author'):
            author_val = source['author']
            if author_val in author_trans:
                source['author'] = author_trans[author_val]
            else:
                source['author'] = {"en": author_val, "es": author_val}
        
        # Language
        if source.get('language'):
            lang_val = source['language']
            if lang_val in lang_trans:
                source['language'] = lang_trans[lang_val]
            else:
                source['language'] = {"en": lang_val, "es": lang_val}
        
        # Work - keep as single string (titles usually not translated)
        # Notes and citation_info - these need manual translation, keep for now
        # Will create separate translation mappings
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Converted {sources_file} → {output_file}")

# Convert both centuries
convert_sources_bilingual(
    'christianity_century_1/sources.json',
    'christianity_century_1/sources_bilingual.json'
)

convert_sources_bilingual(
    'christianity_century_2/sources.json',
    'christianity_century_2/sources_bilingual.json'
)

print("✓ Sources converted to bilingual format")
print("⚠️  Note: 'work', 'notes', and 'citation_info' fields kept as-is")
print("   These may need manual translation or can be expanded later")
