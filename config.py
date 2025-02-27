import os
# Get API key from GitHub Secret (set during deployment)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing API Key! Set GOOGLE_API_KEY in your environment.")
