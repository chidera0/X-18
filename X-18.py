# import pyfiglet module 
import pyfiglet 

from colorama import Fore, init 
import requests
init()
R=pyfiglet.figlet_format("X-18 ",font = "slant")
print(R)
print(f"{Fore.RED}https://web.facebook.com/Alien-god-108932904033061", Fore.RESET)
print(f"{Fore.RED}created by Aliengod16", Fore.RESET)
print(f"{Fore.RED}https://www.youtube.com/channel/UCj9j_SE324s6_Z_CelSe2dQ", Fore.RESET)
# the domain to scan for subdomains
domain = input("[+]enter domain to scan: ")
#open file subdomain
domains = open("subdomain.txt")
# read all the content of the file
contents = domains.read()

new_subdomains = contents.splitlines()

for subdomain in new_subdomains:
    # construct the url from new_subdomains:
    link = f"http://{subdomain}.{domain}"
    try:
       
        requests.get(link)
    except requests.ConnectionError:
        
        pass
    else:
        print(f"{Fore.GREEN}[+]Found subdomain:", link , Fore.RESET)
