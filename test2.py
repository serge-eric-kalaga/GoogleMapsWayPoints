import requests
import json



def find_optimal_route(origin, destinations, api_key):
    optimal_route = [origin]
    current = origin
    while len(destinations) > 0:
        closest_destination, closest_distance = None, float('inf')
        for destination in destinations:
            print(destination)
            url = (f'https://maps.googleapis.com/maps/api/directions/json?'
                   f'origin={current}&destination={destination}&key={api_key}')
            response = requests.get(url)
            data = json.loads(response.text)
            distance = data['routes'][0]['legs'][0]['distance']['value']
            if distance < closest_distance:
                closest_distance = distance
                closest_destination = destination
        optimal_route.append(closest_destination)
        current = closest_destination
        destinations.remove(closest_destination)
    return optimal_route

result = find_optimal_route("Nonsin", ["Ouidi", "Larle", "Gounghin", "Ouaga 2000"], "AIzaSyAgsnYWU-sVcj1yW7cjfcCmW_1-Daedekk")

print(result)
