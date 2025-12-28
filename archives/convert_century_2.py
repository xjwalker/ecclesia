"""
Convert Century 2 events to bilingual format.
"""
import json

# Read Century 2 events
with open('christianity_century_2/events.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# English translations for Spanish titles
title_translations = {
    "Martirio de Ignacio de Antioquía": "Martyrdom of Ignatius of Antioch",
    "Excomunión de Marción y el marcionismo": "Excommunication of Marcion and Marcionism",
    "Martirio de Policarpo de Esmirna": "Martyrdom of Polycarp of Smyrna",
    "Martirio de Justino Mártir": "Martyrdom of Justin Martyr",
    "Ireneo escribe Contra las Herejías": "Irenaeus Writes Against Heresies",
    "Martirios de Lyon y Vienne": "Martyrdoms of Lyons and Vienne"
}

# English translations for Spanish context, significance, confidence_rationale
translations = {
    "EVT_0110_IGNATIUS": {
        "context_en": "Ignatius, bishop of Antioch, was arrested and transported to Rome for execution. During the journey he wrote seven letters to churches in Asia Minor and Rome, which are crucial documents of early Christianity. The letters reveal an already established episcopal structure (bishop, presbyters, deacons), emphasize church unity, and contain the first clear reference to 'Christianity' as a term (vs. 'Judaism'). Ignatius insisted on being martyred, writing to the Romans not to intervene: 'I am God's wheat, and I shall be ground by the teeth of beasts.' His letters also combat docetism (the idea that Jesus had no real body) and emphasize the reality of the Eucharist as 'flesh of Christ.'",
        "confidence_rationale_en": "Medium Confidence (C2) because: 1) The seven authentic letters exist in 4th century manuscripts, 2) Eusebius (4th century) quotes Ignatius extensively, confirming early tradition, 3) The date ~110 CE is based on references to Trajan's reign and correlation with Polycarp, 4) There are no direct contemporary sources of the martyrdom itself, only Ignatius's letters, 5) Some details of his death are legendary (later additions). The letters are authentic and the martyrdom historical, but specific details have uncertainty.",
        "significance_en": "Ignatius's letters are crucial early evidence of hierarchical episcopal structure (monarchical bishop), which would become the standard model of ecclesiastical organization. His emphasis on visible church unity under the bishop influenced Catholic ecclesiology. His eucharistic theology (real presence) anticipated later doctrines. Ignatius's martyrdom exemplifies the theology of martyrdom as imitation of Christ."
    },
    "EVT_0144_MARCION": {
        "context_en": "Marcion, a wealthy shipowner from Sinope (Black Sea), came to Rome and presented a radical theology: the God of the Old Testament (Creator, just, wrathful) was different from the God of the New Testament (Father of Jesus, love, mercy). He rejected the entire OT and most of the NT, accepting only an edited Luke and 10 letters of Paul. According to Marcion, the material world was created by the inferior God of the OT, and Jesus came to reveal the superior God. The church of Rome excommunicated him in 144 CE, but his movement grew rapidly, establishing parallel churches throughout the empire. The Marcionite challenge forced the orthodox church to define its own canon of Scriptures and articulate the relationship between OT and NT.",
        "confidence_rationale_en": "Medium Confidence (C2) because: 1) Multiple patristic sources (Irenaeus, Tertullian, Epiphanius) describe Marcion, though written decades later, 2) No direct writings of Marcion survive, only quotations from opponents, 3) The date of 144 CE is traditional but approximate, 4) Marcionite influence is indisputable (Marcionite churches existed until the 5th century), 5) Some details may be polemic/exaggerated. The existence of Marcion and his movement is certain, but reconstructing his precise theology is difficult.",
        "significance_en": "Marcionism was the most important catalyst for the formation of the NT canon. By proposing his own restricted canon, he forced the church to articulate which books were authoritative. It also compelled orthodoxy to develop theology of OT and NT unity, and the continuity of God's salvific plan. Irenaeus and Tertullian wrote extensively against Marcion, developing hermeneutical tools that shaped Christian theology. Marcionism demonstrated that Christianity could develop in radically different directions without centralized authority."
    },
    "EVT_0155_POLYCARP": {
        "context_en": "Polycarp, bishop of Smyrna and alleged disciple of the apostle John, was arrested during local persecutions. At 86 years old, he refused to deny Christ before the Roman proconsul. When offered to save his life by cursing Christ, he responded: 'Eighty-six years I have served him, and he never did me wrong. How can I blaspheme my King who saved me?' He was burned at the stake, and the letter from the church of Smyrna describes his death with language imitating Christ's passion. The account includes miraculous elements: fire that doesn't burn him, fragrance of incense, dove emerging from his body. It is the oldest Christian martyrdom account outside the NT.",
        "confidence_rationale_en": "Medium Confidence (C2) because: 1) The letter (Martyrium Polycarpi) exists in 4th century manuscripts, 2) Irenaeus, who knew Polycarp, confirms his existence and connection with John, 3) Eusebius preserves traditions about Polycarp, 4) The date varies (155, 156, or 167 CE depending on chronological calculations), 5) Miraculous elements of the account are clearly theological/liturgical, 6) The historical core (an elderly bishop martyred in Smyrna) is solid, but specific details are embellished.",
        "significance_en": "The Martyrdom of Polycarp established the genre of acta martyrum (acts of martyrs) that proliferated in subsequent centuries. It presented martyrdom as imitatio Christi (imitation of Christ), using deliberate passion language. Polycarp's connection with the apostle John made him a crucial link between the apostolic and post-apostolic era, legitimizing the tradition of Asia Minor. His refusal to compromise established the standard for Christian resistance to imperial authority. The cult of martyrs that emerged afterward was based partially on this account."
    },
    "EVT_0165_JUSTIN_MARTYR": {
        "context_en": "Justin, a philosopher converted to Christianity, established a Christian school in Rome where he taught that Christianity was the 'true philosophy.' He wrote apologies (defenses) addressed to Emperor Antoninus Pius and his successor Marcus Aurelius, arguing that Christians were loyal citizens unjustly persecuted. His works describe Christian practices (baptism, Eucharist) in unique detail for the 2nd century. His Logos theology attempted to reconcile Greek philosophy with Scripture: the Logos (divine Reason) that illuminated Socrates and Plato was fully incarnated in Christ. He was arrested along with six disciples and executed by beheading after refusing to sacrifice to the gods.",
        "confidence_rationale_en": "Medium Confidence (C2) because: 1) His two Apologies and Dialogue with Trypho survive in medieval manuscripts, 2) The Acts of his martyrdom exist but are of debated authenticity (possible later embellishment), 3) Eusebius mentions and quotes him extensively, 4) The date ~165 CE is approximate, based on references to emperors, 5) His existence and work are indisputable, but details of his death less certain. The writings are solid primary evidence.",
        "significance_en": "Justin was the first great Christian intellectual to attempt synthesis between Greek philosophy and Christian faith, establishing a pattern for later Christian theology. His apologetics demonstrated that Christianity could compete intellectually with pagan philosophies. His description of Christian liturgy (Sunday baptism, reading of 'memoirs of apostles,' Eucharist) is invaluable evidence of 2nd century practices. His Logos theology influenced the development of Christology. His martyrdom underscored the tension between loyalty to the empire and loyalty to Christ."
    },
    "EVT_0180_IRENAEUS": {
        "context_en": "Irenaeus, bishop of Lyons (Gaul), wrote a massive five-volume refutation of Gnosticism, especially the Valentinian system. He connected with the apostolic era through Polycarp, who knew John. His work establishes criteria of orthodoxy: 1) Four canonical gospels (no more, no less), 2) Apostolic succession (bishops in uninterrupted line from apostles), 3) Rule of faith (basic shared creed), 4) Unity of OT and NT (against Marcionites). He argued that Gnostic Christianity was a late innovation, not secret apostolic tradition. He defended the goodness of material creation against Gnostic dualism. His list of bishops of Rome up to his time is crucial historical evidence.",
        "confidence_rationale_en": "High Confidence (C1) because: 1) Against Heresies survives almost complete in Latin translation (partial Greek original), 2) Multiple medieval manuscripts confirm the text, 3) Eusebius quotes Irenaeus extensively, confirming authenticity, 4) Dating ~180 CE is solid based on references to emperors and historical context, 5) His immediate influence on Tertullian and Hippolytus confirms early circulation. It is one of the most reliable patristic sources of the 2nd century.",
        "significance_en": "Irenaeus established the framework of Christian orthodoxy for centuries: canon of four gospels, apostolic succession as criterion of authority, and unity of Testaments. His refutation of Gnosticism preserved information about Gnostic systems that would otherwise have been lost. His theology of recapitulation (Christ recapitulates human history) influenced Eastern soteriology. His list of Roman bishops is crucial historical evidence for studying institutional development. His work marked the transition from charismatic to institutional Christianity."
    },
    "EVT_0177_LYON_MARTYRS": {
        "context_en": "During the reign of Marcus Aurelius, violent persecution erupted against Christians in Lyons and Vienne (Gaul). The pagan mob attacked Christians, prohibiting them access to public spaces, markets, and baths. Mass arrests followed. Tortures were extreme: Blandina, a slave woman, was tortured repeatedly but refused to apostatize, saying only 'I am a Christian, we do nothing wrong.' Pothinus, a 90-year-old bishop, died in prison after a beating. Christians were displayed in the amphitheater, scourged, attacked by beasts, roasted on an iron chair. Blandina was finally wrapped in a net and thrown to a bull. The letter from the churches of Lyons and Vienne to Asia Minor, preserved by Eusebius, is an exceptional martyrdom document.",
        "confidence_rationale_en": "Medium Confidence (C2) because: 1) Eusebius (4th century) preserves the letter, quoting it extensively in his Ecclesiastical History, 2) We don't have the original text, only Eusebius's version, 3) The date 177 CE is solid based on Marcus Aurelius's reign, 4) Some details (miracles, martyrs' speeches) may be embellished, 5) The historical core (severe persecution in Gaul with multiple martyrs) is indisputable, 6) Marcus Aurelius, Stoic philosopher, effectively allowed local persecutions of Christians.",
        "significance_en": "The martyrdoms of Lyons demonstrated that Christianity had penetrated to the westernmost regions of the empire. The figure of Blandina, a slave who surpassed nobles in resistance, exemplified Christian egalitarianism and the inverted power of God's kingdom. The letter influenced later martyrdom literature, establishing tropes: Christians as athletes of God, martyrdom as rebirth, torture as divine test. Preservation by Eusebius ensured its impact on ecclesiastical memory. It showed tension between imperial philosophy (Marcus Aurelius) and Christian persecution."
    }
}

# Convert events to bilingual format
for event in data['events']:
    event_id = event['id']
    
    # Convert title
    spanish_title = event['title']
    event['title'] = {
        "es": spanish_title,
        "en": title_translations.get(spanish_title, spanish_title)
    }
    
    # Description is already in English, need Spanish
    english_desc = event['description']
    spanish_desc_map = {
        "EVT_0110_IGNATIUS": "Obispo Ignacio de Antioquía martirizado en Roma; sus siete cartas en ruta revelan estructura episcopal temprana y teología eucarística.",
        "EVT_0144_MARCION": "Marción excomulgado de Roma por teología radical rechazando el Antiguo Testamento; su canon impulsa a la iglesia ortodoxa a formalizar la Escritura.",
        "EVT_0155_POLYCARP": "Policarpo, discípulo de Juan, martirizado a los 86 años; su relato de muerte se convierte en modelo para literatura de martirio cristiano.",
        "EVT_0165_JUSTIN_MARTYR": "Justino Mártir, filósofo y apologista cristiano, ejecutado en Roma; sus escritos unen filosofía griega y teología cristiana.",
        "EVT_0180_IRENAEUS": "Ireneo escribe Contra las Herejías, refutando sistemáticamente el gnosticismo y estableciendo criterios ortodoxos: cuatro evangelios, sucesión apostólica.",
        "EVT_0177_LYON_MARTYRS": "Persecución masiva en Galia resulta en martirios horrificos incluyendo Blandina y Potino; carta preservada por Eusebio."
    }
    
    event['description'] = {
        "es": spanish_desc_map.get(event_id, english_desc),
        "en": english_desc
    }
    
    # Context, confidence_rationale, significance - already Spanish, need English
    trans = translations.get(event_id, {})
    
    event['context'] = {
        "es": event['context'],
        "en": trans.get('context_en', event['context'])
    }
    
    event['confidence_rationale'] = {
        "es": event['confidence_rationale'],
        "en": trans.get('confidence_rationale_en', event['confidence_rationale'])
    }
    
    event['significance'] = {
        "es": event['significance'],
        "en": trans.get('significance_en', event['significance'])
    }

# Write bilingual version
with open('christianity_century_2/events_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Century 2 events converted to bilingual format")
