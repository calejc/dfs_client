import requests, json, sys
sys.path.append('..')
import helpers.utils as utils
import data
import pandas as pd


# ------------------------------------- #
#     Decimal to US Odds Conversion     #
# ------------------------------------- #
#   For decimal odds >= 2.00:           #
#     ->  US Odds = (Decimal - 1) * 100 #
#   For decimal odds <= 2.00:           #
#     ->  US Odds = (-100)/(Decimal -1) #
# ------------------------------------- #


# ------------------------------- #
#            API Notes            #
# ------------------------------- #
#  Markets:                       #
#   - 'totals' for O/U            #
#   - 'spreads' for handicap      #
#   - 'h2h' for moneyline         #
#  Sports:                        #
#   - 'icehockey_nhl'             #
#   - 'americanfootball_ncaaf'    #
#   - 'americanfootball_nfl'      #
#   - 'basketball_nba'            #
#   - 'basketball_ncaab'          #
#   - **No Baseball**             #
# ------------------------------- #


def get_odds(sport, mkt):
    url = "https://api.the-odds-api.com/v3/odds/?apiKey=a3463cdc124f7d30bb0c868de5da3a8f&sport={SPORT}&region=eu&mkt={MARKET}".format(
        SPORT = sport,
        MARKET = mkt
    )
    data = requests.get(url)
    data_dict = data.json()
    print(url)
    # Warning when running out of API calls
    remaining = data.headers['x-requests-remaining']
    if int(remaining) < 100:
        print("\n=============================================")
        print("Beware! only {} calls left for the month!".format(remaining))
        print("=============================================\n")

    odds = {}
    for game in data_dict['data']:
        # if 'pointsbetus' in game[]
        if len(game['sites']) > 1:
            print(game['teams'])


# get_odds('icehockey_nhl', 'spreads')
# winning percentage = (RS^2) / ((RS^2) + (RA^2))
