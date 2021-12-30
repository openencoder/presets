
import os
import json

index = []
KEYS = ["title", "type", "format", "author", "parameters"]
URL = "https://github.com/openencoder/presets/raw/main/presets/"

with open("index.json", "w", encoding="utf-8") as out:
    for file in os.scandir("presets"):
        with open(file.path, "r", encoding="utf-8") as fp:
            h = json.loads(fp.read())

            for key in KEYS:
                if key not in h:
                    raise Exception(f"parameter {key} is missing in {file.path}")


            del h["parameters"]

            h["url"] = URL + file.name
            index.append(h)


    if len(index) > 0:
        json.dump(index, out, indent=2)
