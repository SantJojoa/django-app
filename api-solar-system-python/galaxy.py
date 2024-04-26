import os
import requests

def get_data(body_type):
    fields = ['englishName', 'gravity', 'inclination', 'bodyType']
    try:
        response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
        response.raise_for_status()

        data = response.json()
        if isinstance(data, dict) and 'bodies' in data:
            bodies = data['bodies']
            print("Type:", body_type)  
            for body in bodies:
                if body['bodyType'] == body_type:  
                    print("#########################")
                    for field in fields:
                        print(f"{field}: {body.get(field)}")
        else:
            print("Invalid data.")
            print(":", data)  
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error de API: {e}")

# Principal
while True:
    print("#### MAIN MENU ####")
    print("[1]. Planets")
    print("[2]. Moons")
    print("[3]. Stars")
    print("[4]. Asteroids")
    print("[5]. Comets")
    print("[6]. Exit")
    option = input("Please select an option: ")

    if option == '6':
        print("Exiting...")
        break
    
    body_types = {
    '1': "Planet",
    '2': "Moon",
    '3': "Star",
    '4': "Asteroid",
    '5': "Comet"
    }

    if option not in body_types:
        print("Invalid options")
        continue

    body_type = body_types[option]
    info = get_data(body_type)