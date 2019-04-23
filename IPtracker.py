# -*- coding:utf-8 -*-



# Importation of useful libraries (not for colorama but green and red look h4x0r in a script :spy:)

import os, requests, json
from colorama import init, Fore, Back, Style

init()


# Many functions, feel free to look at


def start():

	print(Fore.GREEN + "A simply IP-TRACKER using the ip-api.com API.")
	print("By Crystal/Pearl\n\n")



def clear():

	if os.name == "nt": # If the OS is windows, return cls in the cmd
		return os.system("cls")
	else:				# If the os isn't windows (maybe a linux distro or mac), return clear in the terminal
		return os.system("clear")


def tracking():

	IP = input(Fore.RED + "Enter the IP (or url) to track : ")
	r = requests.get("http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,query".format(IP))
	result = json.loads(r.text)

	if result["status"] == "fail":
		print("The IP/URL is invalid.")
	else:
		clear()
		print("""Target : {ip}

Country : {country}
Country Code : {country_code}
Region : {region}
City : {city}
ZIP : {zip}
Timezone : {timezone}
ISP : {isp}
Reverse DNS : {reverse}
Proxy : {proxy}
IP used for the query : {query}

""".format(ip=IP, country=result["country"], country_code=result["countryCode"], region=result["region"], city=result["city"], zip=result["zip"], timezone=result["timezone"], isp=result["isp"], reverse=result["reverse"], proxy=result["proxy"], query=result["query"]))



clear()
start()
tracking()

over = False


while(not over):
	response = input("Do you want to track another IP/URL ? (Y/N) : ")

	if response.lower() == "n":
		clear()
		print(Fore.GREEN + "Thanks you for using this tool !\n")
		over = True
	else:
		print("\n")
		tracking()




# Seems you had read my code, that's cool, hope you had learn something :smiley:
# By xPearl.