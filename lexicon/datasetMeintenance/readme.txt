wordict.json is for set of japanese words and some more data I guess. unfiletered.
tripordict.json is for set of filtered and worked on data that

wordpul.py pulls data from the internet into the wordict.json
midler.py filters  wordict.json and makes gradually builds tripordict.json

this program is not intended to be runed during compilation, but before it.
while .venv is activated
first run wordpul.py by typing : "python lexicon/datasetMeintenance/wordpul.py"
than run midler.py by typing: "python lexicon/datasetMeintenance/midler.py"