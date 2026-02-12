import json
import pykakasi

# Initialize the converter
kks = pykakasi.kakasi()

# Your list of words (You can load this from a text file instead)
raw_words = [
    "学生", "先生", "学校", "勉強",  # Education
    "猫", "犬", "鳥",               # Animals
    "食べる", "飲む", "寝る"         # Verbs
]

dataset = []

for word in raw_words:
    result = kks.convert(word)
    
    # Combine the pieces (pykakasi splits by character)
    hiragana = "".join([item['hira'] for item in result])
    romaji = "".join([item['hepburn'] for item in result])
    
    entry = {
        "word": word,
        "reading": hiragana,
        "romaji": romaji
    }
    dataset.append(entry)

# Save to JSON
try: 
    with open('lexicon/datasetMeintenance/tripordict.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    print("Success! Created 'tripordict.json' ")
except FileNotFoundError:
    print("tripordict.json could not be found !") 