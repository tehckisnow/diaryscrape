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

def getEp(number):
  #find download url
  mainUrl = 'https://darknetdiaries.com/episode/'
  number = number
  siteUrl = mainUrl + str(number)

  #get html
  script = HTMLSession().get(siteUrl).html.find('script')

  theText = script[0].text.split('window.playerConfiguration = ')
  final = theText[1]
  ob = json.loads(str(final))

  name = ob["episode"]["title"]
  dlUrl = ob["episode"]["media"]["mp3"]
  print(name + dlUrl)

  #download
  urllib.request.urlretrieve(dlUrl, './' + str(number) + ' - ' + name + '.mp3')

def getAll():
  i = 1
  while i <= maxEp:
    getEp(i)
    i += 1


#getEp(1)
getAll()
