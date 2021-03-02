from bs4 import *
import requests
import re
import json

query = str(input("Enter trailer name: "))

imdb = requests.get('https://www.imdb.com/find?q=' + query + '&s=tt&ttype=ft&ref_=fn_ft')
soup = BeautifulSoup(imdb.text, 'html.parser')
results_element = soup.findAll('td', {'class': 'result_text'})
for result_element in results_element:
    results = result_element.findAll('a', href=True)
    for result in results:
        movie_name = result.text
        result = result['href']
        movie = requests.get('https://www.imdb.com' + str(result))
        soup = BeautifulSoup(movie.text, 'html.parser')
        try:
            result = soup.findAll('a', {'class': 'slate_button prevent-ad-overlay video-modal'})[0]["href"]
        except:
            print(movie_name + " has no trailer")
            continue

        trailer = requests.get('https://www.imdb.com/' + str(result) + '&ref_=tt_ov_vi')
        soup = BeautifulSoup(trailer.text, 'html.parser')

        script = soup.findAll('script', {'type': 'text/javascript'})[4]
        pattern = re.compile('var args = (.*);') 
        result = pattern.search(script.string).group(1)

        pattern = re.compile('\[(.*)\)\, ')
        toremove = pattern.search(result).group(0)
        result = result.replace(toremove, "")
        result = result[0:len(result) - 1]
        result = json.loads(result)
        result = str(result['playbackData'])

        pattern = re.compile("\['\[(.*)\]'\]")
        result = pattern.search(result).group(1)
        result = json.loads(result)
        result = result['videoLegacyEncodings'][1]['url']
        print("trailer for " + movie_name + ": " + result)
