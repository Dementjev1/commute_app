import os
import json
from google import genai
from google.genai import types

def load_prompt(filename="system_prompt.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using basic default.")
        return "You are a helpful mobility assistant."

def get_ai_recommendation(data):
    # Use your key here
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    if not api_key:
        return {"error": "No API Key"}

    # Initialize the client
    client = genai.Client(api_key=api_key)
    
    model_id =model_id = 'gemini-2.0-flash-lite'

    config = types.GenerateContentConfig(
        system_instruction=load_prompt('prompt.txt'),
        response_mime_type='application/json'
    )

    results = []
    
    try:
        for event in data['calendar_events']:
            user_prompt = f"Data Context: {json.dumps(data)} \n\n Analyze this specific event: {json.dumps(event)}"
            
            response = client.models.generate_content(
                model=model_id,
                contents=user_prompt,
                config=config
            )
            
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            results.append(json.loads(clean_text))
            
        return results

    except Exception as e:
        print(f"API failed with: {e}")
        # If it still fails, check your API Studio: Is the key for 'Generative Language API'?
        return None
