"""
Add Spanish translations to sources work, notes, and citation_info fields.
"""
import json

# Translations for work titles, notes, and citations
source_translations = {
    "SRC_PAUL_AUTH": {
        "work": {
            "en": "Authentic Epistles (Romans, 1-2 Corinthians, Galatians, Philippians, 1 Thessalonians, Philemon)",
            "es": "Epístolas Auténticas (Romanos, 1-2 Corintios, Gálatas, Filipenses, 1 Tesalonicenses, Filemón)"
        },
        "notes": {
            "en": "Direct primary sources written by Paul himself. Universally accepted as authentic by scholars.",
            "es": "Fuentes primarias directas escritas por el propio Pablo. Universalmente aceptadas como auténticas por los estudiosos."
        }
    },
    "SRC_JOSEPHUS_WAR": {
        "work": {
            "en": "The Jewish War (Bellum Judaicum)",
            "es": "La Guerra de los Judíos (Bellum Judaicum)"
        },
        "notes": {
            "en": "Eyewitness account of the Jewish-Roman War and destruction of Jerusalem. Josephus was present during the siege.",
            "es": "Relato de testigo presencial de la Guerra Judeo-Romana y la destrucción de Jerusalén. Josefo estuvo presente durante el asedio."
        },
        "citation_info": {
            "en": "Book 6, Chapters 4-5: Detailed description of the siege and destruction of the Temple. Book 6, Chapter 5, Section 1: 'the sanctuary was burned' in the month of August",
            "es": "Libro 6, Capítulos 4-5: Descripción detallada del asedio y destrucción del Templo. Libro 6, Capítulo 5, Sección 1: 'el santuario fue quemado' en el mes de agosto"
        }
    },
    "SRC_JOSEPHUS_ANT": {
        "work": {
            "en": "Antiquities of the Jews",
            "es": "Antigüedades de los Judíos"
        },
        "notes": {
            "en": "Historical account from Creation to the outbreak of the Jewish-Roman War. Includes the Testimonium Flavianum about Jesus (controversial authenticity).",
            "es": "Relato histórico desde la Creación hasta el estallido de la Guerra Judeo-Romana. Incluye el Testimonium Flavianum sobre Jesús (autenticidad controvertida)."
        },
        "citation_info": {
            "en": "Book 18, Chapter 3, Section 3: 'At this time there appeared Jesus, a wise man' (Testimonium Flavianum). Book 20, Chapter 9, Section 1: Reference to 'James, brother of Jesus who was called Christ'",
            "es": "Libro 18, Capítulo 3, Sección 3: 'En este tiempo apareció Jesús, un hombre sabio' (Testimonium Flavianum). Libro 20, Capítulo 9, Sección 1: Referencia a 'Santiago, hermano de Jesús llamado Cristo'"
        }
    },
    "SRC_TACITUS_ANNALS": {
        "work": {
            "en": "Annals",
            "es": "Anales"
        },
        "notes": {
            "en": "History of the Roman Empire from Tiberius to Nero. Earliest pagan reference to Jesus and early Christians.",
            "es": "Historia del Imperio Romano desde Tiberio hasta Nerón. Referencia pagana más antigua a Jesús y los primeros cristianos."
        },
        "citation_info": {
            "en": "Book 15, Chapter 44: 'Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus'",
            "es": "Libro 15, Capítulo 44: 'Cristo, de quien el nombre tuvo su origen, sufrió la pena extrema durante el reinado de Tiberio bajo uno de nuestros procuradores, Poncio Pilato'"
        }
    },
    "SRC_PLINY": {
        "work": {
            "en": "Letters (Epistulae)",
            "es": "Cartas (Epistulae)"
        },
        "notes": {
            "en": "Correspondence with Emperor Trajan about handling Christians in Bithynia. Describes Christian practices.",
            "es": "Correspondencia con el Emperador Trajano sobre cómo manejar a los cristianos en Bitinia. Describe las prácticas cristianas."
        },
        "citation_info": {
            "en": "Letter 10.96: Asks Trajan about Christian trials. Letter 10.97: Trajan's response instructing not to seek out Christians but to punish those denounced",
            "es": "Carta 10.96: Pregunta a Trajano sobre los juicios a cristianos. Carta 10.97: Respuesta de Trajano instruyendo no buscar cristianos pero castigar a los denunciados"
        }
    },
    "SRC_SUETONIUS": {
        "work": {
            "en": "The Twelve Caesars (De Vita Caesarum)",
            "es": "Vida de los Doce Césares (De Vita Caesarum)"
        },
        "notes": {
            "en": "Biographies of Julius Caesar through Domitian. Contains brief reference to Claudius expelling Jews from Rome.",
            "es": "Biografías desde Julio César hasta Domiciano. Contiene breve referencia a Claudio expulsando judíos de Roma."
        },
        "citation_info": {
            "en": "Life of Claudius 25.4: 'Since the Jews constantly made disturbances at the instigation of Chrestus, he expelled them from Rome'",
            "es": "Vida de Claudio 25.4: 'Como los judíos causaban disturbios constantemente a instigación de Cresto, los expulsó de Roma'"
        }
    },
    "SRC_ACTS": {
        "work": {
            "en": "Acts of the Apostles",
            "es": "Hechos de los Apóstoles"
        },
        "notes": {
            "en": "Continuation of Luke's Gospel narrating early church history. Historical reliability debated, especially regarding Paul's journeys.",
            "es": "Continuación del Evangelio de Lucas narrando la historia de la iglesia primitiva. Fiabilidad histórica debatida, especialmente sobre los viajes de Pablo."
        },
        "citation_info": {
            "en": "Chapter 15: Jerusalem Council. Chapter 18:2: Aquila and Priscilla expelled from Rome by Claudius. Chapters 13-28: Paul's missionary journeys and arrest",
            "es": "Capítulo 15: Concilio de Jerusalén. Capítulo 18:2: Aquila y Priscila expulsados de Roma por Claudio. Capítulos 13-28: Viajes misioneros de Pablo y arresto"
        }
    },
    "SRC_SYNOPTICS": {
        "work": {
            "en": "Synoptic Gospels (Matthew, Mark, Luke)",
            "es": "Evangelios Sinópticos (Mateo, Marcos, Lucas)"
        },
        "notes": {
            "en": "Biographical accounts of Jesus' life and ministry. Mark is earliest (~70 CE), Matthew and Luke use Mark as a source.",
            "es": "Relatos biográficos de la vida y ministerio de Jesús. Marcos es el más antiguo (~70 d.C.), Mateo y Lucas usan a Marcos como fuente."
        }
    },
    "SRC_JOHN": {
        "work": {
            "en": "Gospel of John",
            "es": "Evangelio de Juan"
        },
        "notes": {
            "en": "Theologically distinct from Synoptics. Presents Jesus as divine Logos. Scholars debate historical reliability vs. theological agenda.",
            "es": "Teológicamente distinto de los Sinópticos. Presenta a Jesús como Logos divino. Los estudiosos debaten fiabilidad histórica vs. agenda teológica."
        }
    },
    "SRC_EHRMAN_NT": {
        "work": {
            "en": "The New Testament: A Historical Introduction to the Early Christian Writings",
            "es": "El Nuevo Testamento: Una Introducción Histórica a los Escritos Cristianos Primitivos"
        },
        "notes": {
            "en": "Standard academic textbook on New Testament historical-critical scholarship.",
            "es": "Libro de texto académico estándar sobre la erudición histórico-crítica del Nuevo Testamento."
        }
    },
    "SRC_SANDERS_PAUL": {
        "work": {
            "en": "Paul and Palestinian Judaism",
            "es": "Pablo y el Judaísmo Palestino"
        },
        "notes": {
            "en": "Groundbreaking work challenging traditional Protestant interpretations of Paul.",
            "es": "Obra innovadora que desafía las interpretaciones protestantes tradicionales de Pablo."
        }
    },
    "SRC_BROWN_DEATH": {
        "work": {
            "en": "The Death of the Messiah",
            "es": "La Muerte del Mesías"
        },
        "notes": {
            "en": "Magisterial two-volume commentary on Passion narratives across all four Gospels.",
            "es": "Comentario magisterial de dos volúmenes sobre las narrativas de la Pasión en los cuatro Evangelios."
        }
    },
    "SRC_MEIER_MARGINAL": {
        "work": {
            "en": "A Marginal Jew: Rethinking the Historical Jesus",
            "es": "Un Judío Marginal: Repensando al Jesús Histórico"
        },
        "notes": {
            "en": "Multi-volume systematic historical Jesus study applying rigorous historical criteria.",
            "es": "Estudio histórico sistemático de Jesús en múltiples volúmenes aplicando criterios históricos rigurosos."
        }
    },
    "SRC_DUNN_JESUS": {
        "work": {
            "en": "Jesus Remembered (Christianity in the Making, Vol. 1)",
            "es": "Jesús Recordado (El Cristianismo en Formación, Vol. 1)"
        },
        "notes": {
            "en": "Explores how Jesus was remembered in oral tradition before written Gospels.",
            "es": "Explora cómo Jesús fue recordado en la tradición oral antes de los Evangelios escritos."
        }
    },
    "SRC_CROSSAN_JESUS": {
        "work": {
            "en": "The Historical Jesus: The Life of a Mediterranean Jewish Peasant",
            "es": "El Jesús Histórico: La Vida de un Campesino Judío Mediterráneo"
        },
        "notes": {
            "en": "Controversial reconstruction emphasizing Jesus as social revolutionary and peasant sage.",
            "es": "Reconstrucción controvertida enfatizando a Jesús como revolucionario social y sabio campesino."
        }
    },
    "SRC_WRIGHT_RESURRECTION": {
        "work": {
            "en": "The Resurrection of the Son of God",
            "es": "La Resurrección del Hijo de Dios"
        },
        "notes": {
            "en": "Defends historicity of bodily resurrection within Jewish context of Second Temple Judaism.",
            "es": "Defiende la historicidad de la resurrección corporal dentro del contexto judío del Judaísmo del Segundo Templo."
        }
    },
    "SRC_BAUCKHAM_EYEWITNESSES": {
        "work": {
            "en": "Jesus and the Eyewitnesses",
            "es": "Jesús y los Testigos Oculares"
        },
        "notes": {
            "en": "Argues that Gospels are based on eyewitness testimony, challenging form-critical skepticism.",
            "es": "Argumenta que los Evangelios se basan en testimonios de testigos oculares, desafiando el escepticismo de la crítica de formas."
        }
    },
    "SRC_HENGEL_CRUCIFIXION": {
        "work": {
            "en": "Crucifixion in the Ancient World and the Folly of the Message of the Cross",
            "es": "La Crucifixión en el Mundo Antiguo y la Locura del Mensaje de la Cruz"
        },
        "notes": {
            "en": "Study of crucifixion as Roman punishment and its scandal in ancient culture.",
            "es": "Estudio de la crucifixión como castigo romano y su escándalo en la cultura antigua."
        }
    },
    "SRC_ALLISON_JESUS": {
        "work": {
            "en": "Constructing Jesus: Memory, Imagination, and History",
            "es": "Construyendo a Jesús: Memoria, Imaginación e Historia"
        },
        "notes": {
            "en": "Explores methodology of historical Jesus research and role of memory in Gospel traditions.",
            "es": "Explora la metodología de la investigación del Jesús histórico y el papel de la memoria en las tradiciones evangélicas."
        }
    },
    "SRC_HURTADO_LORD": {
        "work": {
            "en": "Lord Jesus Christ: Devotion to Jesus in Earliest Christianity",
            "es": "Señor Jesucristo: Devoción a Jesús en el Cristianismo Primitivo"
        },
        "notes": {
            "en": "Study of early Christology and worship practices demonstrating early high Christology.",
            "es": "Estudio de la cristología primitiva y prácticas de adoración demostrando alta cristología temprana."
        }
    }
}

def add_spanish_translations(sources_file, output_file):
    """Add Spanish translations to work, notes, and citation_info fields."""
    with open(sources_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for source in data['sources']:
        source_id = source['id']
        
        if source_id in source_translations:
            trans = source_translations[source_id]
            
            # Convert work to bilingual
            if 'work' in trans:
                source['work'] = trans['work']
            elif 'work' in source and isinstance(source['work'], str):
                # If no translation, keep as English only
                source['work'] = {"en": source['work'], "es": source['work']}
            
            # Convert notes to bilingual
            if 'notes' in trans:
                source['notes'] = trans['notes']
            elif 'notes' in source and isinstance(source['notes'], str):
                source['notes'] = {"en": source['notes'], "es": source['notes']}
            
            # Convert citation_info to bilingual
            if 'citation_info' in trans:
                source['citation_info'] = trans['citation_info']
            elif 'citation_info' in source and isinstance(source['citation_info'], str):
                source['citation_info'] = {"en": source['citation_info'], "es": source['citation_info']}
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Added Spanish translations: {sources_file} → {output_file}")

# Process Century 1 sources
add_spanish_translations(
    'christianity_century_1/sources.json',
    'christianity_century_1/sources.json'
)

print("✓ Century 1 sources updated with Spanish translations")
