import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import sfile
dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Removing temp /old files","Please Wait...")
xbmc.sleep(2000)
dp.update(10)

#CACHE
CACHE    = xbmc.translatePath('special://home/cache/')
#THUMBS
thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')

try: sfile.rmtree(CACHE)
except: pass
try: sfile.rmtree(thumbs)
except: pass

origfolder = (xbmc.translatePath("special://home/addons"))      
def CleanPYO():
    count = 0
    for (dirname, dirs, files) in os.walk(origfolder):
       for filename in files:
           if filename.endswith('.pyo') :
               os.remove(os.path.join(dirname, filename))



CleanPYO() 

dp.update(80)
xbmc.sleep(1000)
dp.update(100)
dp.close()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Closing Kodi","Please Wait...")
dp.update(100)
xbmc.sleep(3000)
os._exit(1)





