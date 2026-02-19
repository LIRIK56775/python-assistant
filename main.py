from operator import index
from aliases import aliases
import webbrowser
import os
import brain
import functions
from actions import commands


history = []

last_cannonical = None
last_argument = None

while True:
    user_input = input("Я тебя слушаю: ").strip().lower()
    if "повтори" in user_input:
        if last_cannonical and last_argument:
            cmd, arg = last_cannonical, last_argument
            print(f"Повторяю: {cmd} {arg}")
            commands[cmd](arg)
        else:
            print("Нет команды для повторения.")
        continue
    
    if "история" in user_input:
        if not history:
            print("История команд пуста.")
        else:
            print("История команд:")
            for i, item in enumerate(history, 1): # enumerate — удобный способ сделать индекс
                print(f"{i}. {item[0]} {item[1]}")
        continue
    
    if user_input in ["выход", "пока", "до свидания"]:
        print("До связи!")
        break

    print("Обрабатываю команду...")
    ai_data = brain.process_command(user_input)
    cmd_name = ai_data.get("command")
    argument = ai_data.get("argument", "")
    message = ai_data.get("message", "")
    if message:
        print(f"Джарвис: {message}")
        functions.say(message)
        
    
    if cmd_name in commands:
        report = commands[cmd_name](argument)
        print(f">>> {report}")
        history.append((cmd_name, argument))
        last_cannonical = cmd_name
        last_argument = argument
    elif cmd_name == "none":
        pass