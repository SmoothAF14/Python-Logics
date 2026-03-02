ships = [
    {
        "name": "Ship1",
        "containers": [
            {
                "items": [
                    {"name": "Glass", "type": "Fragile", "weight": 15, "dest": "LON"},
                    {"name": "Steel", "type": "Heavy", "weight": 50, "dest": "NYC"},
                ]
            }
        ]
    },
    {
        "name": "Ship2",
        "containers": [
            {
                "items": [
                    {"name": "Vase", "type": "Fragile", "weight": 12, "dest": "LON"},
                    {"name": "Paper", "type": "Normal", "weight": 5, "dest": "LON"},
                ]
            }
        ]
    }
]

result = [
    item["name"]
    for ship in ships
    for container in ship["containers"]
    for item in container["items"]
    if item["type"] == "Fragile"
    and item["dest"] == "LON"
    and item["weight"] > 10
]

print(result)