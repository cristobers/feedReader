# we can append to the database as a space seperated 
# string, after which we can then use .split() to 
# make an array, which can be iterated through 
# within Jinja (within frontend.py)

from collections import Counter
from urllib.request import urlopen 
from bs4 import BeautifulSoup

def getWebpage(url):
    html = urlopen(url)
    bs4 = BeautifulSoup(html.read(), "html.parser")
    return bs4

def getWebpageText(url):
    text = getWebpage(url).find_all("p")
    data = "".join([i.get_text() for i in text])
    return data.lower()

def getMostFrequentWords(url, count):
    unwantedWords = ["i","-","the", "and", "a", "is", "they", "i\'m", "them", "he", "him", "she", "her", "you", ")", "(", ",", "for", "my", "are", "though", "that", "also", "using", "an"]
    words = getWebpageText(url).split()
    words = [i for i in words if i not in unwantedWords]
    words = Counter(words).most_common()
    return " ".join(list(zip(*words))[0][:count])