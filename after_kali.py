import os
import sys

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white

def AutoPrint(AP):
    print(f'''
============================================================
| -> {AP}
============================================================
	''')


def AutoRun(AR):
    os.system(AR)

def result(update,
upgrade,
git_gcc,
Python,
Go,
Alacarte,
Docker,
Sublist3r,
Amass,
Asset_Finder,
Sub_Finder,
Mas_Scan,
gobuster,
dirsearch,
wfuzz,
ffuf,
arjun,
ParamSpider,
httprobe,
sublime):

    print(f'Update ........................ {update}')
    print(f'Upgrade ....................... {upgrade}')
    print(f'git & gcc...................... {git_gcc}')
    print(f'Python ........................ {Python}')
    print(f'Go ............................ {Go}')
    print(f'Alacarte ...................... {Alacarte}')
    print(f'Docker ........................ {Docker}')
    print(f'Sublist3r ..................... {Sublist3r}')
    print(f'Amass ......................... {Amass}')
    print(f'Asset_Finder .................. {Asset_Finder}')
    print(f'Sub_Finder .................... {Sub_Finder}')
    print(f'Mas_Scan ...................... {Mas_Scan}')
    print(f'gobuster ...................... {gobuster}')
    print(f'dirsearch ..................... {dirsearch}')
    print(f'wfuzz ......................... {wfuzz}')
    print(f'ffuf .......................... {ffuf}')
    print(f'arjun ......................... {arjun}')
    print(f'ParamSpider ................... {ParamSpider}')
    print(f'httprobe ...................... {httprobe}')
    print(f'sublime ....................... {sublime}')


print(f'''{Y}
   db    888888 888888 888888 88""Yb     88  dP    db    88     88 
  dPYb   88__     88   88__   88__dP     88odP    dPYb   88     88 
 dP__Yb  88""     88   88""   88"Yb      88"Yb   dP__Yb  88  .o 88 
dP""""Yb 88       88   888888 88  Yb     88  Yb dP""""Yb 88ood8 88 
[*] welcome to After Kali (1.1) | by Abdelrahman Nasr
''')


ans = input(f'{Y} Do you want to start downloading? (y/n): ')

