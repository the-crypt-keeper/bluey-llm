import requests
from bs4 import BeautifulSoup

scripts_url = 'https://blueypedia.fandom.com/wiki/Category:Script'
scripts_html = requests.get(scripts_url).text
script_links = BeautifulSoup(scripts_html, 'html.parser').find_all('a')
for link in script_links:
    if link.get('href','').endswith('/Script'):
        print(link.get('href'))
        script_html = requests.get('https://blueypedia.fandom.com' + link.get('href')).text
        script_soup = BeautifulSoup(script_html, 'html.parser')
        script_name = script_soup.find('h1').text.replace('/Script','').strip()
        script_text = script_soup.find('div', {'class': 'mw-parser-output'}).text
        with open(script_name + '.txt', 'w') as f:
            f.write(script_text)
        print('Done with ' + script_name)
    else:
        print('Not a wiki link')