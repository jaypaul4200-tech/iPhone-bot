import os
import time
from google import genai

def run_bot():
    # 1. Grab your API key from Render's environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY is missing in Render environment variables!")
        return

    print("🚀 Initializing Gemini Cloud Client...")
    # 2. Connect to the Google Cloud AI cluster
    client = genai.Client(api_key=api_key)

    print("🤖 Testing bot connection to Gemini...")
    # 3. Send a test message to ensure the cloud pipeline works
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello! Confirm you are online and working.",
    )
    
    print(f"📡 Response from Gemini Cloud: {response.text}")
    print("✨ Setup successful! Bot is monitoring.")

    # 4. Keeps the cloud container running indefinitely
    while True:
        # This is where your market tracking logic will eventually go loop by loop
        time.sleep(60) 

if __name__ == "__main__":
    run_bot()
