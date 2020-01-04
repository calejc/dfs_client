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
    dd = data.TEAM_DATA
    counter, game_count, id_counter = 1, 1, 1
    draft_group_id = []
    dg_ids = {}
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
            dg_ids[id_counter] = {
                'id': x['draftGroupId'],
                'start': utils.strip_datetime(x['minStartTime'])
            }

    # Need to identify the next starting slate, and make sure we have the correct slate ID. Not sure best route here.
    # for id in dg_ids:
        # idx = id

    print(draft_group_id)
    print(dg_ids)
    # print(dg_ids[1]['start'])
    # print(draft_group_id[0])
    print(urls.draftables_url(32648))
    r = requests.get(urls.draftables_url(draft_group_id[0])).json()
    for game in r['competitions']:
        print(game)
        for x in data.TEAM_DATA:
            if game['homeTeam']['abbreviation'] in data.TEAM_DATA[x]['dk_abbreviation']:
                team1 = data.TEAM_DATA[x]['secondary_name']
            elif game['awayTeam']['abbreviation'] in data.TEAM_DATA[x]['dk_abbreviation']:
                team2 = data.TEAM_DATA[x]['secondary_name']
        slate[counter] = {
            'team': team1,
            'opp': utils.return_alt(dd, game['awayTeam']['abbreviation'], 'nst_abbreviation')
            # 'opp': game['awayTeam']['abbreviation']
        }
        counter += 1
        slate[counter] = {
            'team': team2,
            'opp': utils.return_alt(dd, game['homeTeam']['abbreviation'], 'nst_abbreviation')
            # 'opp': game['homeTeam']['abbreviation']
        }
        counter += 1
        game_count += 1

    df_slate = pd.DataFrame.from_dict(slate, orient='index')

    # Until can figure out how to merge multi index, need to use the following indexing code after all merging is done:
    # df_slate = df_slate.set_index(['game', 'team'])

    return df_slate
