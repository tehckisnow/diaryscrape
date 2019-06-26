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
  print("downloading episode: " + str(number))
  
  #find download url
  mainUrl = 'https://darknetdiaries.com/episode/'
  number = number
  siteUrl = mainUrl + str(number)

  #get html
  script = HTMLSession().get(siteUrl).html.find('script')

  #get script element and convert to json
  theText = script[0].text.split('window.playerConfiguration = ')
  final = theText[1]
  ob = json.loads(str(final))

  #get data
  title = str(ob["episode"]["title"])
  name = str(title)
  dlUrl = str(ob["episode"]["media"]["mp3"])
  num = str(number)

  #replace illegal characters
  invalidChars = [":", "/", "\\", "*", "?", "<", ">", "|"] #\
  i = 0
  while i <= len(invalidChars) - 1:
    name = name.replace(invalidChars[i], "-")
    i += 1

  #construct filename
  filename = "./" + num + "- " + name + ".mp3"
  
  #diagnostics
  print("name: " + name)
  print("download url: " + dlUrl)
  print("filename: " + filename)
  
  #download
  if(dl):
    urllib.request.urlretrieve(dlUrl, filename)
    print("episode " + num + " downloaded.")
    print("")

def getAll(dl):
  print("downloading all episodes")
  print("")
  i = 1
  while i <= maxEp:
    getEp(i, dl)
    i += 1
  print("")
  print("downloads complete")


#getEp(1, False)
getAll(True)
