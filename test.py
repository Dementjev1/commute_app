import json
from app import get_ai_recommendation

with open('commute_data.json', 'r') as f:
    data = json.load(f)

print(f'{get_ai_recommendation(data)}')
