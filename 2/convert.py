import json

piles = json.load(open("candyPiles.json"))
print("\n".join(map(str, piles)))