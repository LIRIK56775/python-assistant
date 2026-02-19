import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Ошибка: API-ключ не найден в файле .env")
else:
    genai.configure(api_key=api_key)
    
SYSTEM_PROMPT = """
Ты — харизматичный ИИ-ассистент Джарвис. Ты ведешь диалог и помогаешь управлять ПК.
Возвращай ТОЛЬКО JSON: {"command": "...", "argument": "...", "message": "..."}
"""

model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

chat = model.start_chat(history=[]) # Создаем объект чата с пустой историей

def process_command(user_input):
    try:
        response = chat.send_message(user_input) # Отправляем сообщение в чат, он сам сохранит историю
        
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        return {"command": "none", "argument": "", "message": f"Ошибка связи: {e}"}