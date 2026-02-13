import lexicon_engine
import json

print("Initializing C++ Engine (ONCE)...")
# This runs only once when the server starts
shared_lexicon = lexicon_engine.RaList()

# load json tada file
try:
    with open('lexicon/datasetMeintenance/tripordict.json', 'r', encoding='utf-8') as f:
        jword = json.load(f)
    print("Success! Opened tripordict.json")
except FileNotFoundError:
    print("tripordict.json could not be found !") 


shared_lexicon.add_List(jword)

