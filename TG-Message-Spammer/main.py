import os
import time
import requests
import json
from vardxg import Center, Colors, Write
from colorama import init

logo = ("""
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                Made with <3 by @vardxg

                Press any Key To Start (;

""")
Write.Input(Center.XCenter(logo), Colors.red, interval=0)


bot_token = Write.Input("\n [*] Enter Bot Token >>> ", Colors.red, interval=0)
os.system('cls')

chat_id = Write.Input("\n Chat ID >>> ", Colors.red, interval=0)
os.system('cls')

message = Write.Input("\n Message >>> ", Colors.red, interval=0)
os.system('cls')


class SendMessage():
    def __init__(self) -> None:
        pass

    def telegram_status(text: str) -> None:
        
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

        headers = {
            "connection": "keep-alive",
            "user-agent": "TelegramBot (like TwitterBot);",
            "content-type": "application/json",
        }
        
        response = requests.get(url, headers=headers)

        result = json.loads(response.text)

        status = result['ok']

        return status


while True:
    
    url = "https://api.telegram.org/{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

    headers = {
        "Host": "api.telegram.org",
        "connection": "keep-alive",
        "user-agent": "TelegramBot (like TwitterBot);",
        "accept-encoding": "gzip",
    }

    response = requests.get(url, headers=headers).json()

    for _ in range(5):
        if response["ok"] == True:
            Write.Print(f"\n Message {message} Send!", Colors.green_to_white, interval=0)
        
        elif response["ok"] == False:
            Write.Print(f"\n Message {message} Not Send!", Colors.red_to_white, interval=0)
        
        else:
            Write.Print("\n A error is here idk try again!", Colors.purple, interval=0)
            time.sleep(3)
            exit()

# Made by @vardxg on Telegram!