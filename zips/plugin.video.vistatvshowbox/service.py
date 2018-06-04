# -*- coding: utf-8 -*-

"""
    VistaTV ShowBox

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sfile
import xbmc
import xbmcgui
from resources.lib.modules import control
control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))


KODIL     = xbmc.translatePath('special://home/addons/repository.kodil')
FREEWORLD = xbmc.translatePath('special://home/addons/repository.free')

if os.path.exists(KODIL):
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]VistaTV[/COLOR][/B]","The [COLOR yellow]Kodil Repo[/COLOR] Is Installed","This MUST BE REMOVED","Press OK to Continue")
    try: sfile.rmtree(KODIL)
    except: pass
    os._exit(1)
	
if os.path.exists(FREEWORLD):
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]VistaTV[/COLOR][/B]","The [COLOR yellow]FreeWold Repo[/COLOR] Is Installed","This MUST BE REMOVED","Press OK to Continue")
    try: sfile.rmtree(FREEWORLD)
    except: pass
    os._exit(1)
