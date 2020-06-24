import colorama
from colorama import Fore
from os import system, name

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

def menu():
    print("\n")
    print(f"{Fore.BLUE}[{Fore.WHITE}~{Fore.BLUE}]{Fore.WHITE} Modules:")
    print(f"{Fore.BLUE}[{Fore.WHITE}1{Fore.BLUE}]{Fore.WHITE} Generator.")
    print(f"{Fore.BLUE}[{Fore.WHITE}2{Fore.BLUE}]{Fore.WHITE} Checker.")
    print("\n")
    module = input(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Select Module: ")

    if module == "1":

        from generator import generate
        generate()
    elif module == "2":

        from checker import initCheck
        initCheck()
    else:
        splash()


def splash():
    clear()
    title = f'''                                                                                                                                                          
 {Fore.BLUE}████████╗██╗  ██╗███╗   ██╗{Fore.WHITE}███████╗██╗   ██╗██╗████████╗███████╗
 {Fore.BLUE}╚══██╔══╝██║ ██╔╝████╗  ██║{Fore.WHITE}██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
    {Fore.BLUE}██║   █████╔╝ ██╔██╗ ██║{Fore.WHITE}███████╗██║   ██║██║   ██║   █████╗  
    {Fore.BLUE}██║   ██╔═██╗ ██║╚██╗██║{Fore.WHITE}╚════██║██║   ██║██║   ██║   ██╔══╝  
    {Fore.BLUE}██║   ██║  ██╗██║ ╚████║{Fore.WHITE}███████║╚██████╔╝██║   ██║   ███████╗
    {Fore.BLUE}╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝{Fore.WHITE}╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
                                                                
                    {Fore.WHITE}Made by sidi {Fore.BLUE}| {Fore.WHITE}Version {Fore.BLUE}1.0{Fore.WHITE}'''
    print(title)
    menu()

splash()