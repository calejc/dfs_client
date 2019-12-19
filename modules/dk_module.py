import requests, json, os, sys, csv, pickle
sys.path.append('..')
from bs4 import BeautifulSoup
from selenium import webdriver
import helpers.utils as utils
import helpers.urls as urls
import pandas as pd


# ---------- #
#    TODO    #
# ---------- #
# - Scrape draftable players and their salaries



# Sport IDs: Hockey=3, NFL=1


def get_slate(sportId, type):
    counter = 0
    draft_group_id = []
    slate = {}
    slate_x = {}
    slate_y = {}
    soup = utils.drive(urls.upcoming_draft_groups())
    body_div = soup.find('div', {'id': 'body'})
    show_json = body_div.find('div', {'id': 'show-json'})
    json_data = show_json.find('textarea').text
    newDict = json.loads(str(json_data))
    for x in newDict['draftGroups']:
        if x['sportId'] == sportId and 'startTimeSuffix' not in x and 'Featured' in x['allTags']:
            draft_group_id.append(x['draftGroupId'])
    r = requests.get(urls.draftables_url(draft_group_id[0])).json()
    for game in r['competitions']:
        slate_y[counter] = {
            'team': game['homeTeam']['abbreviation'],
            'id': game['homeTeam']['teamId'],
            'opp': game['awayTeam']['abbreviation'],
            'opp_id': game['awayTeam']['teamId']
        }
        counter += 1
        slate_y[counter] = {
            'team': game['awayTeam']['abbreviation'],
            'id': game['awayTeam']['teamId'],
            'opp': game['homeTeam']['abbreviation'],
            'opp_id': game['homeTeam']['teamId']
        }
        ############################################
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
        ############################################
        counter += 1
    return slate_y

# x = get_slate(3, 'Classic')
# df1 = pd.DataFrame.from_dict(x, orient='index')
# print(df1)
