import webbrowser
import os
import pathlib
import subprocess

def search(argument):
    if argument == "":
        print("Пожалуйста, укажите, что вы хотите найти")
        return
    
    url = "https://www.google.com/search?q=" + argument.replace(" ", "+")
    webbrowser.open(url)
    print(f"Ищу {argument} в интернете")

def browser(argument):
    os.startfile("msedge.exe")        
    print("Открываю браузер")

def site(argument):
    argument = argument.lower().strip()
            
    if argument == "":
        webbrowser.open("https://www.google.com/")
        print("Открываю сайт по умолчанию (Google)")
        return
        
    elif argument == "ютуб":
        webbrowser.open("https://www.youtube.com/")
        print(f"Открываю сайт {argument}")
    
    elif argument == "гугл":
        webbrowser.open("https://www.google.com/")
        print(f"Открываю сайт {argument}")
        
    elif argument == "гитхаб":
        webbrowser.open("https://www.github.com/")
        print(f"Открываю сайт {argument}")
        
    else:
        # универсальный fallback
        url = f"https://{argument}.com"
        webbrowser.open(url)
        print(f"Открываю сайт {argument}")        
    
def notepad(argument):
    os.startfile("notepad.exe")
    print("Открываю блокнот")
    
def folder(argument):
    if argument == "":
        path = os.path.expanduser("~/Desktop")
        os.startfile(path)
        return
    
    folders = {
        "загрузки": os.path.expanduser("~/Downloads"), 
        "рабочий стол": os.path.expanduser("~/Desktop"),
        "документы": os.path.expanduser("~/Documents"),
    }
    
    argument = argument.lower().strip()
    
    if argument in folders:
        os.startfile(folders[argument])
    else:
        print(f"Папка {argument} не найдена")
    
def stop():
    print("Останавливаю программу")
    exit()