# -*- coding: utf-8 -*-

'''
    Filmnet Add-on (C) 2017
    Credits to Exodus and Covenant; our thanks go to their creators

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
'''

import re,urlparse

from resources.lib.modules import client
from resources.lib.modules import cleantitle
from resources.lib.modules import source_utils

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['putlockerseries.unblocked.vc']
        self.base_link = 'https://putlockerseries.unblocked.vc'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(tvshowtitle).replace('-','_')
            url = urlparse.urljoin(self.base_link, 'episode/%s/' % clean_title)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.urljoin(url, '%s/%s/' % (season, episode))
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []   
            if url is None: return sources
            r = client.request(url)
            links = re.findall('href=&quot;(.+?)&quot;', r)
            for i in links:
                valid, hoster = source_utils.is_host_valid(i, hostDict)
                if valid:
                    sources.append({'source': hoster, 'quality': 'SD', 'language': 'en', 'url': i, 'direct': False, 'debridonly': False})
                else:
                    valid, hoster = source_utils.is_host_valid(i, hostprDict)
                    if not valid: continue
                    sources.append({'source': hoster, 'quality': 'SD', 'language': 'en', 'url': i, 'direct': False, 'debridonly': True})
            return sources
        except:
            return sources

    def resolve(self, url):
        return url