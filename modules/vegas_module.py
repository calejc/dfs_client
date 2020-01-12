#!/usr/bin/env python3
import requests, json, sys, os
sys.path.append('..')
import data, helpers.urls as urls, pandas as pd, helpers.utils as utils, datetime as dt, sqlite3 as sql3


# ------------------------------------- #
#     Decimal to US Odds Conversion     #
# ------------------------------------- #
#   For decimal odds >= 2.00:           #
#     ->  US Odds = (Decimal - 1) * 100 #
#   For decimal odds <= 2.00:           #
#     ->  US Odds = (-100)/(Decimal -1) #
# ------------------------------------- #


# ---------- #
#    TODO    #
# ------------------------------------------------ #
#  - make a site_index function                    #
#    - can find other sites besides pinnacle       #
#    - list of preffered sites in order?           #
#                                                  #
#  - Store opening line, and then track mvmt       #
#    - maybe add a delta column along with         #
#    - could also have High/Low columns??          #
#                                                  #
#  - Handle all args in function (**kwargs?)       #
#    - Request single input -> Sport abbreviation  #
#    - Take input, return dk_id for game_id        #
#    - Also return odds_key                        #
#                                                  #
#  - Do not require a region anymore.              #
#    - Aumatically pull all the sites in the list  #
#    - Will need to scrape EU and UK and US        #
#    - Make an 'index' average of all the sites    #
#                                                  #
# ------------------------------------------------ #


def return_market(sport_key, region, mkt):
    # DB_PATH = os.path.join('..', 'odds.db')
    # conn = sql3.connect(DB_PATH)
    # curs = conn.cursor()
    if sport_key == 'icehockey_nhl':
        sportId = 3
        dd = data.NHL_TEAMS
    elif sport_key == 'basketball_nba':
        sportId = 4
        dd = data.NBA_TEAMS
    elif sport_key == 'americanfootball_nfl':
        sportId = 1
        dd = data.NFL_TEAMS
    elif sport_key == 'baseball_mlb':
        sportId = 2
        dd = data.MLB_TEAMS
    else:
        print("No data dictionary for {}".format(sport_key))
        return

    url = urls.get_odds_url(sport_key, region, mkt)
    # print(url)
    data_r = requests.get(url)
    data_dict = data_r.json()
    remaining = data_r.headers['x-requests-remaining']
    if int(remaining) < 500:
        print("\n=============================================")
        print("Beware! only {} calls left for the month!".format(remaining))
        print("=============================================\n")

    games, odds, counter, game_counter = {}, {}, 1, 0
    upcoming, contains_pinnacle, contains_secondary = True, False, False
    prev_date = None
    for game in data_dict['data']:
        game_date =  dt.datetime.fromtimestamp(game['commence_time']).date()
        if prev_date is not None:
            if game_date > prev_date:
                game_counter = 0
        game_id = utils.game_ids(sportId, game_date, game_counter)
        game_counter += 1

        # Compare timestamps to remove active games.
        # Can remove this after we get the DK Slates set
        game_ts = game['commence_time']
        now_ts = dt.datetime.timestamp(dt.datetime.now())
        if now_ts < game_ts:
            upcoming = True
        else:
            upcoming = False
        # ------------------------------------------------------------- #
        # ------------------------------------------------------------- #
        if upcoming == True:
            if game['sites_count'] > 0:
                game_index = data_dict['data'].index(game)
                for site in game['sites']:
                    # If Site in List of Sites: ->
                    if 'pinnacle' in site['site_key']:
                        pinnacle_index = game['sites'].index(site)
                        contains_pinnacle = True
                        break
                    else:
                        contains_pinnacle = False
                if contains_pinnacle == True:
                    site_index = pinnacle_index
                else:
                    site_index = 0

                for team in data_dict['data'][game_index]['teams']:
                    team_index = data_dict['data'][game_index]['teams'].index(team)
                    if mkt == 'totals':
                        teams_odds = None
                        overUnder = game['sites'][site_index]['odds']['totals']['points'][0]
                        odds[counter] = {
                            'game_id': game_id,
                            # 'date': game_date,
                            # 'pinnacle': contains_pinnacle,
                            'team': team,
                            '{}'.format(
                                mkt
                            ): overUnder
                        }
                        counter += 1
                    elif mkt == 'h2h':
                        overUnder = None
                        teams_odds = game['sites'][site_index]['odds'][mkt][team_index]
                        odds[counter] = {
                            'game_id': game_id,
                            # 'date': game_date,
                            # 'pinnacle': contains_pinnacle,
                            'team': team,
                            '{}'.format(
                                mkt
                            ): utils.convert_odds(teams_odds)
                        }
                        counter += 1
                    elif mkt == 'spreads':
                        overUnder = None
                        teams_odds = game['sites'][site_index]['odds'][mkt]['points'][team_index]
                        odds[counter] = {
                            'game_id': game_id,
                            # 'date': game_date,
                            # 'pinnacle': contains_pinnacle,
                            'team': team,
                            '{}'.format(
                                mkt
                            ): teams_odds
                        }
                        counter += 1
                    # try:
                    #     curs.execute('INSERT INTO odds (game_id, team, team_open, team_live, game_open, game_live) VALUES ("{gid}", "{tm}", "{mkt}", "{mkt}", "{totals}", "{totals}");'.\
                    #     format(gid=game_id, tm=team, mkt=teams_odds, totals=overUnder))
                    #     conn.commit()
                    # except sql3.IntegrityError:
                    #     print("ERROR::ID found in Database already")
        prev_date = dt.datetime.fromtimestamp(game['commence_time']).date()

    # return odds
    for g in odds:
        t = odds[g]['team']
        gid = odds[g]['game_id']
        odds[g]['opp'] = utils.check(odds, gid, t)
        # odds[g]['opp'] = utils.return_alt(dd, opp, 'nst_abbreviation')

    df_odds = pd.DataFrame.from_dict(odds, orient='index')
    df_odds = df_odds[['game_id', 'team', 'opp', mkt]]
    return df_odds
