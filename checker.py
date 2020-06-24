import requests, colorama, concurrent.futures, time
from colorama import Fore
import tkinter as tk
from tkinter import filedialog

live = []

def check(token, timeout):

    headers={
            'Authorization': token
        }

    src = requests.get('https://discordapp.com/api/v6/auth/login', headers = headers, timeout = timeout)
        
    try:
        if src.status_code == 200:
            print(f"{Fore.GREEN}[SUCCESS] {token}")
            live.append(token)
        else:
            print(f"{Fore.RED}[ERROR] {token}")

    except Exception:
        print(f"{Fore.YELLOW}[ERROR] {token}")

def initCheck():

    root = tk.Tk()
    root.withdraw()

    splash = '''
    
  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
 ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
 ██      ███████ █████   ██      █████   █████   ██████  
 ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ Module
                                                        
 '''

    print(splash)
    threads = int(input(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Threads: "))
    timeout = int(input(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Timeout: "))
    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Select Token File: ")

    file = filedialog.askopenfilename()

    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Loaded {Fore.BLUE + file + Fore.WHITE}.")
    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Started Checking.")

    with concurrent.futures.ThreadPoolExecutor(max_workers = threads) as executor:
        with open(file, "r") as file:
            for line in file:
                token = line.strip()
                executor.submit(check, token, timeout)

    print(Fore.RESET + "\n")
    print(" __________________________#RESULTS#__________________________ ")
    print("|                                                             |")
    for _ in live:
        print(f"| {Fore.GREEN + _ + Fore.RESET} |")
    print("|_____________________________________________________________|")
    print("\n")

    if len(live) != 0:
        saveFile = input(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Name of the .txt you want the results saved: ")

        with open(f"./{saveFile}", "w") as File:
            for _ in live:
                File.write(_ + "\n")
            print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Results stored in {Fore.BLUE + saveFile + Fore.WHITE}.")
    
    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Quitting TKNSuite", end = "")
    for _ in range(5):
        print(".", end = "")
        time.sleep(1)
    print("\n")

