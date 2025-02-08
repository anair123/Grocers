from fastapi import FastAPI, Query
import requests
from fastapi.middleware.cors import CORSMiddleware
import openai
from openai import OpenAI

import grocers.Grocers.backend.config as config
import os
import pandas as pd

from fuzzywuzzy import process


app = FastAPI()

# Allow requests from your React frontend (change the origin if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update if frontend is deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(
    api_key=config.openai_apikey,  # This is the default and can be omitted
)

# Function to fetch ingredients from OpenAI
def getIngredients(dish):
    prompt = f"List the ingredients for the following dish: {dish}. Separate each ingredient by '|'."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    response_content = response.choices[0].message.content
    ingredients = response_content.split('|')
    ingredients = [i.strip(" ") for i in ingredients if i]
    return ingredients

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
        return {"error": str(e)}

def get_timezone_and_time(lat: float, lon: float):
    """Get timezone and current time using WorldTimeAPI."""
    try:
        timezone_url = f"http://worldtimeapi.org/api/timezone"
        timezone_list = requests.get(timezone_url).json()

        # Find the closest timezone
        selected_timezone = "Etc/UTC"  # Default to UTC if no match
        for tz in timezone_list:
            if tz.startswith("Etc/") or tz.startswith("GMT"):
                continue
            if tz.split("/")[-1].lower() in [str(lat), str(lon)]:
                selected_timezone = tz
                break

        time_url = f"http://worldtimeapi.org/api/timezone/{selected_timezone}"
        time_response = requests.get(time_url).json()

        return {"timezone": time_response["timezone"], "current_time": time_response["datetime"]}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Internal error: {str(e)}"}

@app.get("/get_time")
def get_time_by_pincode(pincode: str = Query(..., description="Enter pincode")):
    location = get_location_info_by_pincode(pincode)
    if "error" in location:
        return location

    time_info = get_timezone_and_time(float(location["latitude"]), float(location["longitude"]))
    return {**location, **time_info}

@app.get("/get_dishname")
def get_dish_name(dishname: str = Query('', description="Enter the dish name")):
    # If dishname is provided, print it and fetch the ingredients
    if dishname:
        print(f"Dish Name: {dishname}")
        ingredients = getIngredients(dishname)  # Get ingredients from OpenAI
        return {"message": f"Dish name is: {dishname}", "ingredients": ingredients}
    else:
        print("No dish name provided.")
        return {"message": "No dish name provided"}
