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




# ---------- #
#    TODO    #
# -------------------------------------------- #
#  - dont scrape games that are in progress    #
#    - get datetime from timestamp             #
#    - get todays datetime                     #
#    - compare, discarding ongoing games       #
#                                              #
#  - make a site_index function                #
#    - can find other sites besides pinnacle   #
#    - list of preffered sites in order?       #
#                                              #
#  - Fix game_ids assignment                   #
#    - need to reset the counter for a new day #
#                                              #
#  - Store opening line, and then track mvmt   #
#    - maybe add a delta column along with     #
#    - could also have High/Low columns??      #
#                                              #
# -------------------------------------------- #



def return_market(sport, region, market):
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
    games = {}
    odds = {}
    counter = 1
    game_counter = 0
    sport_id = 3
    upcoming = True
    contains_pinnacle = True
    if sport == 'icehockey_nhl':
        sport_id = 3

    for game in data_dict['data']:
        game_date =  dt.datetime.fromtimestamp(game['commence_time']).date()
        game_id = utils.game_ids(3, game_date, game_counter)
        game_counter += 1
        game_ts = game['commence_time']
        now_ts = dt.datetime.timestamp(dt.datetime.now())
        if now_ts < game_ts:
            # print(game_id + '  ||  ' + str(game_date) + '  ||  ' + game['teams'][0] + ' vs ' + game['teams'][1])
            pass
        else:
            # print(game_id + '  ||  ' + str(game_date) + ' - ** IN PROGRESS ** - ' + game['teams'][0] + ' vs ' + game['teams'][1])
            upcoming = False


        if game['sites_count'] > 0:
            game_index = data_dict['data'].index(game)
            for site in game['sites']:
                if 'pinnacle' in site['site_key']:
                    pinnacle_index = game['sites'].index(site)
                    contains_pinnacle = True
                    break
                else:
                    contains_pinnacle = False
                # ------------------------------------------------------- #
                # ------------------------------------------------------- #
            if contains_pinnacle == True:
                site_index = pinnacle_index
            else:
                site_index = 0

            for team in data_dict['data'][game_index]['teams']:
                team_index = data_dict['data'][game_index]['teams'].index(team)
                if market == 'totals':
                    # print(site_index)
                    overUnder = game['sites'][site_index]['odds']['totals']['points'][0]
                    odds[counter] = {
                        'game_id': game_id,
                        'team': team,
                        '{}'.format(
                            market
                        ): overUnder
                    }
                    counter += 1
                elif market == 'h2h':
                    teams_odds = game['sites'][site_index]['odds'][market][team_index]
                    odds[counter] = {
                        'game_id': game_id,
                        'team': team,
                        '{}'.format(
                            market
                        ): utils.convert_odds(teams_odds)
                    }
                    counter += 1
                elif market == 'spreads':
                    teams_odds = game['sites'][site_index]['odds'][market]['points'][team_index]
                    odds[counter] = {
                        'game_id': game_id,
                        'team': team,
                        '{}'.format(
                            market
                        ): teams_odds
                    }
                    counter += 1

        # game_counter += 1
    df_odds = pd.DataFrame.from_dict(odds, orient='index')
    print(df_odds)
    print("\n#------------------------------------------------------------------#")
    print("#------------------------------------------------------------------#\n")
    return df_odds



# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #
# Returns a pandas df with teams and their implied team totals
def return_tm_totals(sport, region, market):
    tm_totals = {}
    counter = 1
    df = pd.merge(
        return_market(sport, region, market),
        return_market(sport, region, 'totals'),
        on = ['game_id', 'team']
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
    print(tm_totals)
    df_odds = df.merge(tm_totals, how='left', on=['team'])
    # df_odds = df_odds.drop(['h2h', 'totals'], axis=1)
    return df_odds
