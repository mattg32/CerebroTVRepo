import xbmc
import utils
import os
import xbmcgui
import sfile
import urllib
import urllib2
import time
import re
import downloader
import extractor
import xbmcvfs
import shutil

DoStart = 0
#userid = 0
ipaddy = "0.0.0.0"
dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
    
    
if not ping("google.com"):
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]VistaTV[/COLOR][/B]", "No Internet Connection Found!", "Press OK to exit",'Please Check Your Connection.')
    os._exit(1)
    exit()
    
from uuid import getnode as get_mac
mac = get_mac()
macid = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
#xbmc.log(macid,2)  

def codecheck(userid):
    response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(userid)).read()
    if response == "OK":
        return True
    else:
        return False
      
def checkmac():
    response = urllib2.urlopen('http://vistatv.co.uk/TV-DATA/auth2.php?mac='+macid).read()
    if response == "OK":
        return True
    else:
        return False

def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'
        
myplatform = platform()     

if myplatform == 'android': # Android       
    IDPATH      = '/storage/emulated/0/Download/vistatv/'
elif myplatform == 'windows':   
    IDPATH      = 'C:\\vistatv\\'  
    
else: IDPATH    = xbmc.translatePath('special://home/')


PART1  = "https://github.com/biglad/PersonalDataVistaTV/raw/master/zips/install1.zip"
PART2  = "https://github.com/biglad/PersonalDataVistaTV/raw/master/zips/install2.zip"
PART3  = "https://github.com/biglad/PersonalDataVistaTV/raw/master/zips/install3.zip"
PART4  = "https://github.com/biglad/PersonalDataVistaTV/raw/master/zips/NewUpdate.zip" ## also see UPDATE = 
UPDATE = PART4

USERDATA    = xbmc.translatePath('special://userdata/')
HOME        = xbmc.translatePath('special://home/')
ADDONS      = xbmc.translatePath('special://home/addons')

file1     =  os.path.join(HOME, 'install.zip')
file2     =  os.path.join(HOME, 'install2.zip')
file3     =  os.path.join(HOME, 'install3.zip')
file4     =  os.path.join(HOME, 'install4.zip')
iddata    =  os.path.join(HOME, 'userdata/networksettings.xml')
done      =  os.path.join(HOME, 'done.xml')
idbackup = os.path.join(IDPATH, 'datafile.bin')
#import os.path
#if os.path.exists(done):
#    exit()
dp.create("Staring Vista TV's Wizard","CHECKING FOR CODES",'', ' ')
percent = 99 
dp.update(percent)
SkipCheck = 0
xbmc.sleep(2000)
try:
    with open(iddata, 'r') as myfile:
        data300=str(myfile.read())
except: 
    data300="CODE NOT FOUND CHECKING FOR BACKUP"
dp.create("Staring Vista TV's Wizard","",str(data300), ' ')
xbmc.sleep(5000)
if not checkmac():    
    try:
        with open(idbackup, 'r') as myfile:
            data300=str(myfile.read())
    except: 
        data300="OH DEAR I NEED A NEW CODE!!!!!"
else : data300 = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?idfrommac=yes&mac='+macid).read()
dp.close()
dp.create("Staring Vista TV's Wizard","BACKUP CODE",str(data300), ' ')

xbmc.sleep(5000)
dp.close()
DoStart = 1
SkipCheck = 1
if data300=="CODE NOT FOUND CHECKING FOR BACKUP":
    DoStart = 0
else: SkipCheck = 1

if data300=="OH DEAR I NEED A NEW CODE!!!!!":
    DoStart = 0
else: SkipCheck = 1


def killxbmc():
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)

if not os.path.exists(IDPATH):
    try: os.mkdir(IDPATH)
    except: pass


def install():
    downloader . download(PART1,file1,"Downloading Installer Part 1")
    extractor . extract(file1,HOME,"Unpacking Part 1")
    downloader . download(PART2,file2,"Downloading Installer Part 2")
    extractor . extract(file2,HOME,"Unpacking Part 2")
    downloader . download(PART3,file3,"Downloading Installer Part 3")
    extractor . extract(file3,HOME,"Unpacking Part 3")
    downloader . download(UPDATE,file4,"Downloading Latest Build Info")
    extractor . extract(file4,HOME,"Unpacking Data")
    killxbmc()
    exit()
    
