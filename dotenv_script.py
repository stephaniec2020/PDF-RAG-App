import json
from dotenv import load_dotenv
import os

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_to_env_file(env_file_path, keys):
    with open(env_file_path, 'w') as file:
        for key, value in keys.items():
            file.write(f"{key.upper()}={value}\n")

load_dotenv()

# Read JSON file
json_data = read_json_file('keys.json')

# Extract required keys
open_ai_key = json_data.get('OPENAI_API_KEY', None)
hugging_face_api = json_data.get('HUGGINGFACEHUB_API_TOKEN', None)

# Write keys to .env file
write_to_env_file('.env', {'OPENAI_API_KEY': open_ai_key, 'HUGGINGFACEHUB_API_TOKEN': hugging_face_api})

# Optional: Print the loaded environment variables
print("OpenAI Key:", open_ai_key)
print("Hugging Face API Key:", hugging_face_api)
