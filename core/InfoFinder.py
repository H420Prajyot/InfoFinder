# -*- coding: utf-8 -*-

__version__ = 6.0

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style

init()
warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Please run python version 3.")

checkVersion()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def loadlib():

	import requests, json

	import datetime

	# fonction
	from core.bssidFinder import bssidFinder
	from core.employee_lookup import employee_lookup
	from core.google import google
	from core.hashDecrypt import hashdecrypt
	from core.ipFinder import ipFinder
	from core.mailToIP import mailToIP
	from core.profilerFunc import profilerFunc
	from core.searchAdresse import searchAdresse
	from core.searchTwitter import searchTwitter
	from core.searchPersonne import searchPersonne
	from core.searchInstagram import searchInstagram
	from core.searchUserName import searchUserName
	from core.searchNumber import searchNumber
	from core.searchEmail import SearchEmail
	from core.Profiler import Profiler
	from core.facebookStalk import facebookStalk

	global monip, monpays, codemonpays, pathDatabase
	global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
	global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
	global Profiler


	monip = requests.get("https://api.ipify.org/").text

	monpays = requests.get("http://ip-api.com/json/"+monip).text
	value = json.loads(monpays)
	monpays = value['country']
	codemonpays = value['countryCode']

	pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
	pathDatabase = "\\".join(pathDatabase)+"\\Watched"

	if not os.path.exists(pathDatabase):
		os.mkdir(pathDatabase)

def loadingHack(importlib):
	chaine = "[*]"+' Start InfoFinder...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			time.sleep(0.06)

def loadingUpper(importlib):

	string = "Start InfoFinder"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			sys.stdout.write("\r[*] "+''.join(string) +'...')
			time.sleep(0.1)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1

def loadingTextPrint(importlib):
	string = "Start InfoFinder"

	while importlib.is_alive():

		space = " " * 100
		sys.stdout.write("\r"+space)
		
		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@InfoFinder:~$ "+string[:x]+"|")
			time.sleep(float(times))
			x += 1

def thread_loading():

	num = random.choice([1, 2, 3])

	importlib = threading.Thread(target=loadlib)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	elif num == 3:
		load = threading.Thread(target=loadingTextPrint(importlib))

	load.start()
	importlib.join()
	load.join()

thread_loading()

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)


from datetime import date
today_date = date.today()

header1 = """

 _  _      _____ ____        _____ _  _      ____  _____ ____ 
/ \/ \  /|/    //  _ \      /    // \/ \  /|/  _ \/  __//  __\
| || |\ |||  __\| / \|_____ |  __\| || |\ ||| | \||  \  |  \/|
| || | \||| |   | \_/|\____\| |   | || | \||| |_/||  /_ |    /
\_/\_/  \|\_/   \____/      \_/   \_/\_/  \|\____/\____\\_/\_\
                                                              
"""

header2 = """
  _____ _   _ ______ ____         ______ _____ _   _ _____  ______ _____  
 |_   _| \ | |  ____/ __ \       |  ____|_   _| \ | |  __ \|  ____|  __ \ 
   | | |  \| | |__ | |  | |______| |__    | | |  \| | |  | | |__  | |__) |
   | | | . ` |  __|| |  | |______|  __|   | | | . ` | |  | |  __| |  _  / 
  _| |_| |\  | |   | |__| |      | |     _| |_| |\  | |__| | |____| | \ \ 
 |_____|_| \_|_|    \____/       |_|    |_____|_| \_|_____/|______|_|  \_\
                                                                          
"""

header5 = """

 ____  ____   _____   ___          _____  ____  ____   ___      ___  ____  
|    ||    \ |     | /   \        |     ||    ||    \ |   \    /  _]|    \ 
 |  | |  _  ||   __||     | _____ |   __| |  | |  _  ||    \  /  [_ |  D  )
 |  | |  |  ||  |_  |  O  ||     ||  |_   |  | |  |  ||  D  ||    _]|    / 
 |  | |  |  ||   _] |     ||_____||   _]  |  | |  |  ||     ||   [_ |    \ 
 |  | |  |  ||  |   |     |       |  |    |  | |  |  ||     ||     ||  .  \
|____||__|__||__|    \___/        |__|   |____||__|__||_____||_____||__|\_|
                                                                           
"""

