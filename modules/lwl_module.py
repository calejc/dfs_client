import os, sys
sys.path.append('..')
import requests, json, helpers.utils as utils, helpers.urls as urls
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


# print(os.getenv('LWL_USER'))
# print(os.getenv('LWL_PASS'))

# Need to also scrape the 'jerseys' to get Line1. Following function is working correctly to get the other 3 lines. Also make sure to get powerplay lines

def get_lines(secondary_name):

    # payload = {'login': 'thortney@mailbox.org', 'password': 'Gobigred22'}
    # payload = {'login': os.getenv(), 'password': 'Gobigred22'}
    post_url = 'https://leftwinglock.com/forum/index.php?login/login'
    get_url = 'https://leftwinglock.com/line-combinations/boston-bruins/?team=boston-bruins&strength=EV&gametype=GD'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    with requests.Session() as session:
        session.headers = headers
        post = session.post(post_url, data=payload)
        r = session.get(get_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        team_div = soup.find('ul', {'class': 'team__players'})
        # for li in team_div.find_all('li', {'class': 'team__position'}):
        #     print(li.text)
        for i in range(3):
            # print(i)
            print('\n')
            for x in team_div.find_all('li', {'class': 'team__position'}):
                for t in x.find_all('li', {'class': 'team__players-list-item'})[i]:
                    # print(t['href'])
                    x = parse_link(t['href'])
                    print(x)
def lines(team_slug, strength, gametype):
    get_url = urls.lwl_lines_url(
        team_slug,
        strength,
        gametype
    )
    payload = {
        'login': os.getenv('LWL_USER'),
        'password': os.getenv('LWL_PASS')
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    with requests.Session() as session:
        session.headers = headers
        post = session.post(urls.lwl_login_url(), data=payload)
        r = session.get(get_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        team_div = soup.find('ul', {'class': 'team__players'})
        # for li in team_div.find_all('li', {'class': 'team__position'}):
        #     print(li.text)
        for i in range(3):
            # print(i)
            print('\n')
            for x in team_div.find_all('li', {'class': 'team__position'}):
                for t in x.find_all('li', {'class': 'team__players-list-item'})[i]:
                    # print(t['href'])
                    x = utils.parse_link(t['href'])
                    print(x)
                    print("------")
