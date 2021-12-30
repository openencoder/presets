
import os
import json

index = []
PATH = "presets"
KEYS = ["title", "type", "format", "author", "parameters"]
URL = "https://github.com/openencoder/presets/raw/main/presets/"

with open("index.json", "w", encoding="utf-8") as out:
    for file in sorted(os.listdir(PATH)):
        with open(os.path.join(PATH, file), "r", encoding="utf-8") as fp:
            h = json.loads(fp.read())

            for key in KEYS:
                if key not in h:
                    raise Exception(f"parameter {key} is missing in {file}")


            del h["parameters"]

            h["url"] = URL + file
            index.append(h)


    if len(index) > 0:
        json.dump(index, out, indent=2)
