import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin

def CATEGORIES():
   addDir3('Malaysia','https://raw.githubusercontent.com/kingyanmedia/kodi/master/my.txt',2,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/my.jpg','','')
   addDir3('Singapore','https://raw.githubusercontent.com/kingyanmedia/kodi/master/sg.txt',3,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/Sg.png','','')
   addDir3('Korea','https://raw.githubusercontent.com/kingyanmedia/kodi/master/korean.txt',4,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/Korea.png','','')
   addDir3('China','https://raw.githubusercontent.com/kingyanmedia/kodi/master/china.txt',5,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/China.png','','')
   addDir3('HongKong','https://raw.githubusercontent.com/kingyanmedia/kodi/master/hk.txt',6,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/hk.png','','')
   addDir3('Taiwan','https://raw.githubusercontent.com/kingyanmedia/kodi/master/tw.txt',7,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/taiwan.png','','')
   addDir3('Indonesia','https://raw.githubusercontent.com/kingyanmedia/kodi/master/indo.txt',8,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/indo.png','','')
   addDir3('Japan','https://raw.githubusercontent.com/kingyanmedia/kodi/master/japan.txt',9,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/Japan.png','','')
   addDir3('News','https://raw.githubusercontent.com/kingyanmedia/kodi/master/news.txt',10,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/news1.png','','')
   addDir3('Sports','https://raw.githubusercontent.com/kingyanmedia/kodi/master/sports.txt',11,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/sports.png','','')
   addDir3('Movies','https://raw.githubusercontent.com/kingyanmedia/kodi/master/movie.txt',12,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/movie.png','','')
   addDir3('Learning','https://raw.githubusercontent.com/kingyanmedia/kodi/master/learning.txt',13,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/learning.png','','')
   addDir3('Cartoons','https://raw.githubusercontent.com/kingyanmedia/kodi/master/cartoon.txt',14,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/Cartoon.png','','')
   addDir3('Hindi','https://raw.githubusercontent.com/kingyanmedia/kodi/master/hindi.txt',15,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/hindi.png','','')
   addDir3('MTV','https://raw.githubusercontent.com/kingyanmedia/kodi/master/mtv.txt',16,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/mtv.png','','')
   addDir3('Cinema','https://raw.githubusercontent.com/kingyanmedia/kodi/master/cinema.txt',17,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/cinema.jpg','','')
   addDir3('BESTTV','https://raw.githubusercontent.com/kingyanmedia/kodi/master/besttv.txt',18,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/besttv.jpg','','')
   addDir3('NEWSTV','https://raw.githubusercontent.com/kingyanmedia/kodi/master/newtv.txt',19,'https://raw.githubusercontent.com/kingyanmedia/kodi/master/logo/newstv.jpg','','')
 

def Malaysia():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/my.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Singapore():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/sg.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def Korea():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/korean.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def China():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/china.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def HongKong():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/hk.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Taiwan():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/tw.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Indonesia():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/indo.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Japan():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/japan.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def News():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/news.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Sports():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/sports.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Movies():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/movie.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Learning():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/learning.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Cartoons():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/cartoon.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Hindi():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/hindi.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def MTV():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/mtv.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Cinema():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/cinema.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def BESTTV():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/besttv.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def NEWSTV():
   r = requests.get('https://raw.githubusercontent.com/kingyanmedia/kodi/master/newtv.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
	 
def addLink(name,url,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#################################################################################################################

#                               NEED BELOW CHANGED

  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
     
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
elif mode==2:
        Malaysia()
elif mode==3:
        Singapore()
elif mode==4:
        Korea()
elif mode==5:
        China()
elif mode==6:
        HongKong()
elif mode==7:
        Taiwan()
elif mode==8:
        Indonesia()
elif mode==9:
        Japan()
elif mode==10:
        News()
elif mode==11:
        Sports()
elif mode==12:
        Movies()
elif mode==13:
        Learning()
elif mode==14:
        Cartoons()
elif mode==15:
        Hindi()
elif mode==16:
        MTV()
elif mode==17:
        Cinema()
elif mode==18:
        BESTTV()
elif mode==19:
        NEWSTV()

        


xbmcplugin.endOfDirectory(int(sys.argv[1]))
