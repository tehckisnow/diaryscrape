import urllib.request
from lxml import html
import requests
from requests_html import HTMLSession
import json

#find download url
#find number
#find name
#set variables
#call download

maxEp = 41

#getEp(episode number, whether or not to download(for testingss))
def getEp(number, dl):
  #find download url
  mainUrl = 'https://darknetdiaries.com/episode/'
  number = number
  siteUrl = mainUrl + str(number)

  #get html
  script = HTMLSession().get(siteUrl).html.find('script')

  theText = script[0].text.split('window.playerConfiguration = ')
  final = theText[1]
  ob = json.loads(str(final))

  title = str(ob["episode"]["title"])
  name = str(title)
  dlUrl = str(ob["episode"]["media"]["mp3"])
  num = str(number)
  filename = "./" + num + "- " + name + ".mp3"
  print(name + " " + dlUrl)
  print(filename)
  
  #download
  if(dl):
    urllib.request.urlretrieve(dlUrl, filename)
    #urllib.request.urlretrieve(dlUrl, './filename.mp3') #<--this works perfectly?!?

def getAll(dl):
  i = 1
  while i <= maxEp:
    getEp(i, dl)
    i += 1


getEp(1, True)
#getAll(False)

#urllib.request.urlretrieve('http://traffic.megaphone.fm/ADV3675761065.mp3', './file.mp3')