import requests, json, os, sys, csv, pickle
sys.path.append('..')
from bs4 import BeautifulSoup
from selenium import webdriver
import helpers.utils as utils, helpers.urls as urls, pandas as pd, data


# ---------- #
#    TODO    #
# ---------- #
# - Scrape draftable players and their salaries



def get_slate(sportId, type):
    counter = 1
    game_count = 1
    draft_group_id = []
    slate = {}
    soup = utils.drive(urls.upcoming_draft_groups_url())
    body_div = soup.find('div', {'id': 'body'})
    show_json = body_div.find('div', {'id': 'show-json'})
    json_data = show_json.find('textarea').text
    newDict = json.loads(str(json_data))


    ########################################
    ## Upon decision to add showdown, tiers, etc, will need to add to this ifelse function and create lists of applicable IDs in data.py
    ########################################
    if type == 'Classic':
        check_list = data.CLASSIC_IDS
    ########################################

    for x in newDict['draftGroups']:
        if x['sportId'] == sportId and 'startTimeSuffix' not in x and 'Featured' in x['allTags'] and x['contestType']['contestTypeId'] in check_list:
            draft_group_id.append(x['draftGroupId'])
    # print(draft_group_id)
    r = requests.get(urls.draftables_url(draft_group_id[0])).json()
    for game in r['competitions']:
        for x in data.TEAM_DATA:
            if game['homeTeam']['abbreviation'] in data.TEAM_DATA[x]['dk_abbreviation']:
                team1 = data.TEAM_DATA[x]['secondary_name']
            elif game['awayTeam']['abbreviation'] in data.TEAM_DATA[x]['dk_abbreviation']:
                team2 = data.TEAM_DATA[x]['secondary_name']
        slate[counter] = {
            'game': game_count,
            'team': team1,
            'opp': game['awayTeam']['abbreviation']
        }
        counter += 1
        slate[counter] = {
            'game': game_count,
            'team': team2,
            'opp': game['homeTeam']['abbreviation']
        }
        counter += 1
        game_count += 1

    df_slate = pd.DataFrame.from_dict(slate, orient='index')

    # Until can figure out how to merge multi index, need to use the following indexing code after all merging is done:
    # df_slate = df_slate.set_index(['game', 'team'])
    
    return df_slate
