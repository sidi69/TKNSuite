import colorama, time
from colorama import Fore
from checker import initCheck

def generate():

    import random, string, os, datetime
    from datetime import date
    
    splash = '''
    
  ██████  ███████ ███    ██ 
 ██       ██      ████   ██ 
 ██   ███ █████   ██ ██  ██ 
 ██    ██ ██      ██  ██ ██ 
  ██████  ███████ ██   ████ Module

    '''

    print(splash)
    print(f"{Fore.BLUE}[{Fore.WHITE}NOTE{Fore.BLUE}]{Fore.WHITE} 1 token loop = 5 Tokens of different types.")
    N = input(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Token Loops: ")
    print("\n")
    
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    date = date.today()
    now = datetime.datetime.now()

    while(int(count) < int(N)):
        firstGen = random.choice(string.ascii_letters).upper() + random.choice(string.ascii_letters).upper() + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(21)) + "." +  random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(27))
        secondGen = "MT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(27))
        thirdGen = "NT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(27))
        fourthGen = "MD" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(27))
        fifthGen = "MT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters  +  string.digits) for _ in range(27))
        
        saveFile = current_path + "/" + str(date) + str(now.minute) + ".txt"
        f = open(saveFile, "a")
        f.write(firstGen + "\n" + secondGen + "\n" + thirdGen + "\n" + fourthGen + "\n" + fifthGen + "\n")
        
        print(firstGen)
        print(secondGen)
        print(thirdGen)
        print(fourthGen)
        print(fifthGen)

        count += 1
    
    print("\n")
    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Tokens saved in {Fore.BLUE + saveFile + Fore.WHITE}.")
    print("\n")
    print(f"{Fore.BLUE}[{Fore.WHITE}!{Fore.BLUE}]{Fore.WHITE} Initializing Checker Module", end = "")
    for _ in range(5):
        print(".", end = "")
        time.sleep(1)

    initCheck()