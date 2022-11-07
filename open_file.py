import json

with open("note.json", "r") as f:
    text = json.load(f)

for txt in text["authors"]:
    print(txt["author_name"], ":", txt["rating"])
