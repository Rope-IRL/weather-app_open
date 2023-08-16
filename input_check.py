import requests
from bs4 import BeautifulSoup

#Send request to Geonames. If the Country, that user typed, was found on the page, it return city, if it's not, return None
def inputCheck(city, country):
    country=country.replace(" ", "+")
    url=f"https://www.geonames.org/search.html?q={city}+{country}&country="
    headers={
        "Accept" : "*/*",
  #You need to add your own user-agent
        "user-agent" : ""
    }

    req=requests.get(url, headers)
    src=req.text
    soup=BeautifulSoup(src,"lxml")
    
    checkCity=soup.find("a", string=f"{city}")

    if checkCity !=None:
        return city
    else:
        return None
