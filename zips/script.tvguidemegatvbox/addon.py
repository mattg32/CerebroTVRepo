import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]Live TV Menu[/COLOR][/B]', [ 
    '[B]      >> [COLOR=gold]Open Cerebro TV Guide[/COLOR] << [/B]' , 
    '[B]      >> [COLOR=yellow]My TV Guide [/COLOR]<<[/B] (make your own)',
    '[B]      >> [COLOR=gold]Cerebro IPTV[/COLOR] << Live TV (Many Options)[/B]',
    '[B]      >> [COLOR=yellow]Cerebro Media[/COLOR] <<[/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk)')
    
def function2():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk.2017)')
    
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fLive.xml",return)')
    
def function4():
    xbmc.executebuiltin('RunAddon(plugin.video.wargames)')
    
menuoptions()