if ans == 'y':
    try:
        AutoPrint('update')
        AutoRun('apt-get -y update')
        update = 'Done (1/1)'
    except:
        update = 'Error'

    try:
        AutoPrint('upgrade')
        AutoRun('apt-get -y upgrade')
        upgrade = 'Done (1/1)'
    except:
        upgrade = 'Error'

    try:
        AutoPrint('install git & gcc')
        AutoRun('sudo apt-get --assume-yes install git make gcc')
        git_gcc = 'Done (1/1)'
    except:
        git_gcc = 'Error'

    try:
        AutoPrint('install Python3 & pip3 & virtualenv')
        AutoRun('apt-get install -y python3')
        try:
            AutoRun('apt install -y python3-pip')
            try:
                AutoRun('pip3 install virtualenv ')
		try:
		    AutoRun('sudo apt remove python-is-python2')
		    try:
		        AutoRun('sudo apt install -y python-is-python3')
                        Python = 'Done (5/5)'			
		    except:
			Python = 'Done (4/5)'
		except:
		   Python = 'Done (3/5)'
            except:
                Python = 'Done (2/5)'
        except:
            Python = 'Done (1/5)'
    except:
        Python = 'Error'

    try:
        AutoPrint('install Go Lang')
        AutoRun('sudo apt install -y gccgo-go')
        try:
            AutoRun('sudo apt install -y golang-go')
            Go = 'Done (2/2)'
        except:
            Go = 'Done (1/2)'
    except:
        Go = 'Error'

    try:
        AutoPrint('install Alacarte')
        AutoRun('apt install -y alacarte')
        Alacarte = 'Done (1/1)'
    except:
        Alacarte = 'Error'

    try:
        AutoPrint('install Docker')
        AutoRun('apt install -y docker.io')
        Docker = 'Done (1/1)'
    except:
        Docker = 'Error'

    try:
        AutoPrint('install Sublist3r')
        AutoRun('git clone https://github.com/aboul3la/Sublist3r.git')
        try:
            AutoRun('pip install -r Sublist3r/requirements.txt')
            try:
                AutoRun('python3 Sublist3r/setup.py build')
                try:
                    AutoRun('python3 Sublist3r/setup.py install')
                    Sublist3r = 'Done (4/4)'
                except:
                    Sublist3r = 'Done (3/4)'
            except:
                Sublist3r = 'Done (2/4)'
        except:
            Sublist3r = 'Done (1/4)'
    except:
        Sublist3r = 'Error'

    try:
        AutoPrint('install Amass')
        AutoRun('apt-get -y install amass')
        Amass = 'Done (1/1)'
    except:
        Amass = 'Error'

    try:
        AutoPrint('install Asset Finder')
        AutoRun('apt install -y assetfinder')
        Asset_Finder = 'Done (1/1)'
    except:
        Asset_Finder = 'Error'

    try:
        AutoPrint('install Sub Finder')
        AutoRun('GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder')
        try:
            AutoRun('apt install -y subfinder')
            Sub_Finder = 'Done (2/2)'
        except:
            Sub_Finder = 'Done (1/2)'
    except:
        Sub_Finder = 'Error'
    try:
        AutoPrint('install Mas Scan')
        AutoRun('git clone https://github.com/robertdavidgraham/masscan')
        try:
            AutoRun('cd masscan')
            try:
                AutoRun('make')
                try:
                    AutoRun('make insall')
                    try:
                        AutoRun('cd ..')
                        Mas_Scan = 'Done (5/5)'
                    except:
                        Mas_Scan = 'Done (4/5)'
                except:
                    Mas_Scan = 'Done (3/5)'
            except:
                Mas_Scan = 'Done (2/5)'
        except:
            Mas_Scan = 'Done (1/5)'
    except:
        Mas_Scan = 'Error'

    try:
        AutoPrint('install Go Buster')
        AutoRun('apt-get install -y gobuster')
        gobuster = 'Done (1/1)'
    except:
        gobuster = 'Error'

    try:
        AutoPrint('install Dir Search')
        AutoRun('apt install -y dirsearch')
        dirsearch = 'Done (1/1)'
    except:
        dirsearch = 'Error'

    try:
        AutoPrint('install Wfuzz')
        AutoRun('apt-get install -y wfuzz')
        wfuzz = 'Done (1/1)'
    except:
        wfuzz = 'Error'

    try:
        AutoPrint('install Ffuf')
        AutoRun('apt-get install -y ffuf')
        ffuf = 'Done (1/1)'
    except:
        ffuf = 'Error'

    try:
        AutoPrint('install Arjun')
        AutoRun('git clone https://github.com/s0md3v/Arjun.git')
        try:
            AutoRun('pip3 install arjun')
            try:
                AutoRun('python3 Arjun/setup.py install')
                try:
                    AutoRun('apt-get install -y arjun')
                    arjun = 'Done (4/4)'
                except:
                    arjun = 'Done (3/4)'
            except:
                arjun = 'Done (2/4)'
        except:
            arjun = 'Done (1/4)'
    except:
        arjun = 'Error'

    try:
        AutoPrint('install Param Spider')
        AutoRun('git clone https://github.com/devanshbatham/ParamSpider')
        try:
            AutoRun('pip3 install -r ParamSpider/requirements.txt')
            ParamSpider = 'Done (2/2)'
        except:
            ParamSpider = 'Done (1/2)'
    except:
        ParamSpider = 'Error'

    try:
        AutoPrint('install Httprobe')
        AutoRun('apt-get install -y httprobe')
        httprobe = 'Done (1/1)'
    except:
        httprobe = 'Error'

    try:
        AutoPrint('install Sublime')
        AutoRun('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
        try:
            AutoRun('sudo apt-get install apt-transport-https')
            try:
                AutoRun(
                    'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
                try:
                    AutoRun('apt-get -y update')
                    try:
                        AutoRun('apt-get install -y sublime-text')
                        sublime = 'Done (5/5)'
                    except:
                        sublime = 'Done (4/5)'
                except:
                    sublime = 'Done (3/5)'
            except:
                sublime = 'Done (2/5)'
        except:
            sublime = 'Done (1/5)'
    except:
        sublime = 'Error'

    AutoPrint('Installation Results')

    result(update,
    upgrade,
    git_gcc,
    Python,
    Go,
    Alacarte,
    Docker,
    Sublist3r,
    Amass,
    Asset_Finder,
    Sub_Finder,
    Mas_Scan,
    gobuster,
    dirsearch,
    wfuzz,
    ffuf,
    arjun,
    ParamSpider,
    httprobe,
    sublime)

else:
    sys.exit()
