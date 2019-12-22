import requests, json, sys
sys.path.append('..')
import data, helpers.urls as urls, pandas as pd, helpers.utils as utils, datetime as dt, operator


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
#   - 'baseball_mlb'              #
#  Regions:                       #
#   - eu  -> pinnacle             #
#   - uk  -> william hill         #
# ------------------------------- #





def return_odds(sport, region, market):
    url = urls.get_odds_url(sport, region, market)
    # print(url)
    data = requests.get(url)
    data_dict = data.json()

    # Warning when running out of API calls
    remaining = data.headers['x-requests-remaining']
    if int(remaining) < 100:
        print("\n=============================================")
        print("Beware! only {} calls left for the month!".format(remaining))
        print("=============================================\n")

    odds = {}
    pinnacle_games = []
    games = {}
    odds = {}
    counter = 1
    for game in data_dict['data']:
        game_time =  dt.datetime.fromtimestamp(game['commence_time']).date()
        # if 'pinnacle' in map(operator.itemgetter('site_key'), game['sites']):
        #     pinnacle_games.append(data_dict['data'].index(game))
        for site in game['sites']:
            if 'pinnacle' in site['site_key']:
                game_index = data_dict['data'].index(game)
                pinnacle_index = game['sites'].index(site)

                games[data_dict['data'].index(game)] = game['sites'].index(site)

                for team in data_dict['data'][game_index]['teams']:
                    team_index = data_dict['data'][game_index]['teams'].index(team)
                    teams_odds = game['sites'][pinnacle_index]['odds'][market][team_index]
                    # print(team + " - " + str(team_index) + " - " +  str(teams_odds))

                    # odds[counter] = {team: teams_odds}
                    odds[team] = teams_odds
                    counter += 1
        ### Make a dict. Turn it into a DF. Merge

    # print(games)
    df_odds = pd.DataFrame.from_dict(odds, orient='index')
    # print(odds)
    print(df_odds)
return_odds('icehockey_nhl', 'eu', 'h2h')
