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
    parsedText = []
    text = getWebpage(url).find_all("p")
    # data = parsedText.append([i.get_text().split() for i in text])
    data = parsedText.append([i.get_text() for i in text])
    return parsedText

# this returns the sentences instead of just the words, ideally these setneces can be parsed through soem kind of sentiment analysis 
# which will tell us if the article is positive, neutral, or negative. 

# def getMostFrequentWords(url, count):
#     unwantedWords = ["to","of","in","i","-","the", "and", "a", "is", "they", "i\'m", "them", "he", "him", "she", "her", "you", ")", "(", ",", "for", "my", "are", "though", "that", "also", "using", "an"]
#     words = getWebpageText(url).split()
#     words = [i for i in words if i not in unwantedWords]
#     words = Counter(words).most_common()
#     return " ".join(list(zip(*words))[0][:count])