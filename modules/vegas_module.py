import requests
import json
import pandas as pd
import numpy as np

def get_odds(sport, mkt):
    url = "https://api.the-odds-api.com/v3/odds/?apiKey=a3463cdc124f7d30bb0c868de5da3a8f&sport={}&region=us&mkt={}".format(sport, mkt)
    data = requests.get(url)
    data_dict = data.json()

    # Warning when running out of API calls
    remaining = data.headers['x-requests-remaining']
    if int(remaining) < 200:
        print("\n=============================================")
        print("Beware! only {} calls left for the month!".format(remaining))
        print("=============================================\n")

    team_0 = {}
    # team_1 = []
    odds = {}
    for game in data_dict['data']:

        # teams = game['teams']
        print(team)
        # team_0 = game['teams']['0']
        # team_1 = game['teams']['1']
        # print(team_0 + "  " + team_1)
        # odds_0 = game['sites']['0']['h2h']['0']
        # odds_1 = game['sites']['0']['h2h']['1']
        # odds[game] = {'team_0': odds_0, 'team_1': odds_1}

get_odds('icehockey_nhl', 'spreads')
# winning percentage = (RS^2) / ((RS^2) + (RA^2))
