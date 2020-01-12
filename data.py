from enum import Enum

# Data
# Start of 2019 NHL season => 2019-10-02


# ---------------------------------- #
#    NaturalStatTrick data classes   #
# ---------------------------------- #
class nst_sit(Enum):
    ALL_STRENGTHS = 'all'
    EVEN_STRENGTH = 'ev'
    FULL_STRENGTH = '5v5'
    FULL_ADJUSTED = 'sva' # Score and venue adjusted
    POWERPLAY = 'pp'
    FIVE_ON_FOUR_PP = '5v4'
    PENALTYKILL = 'pk'
    FOUR_ON_FIVE_PK = '4v5'
    WITH_EMPTY_NET = 'enf'
    AGAINST_EMPTY_NET = 'ena'

class nst_score(Enum):
    ALL_SCORES = 'all'
    TIED = 'tied'
    LEADING = 'u'
    TRAILING = 'd'
    WITHIN_ONE = 'w1'
    UP_ONE = 'u1'
    DOWN_ONE = 'd1'

class nst_rate(Enum):
    RATES = 'y'
    COUNTS = 'n'

class nst_loc(Enum):
    HOME_AND_AWAY = 'B'
    HOME = 'H'
    AWAY = 'A'

class nst_gpf(Enum):
    FULL_SEASON = '410'
    LAST_TEN = '10'



# ------------------------------- #
#    LeftWingLock data classes    #
# ------------------------------- #
class lwl_strengths(Enum):
    EV = 'EV'

class lwl_gametypes(Enum):
    GAMEDAY = 'GD'
    MOST_RECENT = '1'
    LAST_3 = '3'


# -------------------------------- #
#    DraftkingsAPI data classes    #
# -------------------------------- #
CLASSIC_IDS = (1, 72, 122, 98, 70, 94, 125, 21)
SHOWDOWN_IDS = []



# -------------------------- #
#    NHL_API data classes    #
# -------------------------- #



# ----------------------------------------- #
#          Sports IDs, keys, names          #
#  Keys are named by 'title' from odds API  #
# ----------------------------------------- #
SPORTS = {
    'NFL':{
        'dk_id': 1,
        'dk_name': 'NFL',
        'odds_key': 'americanfootball_nfl'
    },
    'NHL':{
        'dk_id': 3,
        'dk_name': 'NHL',
        'odds_key': 'icehockey_nhl'
    },
    'NBA':{
        'dk_id': 4,
        'dk_name': 'NBA',
        'odds_key': 'basketball_nba'
    },
    'MLB':{
        'dk_id': 2,
        'dk_name': 'MLB',
        'odds_key': 'baseball_mlb'
    },
    'GOLF':{
        'dk_id': 13,
        'dk_name': 'GOLF'
    },
    'EPL':{
        'dk_id': 12,
        'dk_name': 'SOC',
        'odds_key': 'soccer_epl'
    },
    'NCAAF':{
        'dk_id': 5,
        'dk_name': 'CFB',
        'odds_key': 'americanfootball_ncaaf'
    },
    'NCAAB':{
        'dk_id': 6,
        'dk_name': 'CBB',
        'odds_key': 'basketball_ncaab'
    },
    'MMA':{
        'dk_id': 9,
        'dk_name': 'MMA',
        'odds_key': 'mma_mixed_martial_arts'
    }
}




# ---------------------------------------- #
#    All Team Ids, Names, Abbreviations    #
# ---------------------------------------- #

