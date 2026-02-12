import pandas as pd
import json

# 1. The URL of the raw CSV file you found
csv_url = "https://raw.githubusercontent.com/elzup/jlpt-word-list/master/src/n5.csv"

# 2. Read the CSV directly from the web
# The file uses 'expression' for the word and 'reading' for the hiragana
df = pd.read_csv(csv_url)

# 3. Select only the columns you need
# 'expression' = Original Word (Kanji)
# 'reading'    = Hiragana Reading
# 'meaning'    = English Meaning
clean_df = df[['expression', 'reading', 'meaning']]

# 4. Rename them to something clearer (optional)
clean_df.columns = ['original', 'hiragana', 'meaning']

# 5. Convert to JSON
# 'records' mode creates a list of objects: [{"original": "...", ...}, ...]
json_data = clean_df.to_json(orient='records', force_ascii=False, indent=2)

# 6. Save to a file
try:
    with open('lexicon/datasetMeintenance/wordict.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
    print("Success! Created 'wordict.json' with", len(clean_df), "words.")
except FileNotFoundError:
    print("wordict.json could not be found !") 