# return_market('icehockey_nhl', 'eu', 'h2h')







# Returns a df with teams and their implied team totals
def return_tm_totals(sport, slate_df, *args):
    tm_totals, counter, arg_df = {}, 1, 0
    sport_key = data.SPORTS[sport]['odds_key']
    # sportId = data.SPORTS[sport]['dk_id']
    print(sportId)
    default_h2h = ['NHL', 'MLB']
    default_spreads = ['NBA', 'NFL', 'NCAAB', 'NCAAF']
    markets, regions = ['h2h', 'spreads'], ['us', 'eu', 'uk']
    region = 'eu' # Default

    for r in regions:
        if r in args:
            region = r
    if sport in default_h2h:
        mkt = 'h2h'
    elif sport in default_spreads:
        mkt = 'spreads'

    for m in markets:
        if m in args:
            mkt = m


    # print(urls.get_odds_url(sport_key, region, mkt))


    df = pd.merge(
        return_market(sport_key, region, mkt),
        return_market(sport_key, region, 'totals'),
        on = ['game_id', 'team', 'opp']
    )
    # print(df)
    new_df = pd.merge(slate_df, df, how='left', on=['team', 'opp'])
    new_df = new_df[['game_id', 'team', 'opp', mkt, 'totals']]
    # print(new_df)
    for index, row in new_df.iterrows():
        if sport_key == 'americanfootball_nfl' or sport_key == 'basketball_nba' or sport_key == 'basketball_ncaab' or sport_key == 'americanfootball_ncaaf':
            t = utils.spreads_team_total(float(row['spreads']), float(row['totals']))
        else:
            t = utils.team_total(float(row['h2h']), float(row['totals']))
        tm_totals[counter] = {
            'team': row['team'],
            'tm_total': t
        }
        counter += 1
    tm_totals = pd.DataFrame.from_dict(tm_totals, orient='index')
    df_odds = new_df.merge(tm_totals, how='left', on=['team'])
    df_odds = df_odds.drop([mkt, 'totals', 'opp'], axis=1)
    return df_odds
