import json
import pykakasi

# Initialize the converter
kks = pykakasi.kakasi()

# Your list of words (You can load this from a text file instead)
raw_words = [ ]

try: 
    with open('lexicon/datasetMeintenance/wordict.json', 'r', encoding='utf-8') as f:
        wordFile = json.load(f);  
    print("Success! opened 'wordict.json' ")
except FileNotFoundError:
    print("wordict.json could not be found !") 

for word in wordFile:
    raw_words.append(word.get('original'))

#import os
#from django.conf import settings
#path = os.path.join(settings.BASE_DIR, 'lexicon/datasetMeintenance/wordict.json')

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