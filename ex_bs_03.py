import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

line = int(input("Enter line to be used: ")) - 1 # enter line to use
x = int(input("Enter number of times to repeat: ")) - 1 # enter how many repeats
repeat = 0
url = "http://py4e-data.dr-chuck.net/known_by_Emme.html" # starting url

while repeat <= x: # repeat this loop for the number of times asked
    print(url)
    html = urllib.request.urlopen(url) # follow the url
    soup = BeautifulSoup(html, 'html.parser') # read and clean url
    tags = soup('a') # list all anchor tags
    #print(url)
    url = tags[line].get('href', None) # pull url from instructed line and set as url
    repeat = repeat + 1 # count the repeats, stop at designated number
print("final", url)
