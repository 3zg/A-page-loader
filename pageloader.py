import os
import sys
from colorama import Fore
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def write(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.09)

maxrefreshes = 72

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://github.com/3zg")
    print(f"{Fore.CYAN}Loading driver, wait 3 secs {Fore.RESET}")
    write(f"\033[91m{Fore.BLUE}>> By: Goat#8888 - https://github.com/3zg {Fore.RESET}\033[0m")
    sleep(2.5)
    count = 1
    views = True
    amount = input(f"\n{Fore.WHITE}-> How many views: {Fore.RESET}")
    amount = int(amount)
    amount = amount + 1
    if amount < maxrefreshes:
        while views == True:
            now = datetime.now().strftime("%r")
            print(F"{Fore.WHITE}[!] Views: {count}")
            sleep(0.1)
            print(f"{Fore.CYAN}[{now}] {Fore.WHITE}Loaded: {Fore.BLUE}{driver.current_url}{Fore.GREEN} ({count})")
            driver.refresh()
            now2 = datetime.now().strftime("%r")
            print(f"{Fore.CYAN}[{now2}] {Fore.WHITE}Refreshed: {Fore.BLUE}{driver.current_url}{Fore.RESET}\n")
            sleep(0.001)
            count = count + 1
            if count == amount: 
                views = False
        count = count - 1        
        print(f"{Fore.WHITE}Given {Fore.CYAN}{driver.current_url} {Fore.BLUE}{count}{Fore.RESET} views")   
        sleep(2)
        print(f"{Fore.RED}[!] Closing chrome now {Fore.RESET}")
        driver.quit()
        again = input(f"Do you want to get more views? (respond with y or n): ")  
        if again == "y":
            os.system("cls")
            sleep(0.2)
            main()
        elif again == "n":
            write(f"{Fore.RED}>>> Exiting...{Fore.RESET}")
            try:
                driver.quit()
            except:
                pass    
            sys.exit()
        else:
            print(f"{Fore.RED}[!] Invaild repsonse{Fore.RESET}")    
            write(f"{Fore.RED}>>> Exiting...{Fore.RESET}") 
            try:
                driver.quit()
            except:
                pass   
            sys.exit()

    else:
        print(f"{Fore.RED} [!] Your input must not be higher than {maxrefreshes} to avoid github spam detection {Fore.RESET}",end="\r")
        try:
                driver.quit()
        except:
            pass   
        sleep(1.5)
        os.system("cls")
        main()   

main()       
