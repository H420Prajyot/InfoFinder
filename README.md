Table of Contents
=

* [InfoFinder](#InfoFinder)
* [Disclaimer] (# Disclaimer)
* [Installation on Linux] (# Installation-on-Linux)
* [Installation on Windows] (# Installation-on-Windows)
* [Contact Me] (# Contact Me)

InfoFinder
=


InfoFinder is an information collection tool (OSINT). It provides various modules that allow efficient searches. InfoFinder does not require an API key or login ID.

<img src= "https://github.com/H420Prajyot/InfoFinder/blob/master/txt/info.png">
	  
Disclaimer
=
InfoFinder was developed to do self-research and to see private and sensitive information that can be left behind on social media. I do not encourage the use of this tool on anyone other than yourself or to misuse this tool. The authors of InfoFinder cannot be responsible for the use of their tool.

Installation On Linux
=
You must have `git` and` python3` to install on your machine
```
    
sudo apt install git python3 # on distributions using APT (like Debian family)
    git clone https://github.com/H420Prajyot/InfoFinder
    cd InfoFinder
    python3 -m pip install -r requirements.txt
```    

Execution Linux
=
In the InfoFinder directory, run this command to be able to launch InfoFinder:
```
python3 InfoFinder.py
```

Installation on Windows
=
- 1. Telecharger [InfoFinder](https://github.com/H420Prajyot/InfoFinder/archive/master.zip)
- 2. Install Python from the Windows Store
- 4. Unzip InfoFinder (master.zip)
- 5. Open `CMD` and go to the **` InfoFinder-master` ** directory using the `cd` command.
     Eg:
```
cd Desktop\
cd InfoFinder-master\
``` 
and run:
```
    python3 -m pip install -r requirements.txt
```

Lancer InfoFinder from Windows:
=
- Go to the ** InfoFinder-master ** directory as it was installed and run the command:
```
python3 InfoFinder.py
```

Discord
=
~~If you have any questions, ideas, issues regarding InfoFinder or just want to follow the progress of this project. ~~
Momentarily closed.

New in version 6.0
=
- Additional (+)
	- A 'requirements.txt' file has been added.
	- A new interface.
	- A new OSINT module has been added. The 'Profiler' module allows you to create a profile and retrieve information on sites defined by the user, save this data and display the last posts published on the networks (filtered according to publication dates).
	- New search services (Directories) have been added depending on the user's location. InfoFinder uses your IP to determine the country you are in. Under no circumstances will your IP or other private information be shared. You can choose a country other than your own to centralize your searches.
	- Instagram and LinkedIn search integrated with 'Person Lookup'
	- A new 'Employees search' module which allows you to find people via a company and a city.
	- Instagram and Facebook information search modules have been improved to extract more information.  

- In less (-)
	- Some python libraries (dnspython, socket and smtplib) have been removed for this version.
	- 'Social engineering tool' has been changed to 'Other tool' it only includes the brute force module of a Hash.
	- The 'Spam Email' and 'SMS' modules have been removed from InfoFinder.


Compatible
=
- Windows
- MacOS
- Linux

Python version:
=
- Python3

Modules Python
=
- requests
- bs4
- terminaltables
- colorama

Features :-
=
 - Lookup:
	- Phone lookup
	- Email lookup
	- Last name / First name lookup
	- Surname lookup
	- Addresse lookup
	- Mail ip locator
	- Ip locator
	- Bssid locator
	- Exif read
	- Google search
	- Twitter
	- Instagram
	- Facebook
	- LinkedIn employee search (New !)
	- Hash Bruteforce (New !)

 - Other tools:

	- Hash Bruteforce

- Profiler (New !)
	- Profiler an profile
	- Database management
	- Profile creator

<b>CONTACT ME :-</b>
H420 :- https://www.facebook.com/prajyot.karkade.7