# --------- #
#    NHL    #
# --------- #
NHL_TEAMS = {
    'NJD': {
     'dk_abbreviation': 'NJ',
     'dk_team_id': 4964,
     'nhl_id': 1,
     'name': 'New Jersey Devils',
     'secondary_name': 'New Jersey Devils',
     'slug': 'new-jersey-devils',
     'nhl_abbreviation': 'NJD',
     'nst_abbreviation': 'N.J',
    },
    'NYI': {
     'dk_abbreviation': 'NYI',
     'dk_team_id': 4965,
     'nhl_id': 2,
     'name': 'New York Islanders',
     'secondary_name': 'New York Islanders',
     'slug': 'new-york-islanders',
     'nhl_abbreviation': 'NYI',
     'nst_abbreviation': 'NYI',
    },
    'NYR': {
     'dk_abbreviation': 'NYR',
     'dk_team_id': 4966,
     'nhl_id': 3,
     'name': 'New York Rangers',
     'secondary_name': 'New York Rangers',
     'slug': 'new-york-rangers',
     'nhl_abbreviation': 'NYR',
     'nst_abbreviation': 'NYR',
    },
    'PHI': {
     'dk_abbreviation': 'PHI',
     'dk_team_id': 4968,
     'nhl_id': 4,
     'name': 'Philadelphia Flyers',
     'secondary_name': 'Philadelphia Flyers',
     'slug': 'philadelphia-flyers',
     'nhl_abbreviation': 'PHI',
     'nst_abbreviation': 'PHI',
    },
    'PIT': {
     'dk_abbreviation': 'PIT',
     'dk_team_id': 4969,
     'nhl_id': 5,
     'name': 'Pittsburgh Penguins',
     'secondary_name': 'Pittsburgh Penguins',
     'slug': 'pittsburgh-penguins',
     'nhl_abbreviation': 'PIT',
     'nst_abbreviation': 'PIT',
    },
    'BOS': {
     'dk_abbreviation': 'BOS',
     'dk_team_id': 4954,
     'nhl_id': 6,
     'name': 'Boston Bruins',
     'secondary_name': 'Boston Bruins',
     'slug': 'boston-bruins',
     'nhl_abbreviation': 'BOS',
     'nst_abbreviation': 'BOS',
    },
    'BUF': {
     'dk_abbreviation': 'BUF',
     'dk_team_id': 4955,
     'nhl_id': 7,
     'name': 'Buffalo Sabres',
     'secondary_name': 'Buffalo Sabres',
     'slug': 'buffalo-sabres',
     'nhl_abbreviation': 'BUF',
     'nst_abbreviation': 'BUF',
    },
    'MTL': {
     'dk_abbreviation': 'MON',
     'dk_team_id': 4963,
     'nhl_id': 8,
     'name': 'Montreal Canadiens',
     'secondary_name': 'Montreal Canadiens',
     'slug': 'montreal-canadiens',
     'nhl_abbreviation': 'MTL',
     'nst_abbreviation': 'MTL',
    },
    'OTT': {
     'dk_abbreviation': 'OTT',
     'dk_team_id': 4967,
     'nhl_id': 9,
     'name': 'Ottawa Senators',
     'secondary_name': 'Ottawa Senators',
     'slug': 'ottawa-senators',
     'nhl_abbreviation': 'OTT',
     'nst_abbreviation': 'OTT',
    },
    'TOR': {
     'dk_abbreviation': 'TOR',
     'dk_team_id': 4974,
     'nhl_id': 10,
     'name': 'Toronto Maple Leafs',
     'secondary_name': 'Toronto Maple Leafs',
     'slug': 'toronto-maple-leafs',
     'nhl_abbreviation': 'TOR',
     'nst_abbreviation': 'TOR',
    },
    'CAR': {
     'dk_abbreviation': 'CAR',
     'dk_team_id': 4960,
     'nhl_id': 12,
     'name': 'Carolina Hurricanes',
     'secondary_name': 'Carolina Hurricanes',
     'slug': 'carolina-hurricanes',
     'nhl_abbreviation': 'CAR',
     'nst_abbreviation': 'CAR',
    },
    'FLA': {
     'dk_abbreviation': 'FLA',
     'dk_team_id': 4979,
     'nhl_id': 13,
     'name': 'Florida Panthers',
     'secondary_name': 'Florida Panthers',
     'slug': 'florida-panthers',
     'nhl_abbreviation': 'FLA',
     'nst_abbreviation': 'FLA',
    },
    'TBL': {
     'dk_abbreviation': 'TB',
     'dk_team_id': 4973,
     'nhl_id': 14,
     'name': 'Tampa Bay Lightning',
     'secondary_name': 'Tampa Bay Lightning',
     'slug': 'tampa-bay-lightning',
     'nhl_abbreviation': 'TBL',
     'nst_abbreviation': 'T.B',
    },
    'WSH': {
     'dk_abbreviation': 'WAS',
     'dk_team_id': 4976,
     'nhl_id': 15,
     'name': 'Washington Capitals',
     'secondary_name': 'Washington Capitals',
     'slug': 'washington-capitals',
     'nhl_abbreviation': 'WSH',
     'nst_abbreviation': 'WSH',
    },
    'CHI': {
     'dk_abbreviation': 'CHI',
     'dk_team_id': 4957,
     'nhl_id': 16,
     'name': 'Chicago Blackhawks',
     'secondary_name': 'Chicago Blackhawks',
     'slug': 'chicago-blackhawks',
     'nhl_abbreviation': 'CHI',
     'nst_abbreviation': 'CHI',
    },
    'DET': {
     'dk_abbreviation': 'DET',
     'dk_team_id': 4958,
     'nhl_id': 17,
     'name': 'Detroit Red Wings',
     'secondary_name': 'Detroit Red Wings',
     'slug': 'detroit-red-wings',
     'nhl_abbreviation': 'DET',
     'nst_abbreviation': 'DET',
    },
    'NSH': {
     'dk_abbreviation': 'NSH',
     'dk_team_id': 4980,
     'nhl_id': 18,
     'name': 'Nashville Predators',
     'secondary_name': 'Nashville Predators',
     'slug': 'nashville-predators',
     'nhl_abbreviation': 'NSH',
     'nst_abbreviation': 'NSH',
    },
    'STL': {
     'dk_abbreviation': 'STL',
     'dk_team_id': 4972,
     'nhl_id': 19,
     'name': 'St. Louis Blues',
     'secondary_name': 'St Louis Blues',
     'slug': 'st-louis-blues',
     'nhl_abbreviation': 'STL',
     'nst_abbreviation': 'STL',
    },
    'CGY': {
     'dk_abbreviation': 'CGY',
     'dk_team_id': 4956,
     'nhl_id': 20,
     'name': 'Calgary Flames',
     'secondary_name': 'Calgary Flames',
     'slug': 'calgary-flames',
     'nhl_abbreviation': 'CGY',
     'nst_abbreviation': 'CGY',
    },
    'COL': {
     'dk_abbreviation': 'COL',
     'dk_team_id': 4970,
     'nhl_id': 21,
     'name': 'Colorado Avalanche',
     'secondary_name': 'Colorado Avalanche',
     'slug': 'colorado-avalanche',
     'nhl_abbreviation': 'COL',
     'nst_abbreviation': 'COL',
    },
    'EDM': {
     'dk_abbreviation': 'EDM',
     'dk_team_id': 4959,
     'nhl_id': 22,
     'name': 'Edmonton Oilers',
     'secondary_name': 'Edmonton Oilers',
     'slug': 'edmonton-oilers',
     'nhl_abbreviation': 'EDM',
     'nst_abbreviation': 'EDM',
    },
    'VAN': {
     'dk_abbreviation': 'VAN',
     'dk_team_id': 4975,
     'nhl_id': 23,
     'name': 'Vancouver Canucks',
     'secondary_name': 'Vancouver Canucks',
     'slug': 'vancouver-canucks',
     'nhl_abbreviation': 'VAN',
     'nst_abbreviation': 'VAN',
    },
    'ANA': {
     'dk_abbreviation': 'ANH',
     'dk_team_id': 4978,
     'nhl_id': 24,
     'name': 'Anaheim Ducks',
     'secondary_name': 'Anaheim Ducks',
     'slug': 'anaheim-ducks',
     'nhl_abbreviation': 'ANA',
     'nst_abbreviation': 'ANA',
    },
    'DAL': {
     'dk_abbreviation': 'DAL',
     'dk_team_id': 4962,
     'nhl_id': 25,
     'name': 'Dallas Stars',
     'secondary_name': 'Dallas Stars',
     'slug': 'dallas-stars',
     'nhl_abbreviation': 'DAL',
     'nst_abbreviation': 'DAL',
    },
    'LAK': {
     'dk_abbreviation': 'LA',
     'dk_team_id': 4961,
     'nhl_id': 26,
     'name': 'Los Angeles Kings',
     'secondary_name': 'Los Angeles Kings',
     'slug': 'los-angeles-kings',
     'nhl_abbreviation': 'LAK',
     'nst_abbreviation': 'L.A',
    },
    'SJS': {
     'dk_abbreviation': 'SJ',
     'dk_team_id': 4971,
     'nhl_id': 28,
     'name': 'San Jose Sharks',
     'secondary_name': 'San Jose Sharks',
     'slug': 'san-jose-sharks',
     'nhl_abbreviation': 'SJS',
     'nst_abbreviation': 'S.J',
    },
    'CBJ': {
     'dk_abbreviation': 'CLS',
     'dk_team_id': 4982,
     'nhl_id': 29,
     'name': 'Columbus Blue Jackets',
     'secondary_name': 'Columbus Blue Jackets',
     'slug': 'columbus-blue-jackets',
     'nhl_abbreviation': 'CBJ',
     'nst_abbreviation': 'CBJ',
    },
    'MIN': {
     'dk_abbreviation': 'MIN',
     'dk_team_id': 4983,
     'nhl_id': 30,
     'name': 'Minnesota Wild',
     'secondary_name': 'Minnesota Wild',
     'slug': 'minnesota-wild',
     'nhl_abbreviation': 'MIN',
     'nst_abbreviation': 'MIN',
    },
    'WPG': {
     'dk_abbreviation': 'WPG',
     'dk_team_id': 4981,
     'nhl_id': 52,
     'name': 'Winnipeg Jets',
     'secondary_name': 'Winnipeg Jets',
     'slug': 'winnipeg-jets',
     'nhl_abbreviation': 'WPG',
     'nst_abbreviation': 'WPG',
    },
    'ARI': {
     'dk_abbreviation': 'ARI',
     'dk_team_id': 4977,
     'nhl_id': 53,
     'name': 'Arizona Coyotes',
     'secondary_name': 'Arizona Coyotes',
     'slug': 'arizona-coyotes',
     'nhl_abbreviation': 'ARI',
     'nst_abbreviation': 'ARI',
    },
    'VGK': {
     'dk_abbreviation': 'VGK',
     'dk_team_id': 58462,
     'nhl_id': 54,
     'name': 'Vegas Golden Knights',
     'secondary_name': 'Vegas Golden Knights',
     'slug': 'vegas-golden-knights',
     'nhl_abbreviation': 'VGK',
     'nst_abbreviation': 'VGK',
    }
}

