import google.generativeai as genai
import os
from config import GOOGLE_API_KEY  # Import API key

# Configure API
genai.configure(api_key=GOOGLE_API_KEY)

def get_travel_options(source, destination):
    """Fetches travel options from AI model."""
    prompt = f"Find the best travel options from {source} to {destination}, including flights, trains, buses, and cabs with approximate costs."
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response else "No response received. Try again."

# Test function
if __name__ == "__main__":
    print(get_travel_options("New York", "Los Angeles"))
