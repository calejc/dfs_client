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





def return_market(sport, region, market):
    url = urls.get_odds_url(sport, region, market)
    data = requests.get(url)
    data_dict = data.json()
    # Warning when running out of API calls
    remaining = data.headers['x-requests-remaining']
    if int(remaining) < 100:
        print("\n=============================================")
        print("Beware! only {} calls left for the month!".format(remaining))
        print("=============================================\n")

    odds = {}
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
                    if market == 'totals':
                        overUnder = game['sites'][pinnacle_index]['odds']['totals']['points'][0]
                        odds[counter] = {
                            'team': team,
                            '{}'.format(
                                market
                            ): overUnder
                        }
                        counter += 1
                    elif market == 'h2h':
                        teams_odds = game['sites'][pinnacle_index]['odds'][market][team_index]
                        odds[counter] = {
                            'team': team,
                            '{}'.format(
                                market
                            ): utils.convert_odds(teams_odds)
                        }
                        counter += 1
                    elif market == 'spreads':
                        teams_odds = game['sites'][pinnacle_index]['odds'][market]['points'][team_index]
                        odds[counter] = {
                            'team': team,
                            '{}'.format(
                                market
                            ): teams_odds
                        }
                        counter += 1


    df_odds = pd.DataFrame.from_dict(odds, orient='index')
    return df_odds

# Returns a pandas df with teams and their implied team totals
def return_tm_totals(sport, region, market):
    tm_totals = {}
    counter = 1
    # x = return_market(sport, region, market)
    # y = return_market(sport, region, 'totals')
    df = pd.merge(
        return_market(sport, region, market),
        return_market(sport, region, 'totals'),
        on = 'team'
    )
    for index, row in df.iterrows():
        if sport == 'americanfootball_nfl':
            t = utils.nfl_team_total(float(row['spreads']), float(row['totals']))
        else:
            t = utils.team_total(float(row['h2h']), float(row['totals']))
        tm_totals[counter] = {
            'team': row['team'],
            'tm_total': t
        }
        counter += 1
    tm_totals = pd.DataFrame.from_dict(tm_totals, orient='index')
    df_odds = pd.merge(df, tm_totals, on='team', how='left')
    # df_odds = df_odds.drop(['h2h', 'totals'], axis=1)
    return df_odds
