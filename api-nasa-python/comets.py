import requests
import os  # Ejecuta comandos del OS

def get_comet_data(api_key):
    print(":::: Getting info ::::")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        # Show data
        # Print comet name
        print("Comet name: ", data["name"])
        # Magnitude
        print("Apsolute magnitude: ", data["absolute_magnitude_h"])
        # Estimated diameter max (km)
        print("Estimated diameter max (km): ", data["estimated_diameter"]["kilometers"]["estimated_diameter_max"])
        # Estimated diameter min (km)
        print("Estimated diameter min (km): ", data["estimated_diameter"]["kilometers"]["estimated_diameter_min"])
        # Estimated diameter max (ft)
        print("Estimated diameter max (ft): ", data["estimated_diameter"]["feet"]["estimated_diameter_max"])
        # Estimated diameter min (ft)
        print("Estimated diameter min (ft): ", data["estimated_diameter"]["feet"]["estimated_diameter_min"])
        # obital_data
        # last_observation_date
        print("Last observation date: ", data["orbital_data"]["last_observation_date"])
    except requests.exceptions.RequestException as e:
        print(f"Api error {e}")

# Main
api_get_nasa = "Vac7x7Mrv5WCk9qMuLRMvWEYV5WEEIvPzfyRFQsj"
get_comet_data(api_get_nasa)
