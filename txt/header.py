import random

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