# ------------------------------- #
# ------------------------------- #

# --------- #
#    NBA    #
# --------- #
NBA_TEAMS = {
  'ATL': {
    'tricode': 'ATL',
    'urlName': 'hawks',
    'teamShortName': 'Atlanta',
    'abbreviation': 'ATL',
    'dk_abbreviation': 'ATL',
    'name': 'Atlanta Hawks',
    'secondary_name': 'Atlanta Hawks',
    'nba_id': '1610612737',
    'dk_team_id': 0
  },
  'BOS': {
    'tricode': 'BOS',
    'urlName': 'celtics',
    'teamShortName': 'Boston',
    'abbreviation': 'BOS',
    'dk_abbreviation': 'BOS',
    'name': 'Boston Celtics',
    'secondary_name': 'Boston Celtics',
    'nba_id': '1610612738',
    'dk_team_id': 0
  },
  'BKN': {
    'tricode': 'BKN',
    'urlName': 'nets',
    'teamShortName': 'Brooklyn',
    'abbreviation': 'BKN',
    'dk_abbreviation': 'BKN',
    'name': 'Brooklyn Nets',
    'secondary_name': 'Brooklyn Nets',
    'nba_id': '1610612751',
    'dk_team_id': 0
  },
  'CHA': {
    'tricode': 'CHA',
    'urlName': 'hornets',
    'teamShortName': 'Charlotte',
    'abbreviation': 'CHA',
    'dk_abbreviation': 'CHA',
    'name': 'Charlotte Hornets',
    'secondary_name': 'Charlotte Hornets',
    'nba_id': '1610612766',
    'dk_team_id': 0
  },
  'CHI': {
    'tricode': 'CHI',
    'urlName': 'bulls',
    'teamShortName': 'Chicago',
    'abbreviation': 'CHI',
    'dk_abbreviation': 'CHI',
    'name': 'Chicago Bulls',
    'secondary_name': 'Chicago Bulls',
    'nba_id': '1610612741',
    'dk_team_id': 0
  },
  'CLE': {
    'tricode': 'CLE',
    'urlName': 'cavaliers',
    'teamShortName': 'Cleveland',
    'abbreviation': 'CLE',
    'dk_abbreviation': 'CLE',
    'name': 'Cleveland Cavaliers',
    'secondary_name': 'Cleveland Cavaliers',
    'nba_id': '1610612739',
    'dk_team_id': 0
  },
  'DAL': {
    'tricode': 'DAL',
    'urlName': 'mavericks',
    'teamShortName': 'Dallas',
    'abbreviation': 'DAL',
    'dk_abbreviation': 'DAL',
    'name': 'Dallas Mavericks',
    'secondary_name': 'Dallas Mavericks',
    'nba_id': '1610612742',
    'dk_team_id': 0
  },
  'DEN': {
    'tricode': 'DEN',
    'urlName': 'nuggets',
    'teamShortName': 'Denver',
    'abbreviation': 'DEN',
    'dk_abbreviation': 'DEN',
    'name': 'Denver Nuggets',
    'secondary_name': 'Denver Nuggets',
    'nba_id': '1610612743',
    'dk_team_id': 0
  },
  'DET': {
    'tricode': 'DET',
    'urlName': 'pistons',
    'teamShortName': 'Detroit',
    'abbreviation': 'DET',
    'dk_abbreviation': 'DET',
    'name': 'Detroit Pistons',
    'secondary_name': 'Detroit Pistons',
    'nba_id': '1610612765',
    'dk_team_id': 0
  },
  'GSW': {
    'tricode': 'GSW',
    'urlName': 'warriors',
    'teamShortName': 'Golden State',
    'abbreviation': 'GSW',
    'dk_abbreviation': 'GS',
    'name': 'Golden State Warriors',
    'secondary_name': 'Golden State Warriors',
    'nba_id': '1610612744',
    'dk_team_id': 0
  },
  'HOU': {
    'tricode': 'HOU',
    'urlName': 'rockets',
    'teamShortName': 'Houston',
    'abbreviation': 'HOU',
    'dk_abbreviation': 'HOU',
    'name': 'Houston Rockets',
    'secondary_name': 'Houston Rockets',
    'nba_id': '1610612745',
    'dk_team_id': 0
  },
  'IND': {
    'tricode': 'IND',
    'urlName': 'pacers',
    'teamShortName': 'Indiana',
    'abbreviation': 'IND',
    'dk_abbreviation': 'IND',
    'name': 'Indiana Pacers',
    'secondary_name': 'Indiana Pacers',
    'nba_id': '1610612754',
    'dk_team_id': 0
  },
  'LAC': {
    'tricode': 'LAC',
    'urlName': 'clippers',
    'teamShortName': 'LA Clippers',
    'abbreviation': 'LAC',
    'dk_abbreviation': 'LAC',
    'name': 'LA Clippers',
    'secondary_name': 'Los Angeles Clippers',
    'nba_id': '1610612746',
    'dk_team_id': 0
  },
  'LAL': {
    'tricode': 'LAL',
    'urlName': 'lakers',
    'teamShortName': 'L.A. Lakers',
    'abbreviation': 'LAL',
    'dk_abbreviation': 'LAL',
    'name': 'Los Angeles Lakers',
    'secondary_name': 'Los Angeles Lakers',
    'nba_id': '1610612747',
    'dk_team_id': 0
  },
  'MEM': {
    'tricode': 'MEM',
    'urlName': 'grizzlies',
    'teamShortName': 'Memphis',
    'abbreviation': 'MEM',
    'dk_abbreviation': 'MEM',
    'name': 'Memphis Grizzlies',
    'secondary_name': 'Memphis Grizzlies',
    'nba_id': '1610612763',
    'dk_team_id': 0
  },
  'MIA': {
    'tricode': 'MIA',
    'urlName': 'heat',
    'teamShortName': 'Miami',
    'abbreviation': 'MIA',
    'dk_abbreviation': 'MIA',
    'name': 'Miami Heat',
    'secondary_name': 'Miami Heat',
    'nba_id': '1610612748',
    'dk_team_id': 0
  },
  'MIL': {
    'tricode': 'MIL',
    'urlName': 'bucks',
    'teamShortName': 'Milwaukee',
    'abbreviation': 'MIL',
    'dk_abbreviation': 'MIL',
    'name': 'Milwaukee Bucks',
    'secondary_name': 'Milwaukee Bucks',
    'nba_id': '1610612749',
    'dk_team_id': 0
  },
  'MIN': {
    'tricode': 'MIN',
    'urlName': 'timberwolves',
    'teamShortName': 'Minnesota',
    'abbreviation': 'MIN',
    'dk_abbreviation': 'MIN',
    'name': 'Minnesota Timberwolves',
    'secondary_name': 'Minnesota Timberwolves',
    'nba_id': '1610612750',
    'dk_team_id': 0
  },
  'NOP': {
    'tricode': 'NOP',
    'urlName': 'pelicans',
    'teamShortName': 'New Orleans',
    'abbreviation': 'NOP',
    'dk_abbreviation': 'NOP',
    'name': 'New Orleans Pelicans',
    'secondary_name': 'New Orleans Pelicans',
    'nba_id': '1610612740',
    'dk_team_id': 0
  },
  'NYK': {
    'tricode': 'NYK',
    'urlName': 'knicks',
    'teamShortName': 'New York',
    'abbreviation': 'NYK',
    'dk_abbreviation': 'NYK',
    'name': 'New York Knicks',
    'secondary_name': 'New York Knicks',
    'nba_id': '1610612752',
    'dk_team_id': 0
  },
  'OKC': {
    'tricode': 'OKC',
    'urlName': 'thunder',
    'teamShortName': 'Oklahoma City',
    'abbreviation': 'OKC',
    'dk_abbreviation': 'OKC',
    'name': 'Oklahoma City Thunder',
    'secondary_name': 'Oklahoma City Thunder',
    'nba_id': '1610612760',
    'dk_team_id': 0
  },
  'ORL': {
    'tricode': 'ORL',
    'urlName': 'magic',
    'teamShortName': 'Orlando',
    'abbreviation': 'ORL',
    'dk_abbreviation': 'ORL',
    'name': 'Orlando Magic',
    'secondary_name': 'Orlando Magic',
    'nba_id': '1610612753',
    'dk_team_id': 0
  },
  'PHI': {
    'tricode': 'PHI',
    'urlName': 'sixers',
    'teamShortName': 'Philadelphia',
    'abbreviation': 'PHI',
    'dk_abbreviation': 'PHI',
    'name': 'Philadelphia 76ers',
    'secondary_name': 'Philadelphia 76ers',
    'nba_id': '1610612755',
    'dk_team_id': 0
  },
  'PHX': {
    'tricode': 'PHX',
    'urlName': 'suns',
    'teamShortName': 'Phoenix',
    'abbreviation': 'PHX',
    'dk_abbreviation': 'PHO',
    'name': 'Phoenix Suns',
    'secondary_name': 'Phoenix Suns',
    'nba_id': '1610612756',
    'dk_team_id': 0
  },
  'POR': {
    'tricode': 'POR',
    'urlName': 'blazers',
    'teamShortName': 'Portland',
    'abbreviation': 'POR',
    'dk_abbreviation': 'POR',
    'name': 'Portland Trail Blazers',
    'secondary_name': 'Portland Trail Blazers',
    'nba_id': '1610612757',
    'dk_team_id': 0
  },
  'SAC': {
    'tricode': 'SAC',
    'urlName': 'kings',
    'teamShortName': 'Sacramento',
    'abbreviation': 'SAC',
    'dk_abbreviation': 'SAC',
    'name': 'Sacramento Kings',
    'secondary_name': 'Sacramento Kings',
    'nba_id': '1610612758',
    'dk_team_id': 0
  },
  'SAS': {
    'tricode': 'SAS',
    'urlName': 'spurs',
    'teamShortName': 'San Antonio',
    'abbreviation': 'SAS',
    'dk_abbreviation': 'SA',
    'name': 'San Antonio Spurs',
    'secondary_name': 'San Antonio Spurs',
    'nba_id': '1610612759',
    'dk_team_id': 0
  },
  'TOR': {
    'tricode': 'TOR',
    'urlName': 'raptors',
    'teamShortName': 'Toronto',
    'abbreviation': 'TOR',
    'dk_abbreviation': 'TOR',
    'name': 'Toronto Raptors',
    'secondary_name': 'Toronto Raptors',
    'nba_id': '1610612761',
    'dk_team_id': 0
  },
  'UTA': {
    'tricode': 'UTA',
    'urlName': 'jazz',
    'teamShortName': 'Utah',
    'abbreviation': 'UTA',
    'dk_abbreviation': 'UTA',
    'name': 'Utah Jazz',
    'secondary_name': 'Utah Jazz',
    'nba_id': '1610612762',
    'dk_team_id': 0
  },
  'WAS': {
    'tricode': 'WAS',
    'urlName': 'wizards',
    'teamShortName': 'Washington',
    'abbreviation': 'WAS',
    'dk_abbreviation': 'WAS',
    'name': 'Washington Wizards',
    'secondary_name': 'Washington Wizards',
    'nba_id': '1610612764',
    'dk_team_id': 0
  }
}





#
