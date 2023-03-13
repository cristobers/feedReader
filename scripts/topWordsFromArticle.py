# we can append to the database as a space seperated 
# string, after which we can then use .split() to 
# make an array, which can be iterated through 
# within Jinja (within frontend.py)

from collections import Counter
from urllib.request import urlopen 
from bs4 import BeautifulSoup

def getWebpage(url):
    html = urlopen(url, timeout=5)
    bs4 = BeautifulSoup(html.read(), "html.parser")
    return bs4

def getWordsFromWebpage(url):
    text = getWebpage(url).find_all("p")
    a = ''.join([i.get_text() for i in text])
    return a

def getMostFrequentWords(url, count=None) -> str:
    words = getWordsFromWebpage(url).split()
    words = [word for word in words if word[0].isupper() and len(word) > 2 and word not in ("This", "The", "And", "Then", "For", "None")]
    words = Counter(words).most_common()
    
    print(f"Gathering the most frequent words for {url}")

    if count != None:
        return " ".join(list(zip(*words))[0][:count])
    return " ".join(list(zip(*words))[0])