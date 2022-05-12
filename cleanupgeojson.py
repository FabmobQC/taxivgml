import json


string_dict = {
    "24h - 7 jours": "Mo-Su 00:00-24:00",
    "24 H - 7 J": "Mo-Su 00:00-24:00",
    "24h-7J": "Mo-Su 00:00-24:00",
    "24H - 7 J": "Mo-Su 00:00-24:00",
    "24H- 7J": "Mo-Su 00:00-24:00",
    "24H - 7H": "Mo-Su 00:00-24:00",
    "7J - 24H": "Mo-Su 00:00-24:00",
    "24-7": "Mo-Su 00:00-24:00",
    "24H-7J": "Mo-Su 00:00-24:00",
    "De soir": "Mo-Su 18:00-24:00",
    "Soir": "Mo-Su 18:00-24:00",
    "18H30 à 9H": "Mo-Su 18:30-09:00",
    "En tout temps": "Mo-Su 00:00-24:00",
    "18H à Minuit": "Mo-Su 18:00-24:00",
    "Lun au Ven de 8h00 à 19h00.": "Mo-Fr 08:00-20:00",
    "LUN au VEN de 8H à 20H": "Mo-Fr 08:00-20:00",
    "18H30 à 9H Mo-Su": "18:30-09:00",
    "LUN au VEN 8h à 18h": "Mo-Fr 08:00-18:00",
    "LUN à VEN 8h à 18h": "Mo-Fr 08:00-18:00",
    "18H00 à 24h00": "Mo-Su 18:00-24:00",
    "21h00 à 08h30": "Mo-Su 21:00-08:30",
    "20h00 à 05h30": "Mo-Su 20:00-05:30",
    "Lun au Ven de 8h00 à 18h00": "Mo-Fr 08:00-18:00",
    "18h00 à 07h00": "Mo-Su 18:00-07:00",
    "19H à 6H30": "Mo-Su 19:00-06:30",
    "6H30 à 19H": "Mo-Su 06:30-19:00",
    "5h00 à 17H00 - 7 Jours": "Mo-Su 05:00-17:00",
    "00h00 à 04h00 - 7 jours": "Mo-Su 00:00-04:00",
    "00h00 à 04h00 - 7 jours sur 7": "Mo-Su 00:00-04:00",
    "00h00 à 04h00 - 7 jours sur 7.": "Mo-Su 00:00-04:00"
}

with open("postestaxi.geojson", "r+") as file:
    data = json.load(file)

    for item in data["features"]:

        item["properties"]["lat"] = item["properties"].pop("Lat")
        item["properties"]["long"] = item["properties"].pop("Long")
        item["properties"]["name"] = item["properties"].pop("Nom")
        item["properties"]["capacity"] = item["properties"].pop("Nb_place")
        #item["properties"]["contact:phone"] = ""
        item["properties"]["addr:full"] = item["properties"].pop(
            "Localisation")

        type = item["properties"].pop("Type")

        status = item["properties"].pop("Etat_poste")

        if status == "Poste public temporaire" or status == "Poste prive temporaire" or status == "Poste encommun temporaire":
            item["properties"]["temporary"] = "yes"

        if status == "Poste public actif" or status == "Poste encommun actif" or status == "Poste prive actif" or status == "Poste public temporaire" or status == "Poste encommun temporaire" or status == "Poste prive temporaire":
            item["properties"]["access"] = "yes"
        else:
            item["properties"]["access"] = "no"

        if type == "Public":
            item["properties"]["ownership"] = "public"

        if type == "Privé":
            item["properties"]["ownership"] = "private"

        # This type of ownership needs to be validated
        if type == "En commun":
            item["properties"]["ownership"] = "public_nonprofit"

        old_value = item["properties"].pop("Heure_operation")

        if old_value in string_dict.keys():
            item["properties"]["opening_hours"] = string_dict[old_value]
        else:
            print(old_value, item["properties"]["name"])
            item["properties"]["opening_hours"] = "Mo-Su 00:00-24:00"

        item["properties"]["amenity"] = "taxi"

with open('postestaxi_new.geojson', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
