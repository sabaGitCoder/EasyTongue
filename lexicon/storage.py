import lexicon_engine

print("Initializing C++ Engine (ONCE)...")
# This runs only once when the server starts
shared_lexicon = lexicon_engine.RaList()

# Pre-load data here later
shared_lexicon.add_words({"がくせい", "みどり", "あんぜんな", "ざんねんですね"})