def update():
    downloader . download(UPDATE,file4,"Downloading Latest Build Info")
    extractor . extract(file4,HOME,"Unpacking Data")
    killxbmc()
    exit()
      

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6
        )
        
    call = dialog.select('[B][COLOR=yellow]VistaTV Build Installer[/COLOR][/B]', [ 
    '[B][COLOR=gold]Install for Kodi 17.6[/COLOR][/B]' ,    
    '[B][COLOR=gold]Close Kodi[/COLOR][/B]',
    '[B][COLOR=gold]Exit Wizard[/COLOR][/B]',
    '[B][COLOR=gold]Fresh Install[/COLOR][/B]',
    '[B][COLOR=gold]Remove My Auth Code[/COLOR][/B]',
    '[B][COLOR=gold](re)-Download Last Update[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-6]
        return func()
    else:
        func = funcs[call]
        return func()
    return 
    
def function1():
    function4()
    exit()
    
def function2():
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
    
def function3():
    exit()
    
def function4():

    if not SkipCheck == 1:
        userid = data300
        if codecheck(userid):
            DoStart = 1
        else:
            DoStart = 0
    else: 
        DoStart = 1
        
    if checkmac():
        GetID = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?idfrommac=yes&mac='+macid).read()
        data300 = str(GetID)
        userid = data300
        DoStart = 1
    
    if data300=="CODE NOT FOUND CHECKING FOR BACKUP":
        DoStart = 0
    if data300=="OH DEAR I NEED A NEW CODE!!!!!":
        DoStart = 0
        


    if DoStart ==0:            
        dialog.ok("[COLOR=red][B]VistaTV Auth System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","www.vistatv.uk")
        userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
        if userid =="":
            dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]",".","PLEASE TRY AGAIN")
            xbmc.sleep(15000)
            exit()
            
        response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
        if response == "OK":
            fo = open(iddata, "w")
            fo.write(userid);
            fo.close()
            fo = open(idbackup, "w")
            fo.write(userid);
            fo.close()
            DoStart = 1
        
        
    if DoStart ==0:
        dialog.ok("[COLOR=red][B]VistaTV Auth System[/COLOR][/B]", "Code Not Found", "Please Try Again","For Support www.vistatv.uk")
        #xbmc.executebuiltin('RunAddon(script.vistatv-wizard)')
        exit()
    else:   
        dp.create("Staring Vista TV's Wizard","",'Code Pre Installed', ' ')
        percent = 99
        update = xbmcgui.Dialog().yesno("[COLOR gold]VistaTV[/COLOR]","[COLOR yellow]Due you wish to use current code?[/COLOR]","[COLOR turquoise]"+str(userid)+"[/COLOR]" ,"????")
        if not update:
            dialog.ok("[COLOR=red][B]VistaTV Auth System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","vistatv.co.uk")
            userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
        if userid =="":
            dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]",".","PLEASE TRY AGAIN")
            xbmc.sleep(15000)
            exit()
            
        response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
        if response == "OK":
            fo = open(iddata, "w")
            fo.write(userid);
            fo.close()
            DoStart = 1
            #exit()
        else:
            fo = open(iddata, "w")
            fo.write(userid);
            fo.close()
            fo = open(idbackup, "w")
            fo.write(userid);
            fo.close()
            DoStart = 1
            install()
            #exit()
    addondir= xbmc.translatePath('special://home/addons')
    datadir = xbmc.translatePath('special://userdata/userdata')
    ## todo wipde all addons & user data
    dp.create("Staring Vista TV's Wizard","Removing",'Add-ons', 'Please Wait')
    percent = 05 
    dp.update(percent)
    try: shutil.rmtree(addondir)
    except: pass
    xbmc.sleep(9000)
    percent = 30 
    try: xbmcvfs.rmdir(addondir)
    except: pass
    xbmc.sleep(1000)
    percent = 50 
    dp.update(percent)
    dp.create("Staring Vista TV's Wizard","Removing",'Userdata', 'Please Wait')
    try: shutil.rmtree(datadir)
    except: pass
    xbmc.sleep(9000)
    percent = 68
    try: xbmcvfs.rmdir(datadir)
    except: pass
    xbmc.sleep(1000)
    percent = 83 
    dp.update(percent)
    dp.create("Staring Vista TV's Wizard","Getting Ready",'To Install', 'Please Wait')
    try: xbmcvfs.mkdir(addondir)
    except: pass
    xbmc.sleep(1000)
    try: xbmcvfs.mkdir(datadir)
    except: pass
    xbmc.sleep(1000)
    install()
    exit()
    
def function5():
    dialog.ok("[COLOR=red][B]VistaTV Auth System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","vistatv.co.uk")
    userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
    if userid =="":
        dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]",".","PLEASE TRY AGAIN")
        xbmc.sleep(15000)
        exit()
        
    response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
    if response == "OK":
        fo = open(iddata, "w")
        fo.write(userid);
        fo.close()
        install()
    exit()
    
def function6():
    update()
    exit()
    
if SkipCheck == 1:
    function4()
else:
	if checkmac():
		function4()
	else:
		menuoptions()