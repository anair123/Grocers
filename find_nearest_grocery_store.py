import pandas as pd
import numpy as np
import requests

locations = pd.read_excel('locations.xlsx')
print(locations)
print("")

def get_location_info_by_pincode(pincode: str):
    """Get latitude, longitude, and country using OpenStreetMap (Nominatim) by pincode."""
    try:
        geo_url = f"https://nominatim.openstreetmap.org/search?postalcode={pincode}&format=json&limit=1"
        geo_response = requests.get(geo_url, headers={"User-Agent": "FastAPI-Location-App"}).json()

        if not geo_response:
            return {"error": "Invalid pincode"}

        lat, lon = geo_response[0]["lat"], geo_response[0]["lon"]
        country = geo_response[0]["display_name"]
        return {"latitude": lat, "longitude": lon, "country": country}
    except Exception as e:
        print(e)

# Haversine formula to calculate distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
    lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = np.sin(dlat / 2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    distance = R * c
    return distance

# Apply the distance calculation for each row
user_location = get_location_info_by_pincode(pincode=10967)

input_lat, input_lon = float(user_location['latitude']), float(user_location['longitude'])


locations['distance_km'] = locations.apply(lambda row: haversine(input_lat, input_lon, row['latitude'], row['longitude']), axis=1)
df_sorted = locations.sort_values('distance_km')

print(df_sorted)