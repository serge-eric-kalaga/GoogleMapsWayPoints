import requests
import json

def sort_points_by_distance(origin, points):
    # Utilise l'API Google Maps pour obtenir les distances entre l'origine et les autres points
    distances = []
    for point in points:
        url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={point}&key=API_KEY'
        response = requests.get(url)
        data = json.loads(response.text)
        distance = data['rows'][0]['elements'][0]['distance']['value']
        distances.append((point, distance))
    
    # Trie les points en fonction de leur distance à l'origine
    sorted_points = [x[0] for x in sorted(distances, key=lambda x: x[1])]
    
    # ajout l'origine en premier
    sorted_points.insert(0, origin)
    return sorted_points


print(sort_points_by_distance("Ouagadougou", ["Banfora", "Dori", "Ziniare"]))

