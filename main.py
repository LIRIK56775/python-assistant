from operator import index
from aliases import aliases
import webbrowser
import os
from actions import commands

history = []

last_cannonical = None
last_argument = None

while True:
    command = input("Что открыть ")
    
    command = command.strip() # удаляем пробелы в начале и конце строки

    command = command.lower() # приводим все команды к одному регистру
    
    canonical = None
    
    for key in aliases:
        for alias in aliases[key]:
            if alias in command:
                canonical = key
                break
        if canonical is not None:
            break
    
    if canonical == "повтори":
        if last_cannonical is not None and last_argument is not None:
            commands[last_cannonical](last_argument)
        else:
            print("Нет команды для повторения")
            
    elif canonical == "история":
        if len(history) == 0:
            print("История команд пуста")
        else:
            print("История команд:")
            index = 1
            for item in history:
                cmd = item[0]
                arg = item[1]
                print(f"{index}. {cmd} {arg}")
                index += 1
                
    elif canonical is not None:
        words = command.split()
        stop_words = ["открой", "открыть", "запусти", "запустить", "покажи", "показать", "найди", "найти", "найду", "найди мне", "найди мне", canonical,"история"]
        filtered = []
        for word in words:
            if word not in stop_words:
                filtered.append(word)
                
        argument = " ".join(filtered)
        
        commands[canonical](argument)
        last_cannonical = canonical
        last_argument = argument
        history.append((canonical, argument))
        
        
    else:
        print("Команда не распознана")