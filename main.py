import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# ==========================================================
# Load environment variables from the .env file
# ==========================================================
load_dotenv()

# ==========================================================
# User Details
# ==========================================================
GENDER = "male"
YOUR_AGE = 21
WEIGHT_KG = 60
HEIGHT_CM = 160

# ==========================================================
# Nutritionix API Credentials
# ==========================================================
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
EXERCISE_ENDPOINT = os.getenv("EXERCISE_ENDPOINT")

# ==========================================================
# Sheety API Credentials
# ==========================================================
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

# Option 1 : Bearer Token Authentication
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

# Option 2 : Basic Authentication
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

# ==========================================================
# Nutritionix API Headers
# ==========================================================
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# ==========================================================
# Ask user about today's workout
# Examples:
# - ran 5 km
# - cycled for 45 minutes
# - swam for 30 minutes
# ==========================================================
exercise_data = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": YOUR_AGE,
}

# ==========================================================
# Send request to Nutritionix API
# ==========================================================
exercise_response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_data,
    headers=nutritionix_headers,
)

# Stop the program if an error occurs
exercise_response.raise_for_status()

# Convert response into Python dictionary
result = exercise_response.json()

# ==========================================================
# Get Current Date and Time
# ==========================================================
today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

# ==========================================================
# Save workout data into Google Sheets using Sheety API
# ==========================================================
for exercise in result["exercises"]:

    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # ======================================================
    # Option 1 : Bearer Token Authentication
    # ======================================================
    if SHEETY_TOKEN:

        sheety_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        sheet_response = requests.post(
            url=SHEETY_ENDPOINT,
            json=sheet_inputs,
            headers=sheety_headers
        )

    # ======================================================
    # Option 2 : Basic Authentication
    # ======================================================
    elif SHEETY_USERNAME and SHEETY_PASSWORD:

        sheet_response = requests.post(
            url=SHEETY_ENDPOINT,
            json=sheet_inputs,
            auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
        )

    # ======================================================
    # No Authentication Found
    # ======================================================
    else:
        raise Exception(
            "No Sheety Authentication Found!\n"
            "Please configure either:\n"
            "1. SHEETY_TOKEN\n"
            "OR\n"
            "2. SHEETY_USERNAME & SHEETY_PASSWORD"
        )

    # Raise an exception if Sheety request fails
    sheet_response.raise_for_status()

    print(f"✅ {exercise['name'].title()} added successfully!")
    print(sheet_response.json())

print("\n🎉 Workout data saved successfully!")