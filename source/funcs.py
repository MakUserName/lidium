import json

def save(x, y) -> None:
    data = {"player.save.pos": [x,y]}
    with open('./client/latest.json', 'w') as file:json.dump(data, file, indent=4)

def load() -> list:
    localList = []
    with open('./client/latest.json', 'r') as file:
        stock = json.load(file)
        pos = stock['player.save.pos'];localList.append(pos)
    return localList