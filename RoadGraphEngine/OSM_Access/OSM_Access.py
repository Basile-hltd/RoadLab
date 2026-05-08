import math
import requests
import json

main_api_url = "https://api.openstreetmap.org/"

def Version():
    try:
        response = requests.get(main_api_url+"/api/versions.json")
        json_data  = response.json()

        version = json_data["version"]

        return version
    
    except:
        return None
    

def tile_bbox(lat, lon, size_m):
    half = size_m / 2

    # conversion mètres → degrés latitude
    dlat = half / 111320

    # conversion mètres → degrés longitude (corrigé latitude)
    dlon = half / (111320 * math.cos(math.radians(lat)))

    return (
        lon - dlon,  # left
        lat - dlat,  # bottom
        lon + dlon,  # right
        lat + dlat   # top
    )
    
def GetTile(lat, lon, size):
    bbox = tile_bbox(lat, lon, size)
    params = {
        "bbox": ",".join(map(str, bbox))
    }
    
    response = requests.get(main_api_url+"/api/0.6/map", params=params)

    with open("result.txt", "w", encoding="utf-8") as f:
            f.write(response.text)

    return True

    try:
        bbox = tile_bbox(lat, lon, size)
        params = {
            "bbox": ",".join(map(str, bbox))
        }
        
        response = requests.get(main_api_url+"/api/0.6/map", params=params)

        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(response.json(), f, indent=4)

        return True
    
    except:
        return None