header6 = """

 _____ _   _ ______ _____       ______ _____ _   _______ ___________ 
|_   _| \ | ||  ___|  _  |      |  ___|_   _| \ | |  _  \  ___| ___ \
  | | |  \| || |_  | | | |______| |_    | | |  \| | | | | |__ | |_/ /
  | | | . ` ||  _| | | | |______|  _|   | | | . ` | | | |  __||    / 
 _| |_| |\  || |   \ \_/ /      | |    _| |_| |\  | |/ /| |___| |\ \ 
 \___/\_| \_/\_|    \___/       \_|    \___/\_| \_/___/ \____/\_| \_|
                                                                     
                                                                     

"""

header7 = """

_________ _        _______  _______         _______ _________ _        ______   _______  _______ 
\__   __/( (    /|(  ____ \(  ___  )       (  ____ \\__   __/( (    /|(  __  \ (  ____ \(  ____ )
   ) (   |  \  ( || (    \/| (   ) |       | (    \/   ) (   |  \  ( || (  \  )| (    \/| (    )|
   | |   |   \ | || (__    | |   | | _____ | (__       | |   |   \ | || |   ) || (__    | (____)|
   | |   | (\ \) ||  __)   | |   | |(_____)|  __)      | |   | (\ \) || |   | ||  __)   |     __)
   | |   | | \   || (      | |   | |       | (         | |   | | \   || |   ) || (      | (\ (   
___) (___| )  \  || )      | (___) |       | )      ___) (___| )  \  || (__/  )| (____/\| ) \ \__
\_______/|/    )_)|/       (_______)       |/       \_______/|/    )_)(______/ (_______/|/   \__/
                                                                                                 

"""

header8 = """

 (        )  (        )       (     (        )  (           (     
 )\ )  ( /(  )\ )  ( /(       )\ )  )\ )  ( /(  )\ )        )\ )  
(()/(  )\())(()/(  )\())     (()/( (()/(  )\())(()/(   (   (()/(  
 /(_))((_)\  /(_))((_)\  ___  /(_)) /(_))((_)\  /(_))  )\   /(_)) 
(_))   _((_)(_))_|  ((_)|___|(_))_|(_))   _((_)(_))_  ((_) (_))   
|_ _| | \| || |_   / _ \     | |_  |_ _| | \| | |   \ | __|| _ \  
 | |  | .` || __| | (_) |    | __|  | |  | .` | | |) || _| |   /  
|___| |_|\_||_|    \___/     |_|   |___| |_|\_| |___/ |___||_|_\  
                                                                  

"""

header9 = """

 (       ) (       )     (    (       ) (         (     
 )\ ) ( /( )\ ) ( /(     )\ ) )\ ) ( /( )\ )      )\ )  
(()/( )\()|()/( )\())   (()/((()/( )\()|()/(  (  (()/(  
 /(_)|(_)\ /(_)|(_)\ ___ /(_))/(_)|(_)\ /(_)) )\  /(_)) 
(_))  _((_|_))_| ((_)___(_))_(_))  _((_|_))_ ((_)(_))   
|_ _|| \| | |_  / _ \   | |_ |_ _|| \| ||   \| __| _ \  
 | | | .` | __|| (_) |  | __| | | | .` || |) | _||   /  
|___||_|\_|_|   \___/   |_|  |___||_|\_||___/|___|_|_\  
                                                        

"""

header11 = """

  _____    __  ___  ___        ________    __  ___  __  __  
  \_   \/\ \ \/ __\/___\      / __\_   \/\ \ \/   \/__\/__\ 
   / /\/  \/ / _\ //  //____ / _\  / /\/  \/ / /\ /_\ / \// 
/\/ /_/ /\  / /  / \_//_____/ / /\/ /_/ /\  / /_///__/ _  \ 
\____/\_\ \/\/   \___/      \/  \____/\_\ \/___,'\__/\/ \_/ 
                                                            

"""

header12 = """

    _____   ____________        ___________   ______  __________ 
   /  _/ | / / ____/ __ \      / ____/  _/ | / / __ \/ ____/ __ \
   / //  |/ / /_  / / / /_____/ /_   / //  |/ / / / / __/ / /_/ /
 _/ // /|  / __/ / /_/ /_____/ __/ _/ // /|  / /_/ / /___/ _, _/ 
/___/_/ |_/_/    \____/     /_/   /___/_/ |_/_____/_____/_/ |_|  
                                                                 


                 \\\\
                  \\\\_   \\\\
                   (')   \\\\_
   INFO-FINDER -> / )=.---(') <- Privacy
                o( )o( )_-\_
"""

