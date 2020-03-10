# Author: Richard Zins

from bs4 import BeautifulSoup
import requests
import queue 

url = input("Enter the starting website URl: ")
q = queue.Queue()
q.put(url)

while not q.empty() :

    entry = q.get()
    request = requests.get(entry)
    data = request.text
    soup = BeautifulSoup(data, "html.parser")
    #  print(soup.prettify())

    for link in soup.find_all("a") :
        str = link.get("href")

        if "http" in str :
             q.put(str)
             print(str)
        elif str.find("/") != 0 :
             locationOfDotCom = entry.find(".com")
             newEntry = entry[0 : locationOfDotCom + 4]
             str2 = newEntry + "/" +  str
             q.put(str2)
             print(str2)
        else :
             locationOfDotCom = entry.find(".com")
             newEntry = entry[0 : locationOfDotCom + 4]
             str2 = newEntry + str
             q.put(str2)
             print(str2)
