import requests, json, os, sys, csv, urls, pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import drive


# ---------- #
#    TODO    #
# ---------- #
# - Scrape draftable players and their salaries



# Sport IDs: Hockey=3, NFL=1


def get_slate(sportId, type):
    counter = 0
    draft_group_id = []
    slate = {}
    soup = drive(urls.upcoming_draft_groups())
    body_div = soup.find('div', {'id': 'body'})
    show_json = body_div.find('div', {'id': 'show-json'})
    json_data = show_json.find('textarea').text
    newDict = json.loads(str(json_data))
    for x in newDict['draftGroups']:
        if x['sportId'] == sportId and 'startTimeSuffix' not in x and 'Featured' in x['allTags']:
            draft_group_id.append(x['draftGroupId'])
    r = requests.get(urls.draftables_url(draft_group_id[0])).json()
    for game in r['competitions']:
        slate[game['name']] = {
            'home': {
                'abbreviation': game['homeTeam']['abbreviation'],
                'id': game['homeTeam']['teamId']
                },
            'away': {
                'abbreviation': game['awayTeam']['abbreviation'],
                'id': game['awayTeam']['teamId']
                }
            }
        counter += 1
    return slate



#
