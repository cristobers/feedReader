# this is just a test for now,
# it may be a good idea to append the top 12 or so words to the database
# so that we're not requesting a new count of words each time
# the websites we're gathering from will thank us :)

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
    gramaticalArticles = ["i","-","the", "and", "a", "is", "they", "i\'m", "them", "he", "him", "she", "her", "you", ")", "(", ",", "for", "my", "are", "though", "that", "also", "using"]
    words = getWebpageText(url).split()
    words = [i for i in words if i not in gramaticalArticles]
    words = Counter(words).most_common()
    return ", ".join(list(zip(*words))[0][:count])

def main(url, count):
    print(getMostFrequentWords(url, count))