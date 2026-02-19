import webbrowser
import os
import pathlib
import subprocess
import pyautogui
import pyttsx3
import time
import edge_tts
import asyncio
import pygame

pygame.mixer.init()

def say(text):
    """Основная функция для вызова из main.py"""
    if text:
        print(f"Джарвис: {text}")
        # Запускаем асинхронную часть внутри обычной функции
        asyncio.run(_generate_and_play(text))

async def _generate_and_play(text):
    voice = "ru-RU-DmitryNeural" # Тот самый крутой мужской голос
    output_file = "answer.mp3"
    
    # Создаем аудиофайл
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    
    # Загружаем и играем
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()
    
    # Ждем пока договорит
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
    
    # Выгружаем файл, чтобы его можно было удалить
    pygame.mixer.music.unload()
    
    if os.path.exists(output_file):
        os.remove(output_file)
    pass

def search(argument):
    if argument == "":
        return("Пожалуйста, укажите, что вы хотите найти")
        
    try:        
        url = "https://www.google.com/search?q=" + argument.replace(" ", "+")
        webbrowser.open(url)
        return(f"Ищу {argument} в интернете")
    except Exception as e:
        return(f"Ошибка при поиске: {e}")
    
def browser(argument):
    try:
        os.startfile("msedge.exe")        
        return("Открываю браузер")
    except Exception as e:
        return(f"Ошибка при открытии браузера: {e}")

def site(argument):
    sites = {
        "ютуб": "https://www.youtube.com/",
        "гугл": "https://www.google.com/",
        "гитхаб": "https://www.github.com/",
    }
    
    try:
        url = sites.get(argument.lower(),f"https://{argument}")
        webbrowser.open(url)
        return(f"Открываю сайт {argument}")
    except Exception as e:
        return(f"Ошибка при открытии сайта: {e}")
    
def notepad(argument):
    try:
        os.startfile("notepad.exe")
        return("Открываю блокнот")
    except Exception as e:
        return(f"Ошибка при открытии блокнота: {e}")
    
def folder(argument):
    argument = argument.lower().strip()
    
    folders = {
        "загрузки": os.path.expanduser("~/Downloads"),
        "рабочий стол": os.path.expanduser("~/Desktop"),
        "документы": os.path.expanduser("~/Documents"),
    }
    
    target_path = folders.get(argument, os.path.expanduser(f"~/Desktop"))
    
    try:
        os.startfile(target_path)
        if argument in folders:
            return(f"Открываю папку {argument}")
        else:
            return(f"Открываю папку рабочий стол, так как папка '{argument}' не распознана")
    except Exception as e:
        return(f"Ошибка при открытии папки: {e}")
    
def type_text(argument):
    if argument == "":
        return("Что именно мне написать?")

    print(f"Печатаю: {argument} через 2 секунды... Приготовьтесь!")
    time.sleep(2)
    pyautogui.write(argument, interval=0.1)
    print("Готово!") 
    
    
def stop():
    print("Останавливаю программу")
    exit()