header13 = """

██ ███    ██ ███████  ██████        ███████ ██ ███    ██ ██████  ███████ ██████  
██ ████   ██ ██      ██    ██       ██      ██ ████   ██ ██   ██ ██      ██   ██ 
██ ██ ██  ██ █████   ██    ██ █████ █████   ██ ██ ██  ██ ██   ██ █████   ██████  
██ ██  ██ ██ ██      ██    ██       ██      ██ ██  ██ ██ ██   ██ ██      ██   ██ 
██ ██   ████ ██       ██████        ██      ██ ██   ████ ██████  ███████ ██   ██ 
                                                                                 
                                                                                 

"""

header14 = """
██╗███╗   ██╗███████╗ ██████╗       ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██║████╗  ██║██╔════╝██╔═══██╗      ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║██╔██╗ ██║█████╗  ██║   ██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║██║ ╚████║██║     ╚██████╔╝      ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝       ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                 
"""

header15 = """

   _   _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( I | N | F | O | - | F | I | N | D | E | R )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

"""

header16 = """

  ___ _   _ _____ ___        _____ ___ _   _ ____  _____ ____  
 |_ _| \ | |  ___/ _ \      |  ___|_ _| \ | |  _ \| ____|  _ \ 
  | ||  \| | |_ | | | |_____| |_   | ||  \| | | | |  _| | |_) |
  | || |\  |  _|| |_| |_____|  _|  | || |\  | |_| | |___|  _ < 
 |___|_| \_|_|   \___/      |_|   |___|_| \_|____/|_____|_| \_\
                                                               

"""

header17 = """

 _ _, _ __,  _,    __, _ _, _ __, __, __,
 | |\ | |_  / \    |_  | |\ | | \ |_  |_)
 | | \| |   \ / ~~ |   | | \| |_/ |   | \
 ~ ~  ~ ~    ~     ~   ~ ~  ~ ~   ~~~ ~ ~
                                         

"""

header18 = """

 _  _   _  ___    _____          ___    _  _   _  ___    ___    ___   
(_)( ) ( )(  _`\ (  _  )        (  _`\ (_)( ) ( )(  _`\ (  _`\ |  _`\ 
| || `\| || (_(_)| ( ) | ______ | (_(_)| || `\| || | ) || (_(_)| (_) )
| || , ` ||  _)  | | | |(______)|  _)  | || , ` || | | )|  _)_ | ,  / 
| || |`\ || |    | (_) |        | |    | || |`\ || |_) || (_( )| |\ \ 
(_)(_) (_)(_)    (_____)        (_)    (_)(_) (_)(____/'(____/'(_) (_)
                                                                      
                                                                      

"""

def lb_header():

    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))

helpMain = """
 Name                       Action
 ----                       ------
 Lookup                     Do some research on a person. 
 Other Tool                 Use tools other than recognition.
 Make file                  Create a '.txt' file to write the information obtained.
 Show Database              Access the database.

 Exit                       Exit the software.
 Help                       Displays this message.
 Clear                      Clear the screen."""

helpLookup = """
 Name                             Action
 ----                             ------
 Personne lookup                  Do research with a name, first name and (city).
 Username lookup                  Do research with a pseudonym. 
 Adresse lookup                   Do research with an address.
 Phone lookup                     Do some research with a phone number.
 IP lookup                        Do research with an IP address.
 SSID locator                     Searching with a MAC / BSSID address.
 Email lookup                     Do research with an email address.
 Mail tracer                      Do research with the header of an email.
 Employees search                 Finds the employees of a company.
 Google search                    Do some research on google.
 Facebook graphSearch             Do research using graphSearch.
 twitter info                     Retrieve information from a Twitter account.
 instagram info                   Retrieve Instagram Account Information.

 Back main menu                   Return to the main menu.
 Exit script                      To quit the software.
 Clear screen                     Clear the screen."""

helpOtherTool = """
  Name                             Action
 ----                             ------
 Hash decrypter                   Try to decrypt a hash through an online database.

 Back main menu                   Return to the main menu.
 Exit script                      To quit the software.
 Clear screen                     Clear the screen."""

helpProfiler = """
 Name                      Action
 ----                      ------
 Search Profiles           Search for a profile in the database.
 Show all Profiles         Displays all the profiles in the database.

 Exit Database             Exit the database to return to the main menu.
 Help message              Message displays
"""

helpCountry = """
 Name                      Action
 ----                      ------
 FR                        Use French services.
 BE                        Use Belgian services.
 CH                        Use Swiss services.
 EN                        Use English services.
 All                       Use all the services.

 Back main menu            Return to the main menu.
 Exit script               To quit the software.
 Clear screen              Clear the screen."""

mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country

 [e] Exit script    [h] Help Message    [c] Clear Screen"""

text = ['Press F to hack', 'LEAVE ME HERE', 'The security is an illusion.', 'Profiler ctOS v2.0', 'DedSec takeover', 'Fsociety00.dat', 'Evil Corp',
 'Hello, friend', 'Hacking is our weapon', 'Hello, World', 'Login the world...', 'Big Brother is watching you.', 'Fuck Society', 'Wrench is calling...',
 'The control is an illusion.', 'install google_crack.exe...', 'you are free ! lol no, it was a joke.', 'you are a 1 or a 0 ?', 'Matraque: 1 - Genou: 0', 'Je veux que tu comprenne... Que tu ne sera plus jamais libre..', 'Tu pense être intouchable... Je vais briser tes illusion...',
 'je veux que tu sache... que tu n\'es plus anonyme...', 'Snapchat: T-Bone sent you a new message.', 'LulzSec <3 <3', '<3 Kraken Security OS is bae <3', 'DedSec is now in LinkedIn !',
 'FRANCE World champion 2018 !!', '~~(8:> is Defalt ~~(8:>', 'Facebook: Neo in a relationship with Elliot Alderson.', 'Just.. fuck the society.', 'locating 127.0.0.1 ... No match found', 
 '101100100101100 01100110010110011001', '101100 0110011001', 'c2V5cHRvbyBteSBsb3Zl', '1 item in your web hisotry: \'Fkk cuckold how to make your wife a hotwife zootube\'', '49 20 4c 4f 56 45 20 55', 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6VUS3OKVZGQYSLJQ3GO===', 'Regarde derrière toi...',
 'dW4gZCdldXggdHJvdWUgw6AgcXUnYSB0J3JlIHNlaW4gcXVlIHNpIGNlIGNldHRl', 'Send me nudes: Harry.Truman@nsa.gov', "Access point 'AP-Zone51' was found nearby."]

lookupOption = """
 [1] Personne lookup          [8] Mail tracer                     
 [2] Username lookup          [9] Employees research
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch          
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup             

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

otherToolOption = """
 [1] Hash decrypter

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen 
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles   
 [3] Create profile

 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg) 
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)

 [e] back main menu   [c] Clear screen   [h] Help message
"""

def menu():

	pr = Profiler()
	pr.loadDatabase(pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
                         __..--.._ 
  .....              .--~  .....  `.         Time:      [ %s | %s ]
.":    "`-..  .    .' ..-'"    :". `         Author:    [ H420Prajyot ]      
` `._ ` _.'`"(     `-"'`._ ' _.' '           Version:   [ %s ]              
     ~~~      `.          ~~~                Pays:      [ %s | %s ]
              .'                             Database:  [ %s | %s Ko ]  
             /                             
            (                             %s
             ^---'                                                                                  
	""" % (Fore.YELLOW+str(today_date)+Fore.RESET, Fore.YELLOW+times()+Fore.RESET, 
		   Fore.YELLOW+str(__version__)+Fore.RESET, 
		   Fore.CYAN+monpays+Fore.RESET, codemonpays,
		   Fore.GREEN+str(nbProfilesBDD)+Fore.RESET, Fore.RED+str(sizeOfDB)+Fore.RESET,
		   random.choice(text)
		  )
	
	print(lb_header())
	print(menu)

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n InfoFinder("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
	
		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = Profiler()
				pr.loadDatabase(pathDatabase)
				database = pr.database
				
				choix = input("\n InfoFinder("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpMsg)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					profile = input(" Profil: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=pathDatabase)
					
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Firstname name)"+Fore.RESET)
					name = input(" Profile Name: ")
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					twitter = input(" Twitter: ")
					# print(found+" %s" % (twitter))
					instagram = input(" Instagram: ")
					# print(found+" %s" % (instagram))
					facebook = input(" Facebook: ")
					# print(found+" %s" % (facebook))

					info = {"URL": {"Twitter": twitter, "Facebook":facebook, "Instagram": instagram}}
					create = pr.writeProfile(fileName=name, path=pathDatabase, info=info)

					if create:
						print("\n"+found+" Profile '%s' has been created successfully." % (name))
					else:
						print("\n"+warning+" An error has occurred. Profile '%s' could not be created." % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n InfoFinder("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber(codemonpays)
				elif lookup.lower() == '7':
					SearchEmail()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse(codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Command not found")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n InfoFinder("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Command not found")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n InfoFinder("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					codemonpays = "FR"
					monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					codemonpays = "BE"
					monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					codemonpays = "CH"
					monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					codemonpays = "EN"
					monpays = "English"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					codemonpays = "XX"
					monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Command not found")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")