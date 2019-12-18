from enum import Enum



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


# -------------------------------- #
#    DraftkingsAPI data classes    #
# -------------------------------- #
CLASSIC_IDS = [1, 72, 122, 98, 70, 94, 125, 21]
SHOWDOWN_IDS = []

class dk_sport_ids(Enum):
    NFL = 1
    NHL = 2


# -------------------------- #
#    NHL_API data classes    #
# -------------------------- #



# ---------------------------------------- #
#    All Team Ids, Names, Abbreviations    #
# ---------------------------------------- #
TEAM_DATA = {
    'NJD': {
     'dk_abbreviation': 'NJ',
     'dk_team_id': 4964,
     'nhl_id': 1,
     'name': 'New Jersey Devils',
     'slug': 'new-jersey-devils',
     'nhl_abbreviation': 'NJD',
     'nst_abbreviation': 'NJD',
    },
    'NYI': {
     'dk_abbreviation': 'NYI',
     'dk_team_id': 4965,
     'nhl_id': 2,
     'name': 'New York Islanders',
     'slug': 'new-york-islanders',
     'nhl_abbreviation': 'NYI',
     'nst_abbreviation': 'NYI',
    },
    'NYR': {
     'dk_abbreviation': 'NYR',
     'dk_team_id': 0,
     'nhl_id': 3,
     'name': 'New York Rangers',
     'slug': 'new-york-rangers',
     'nhl_abbreviation': 'NYR',
     'nst_abbreviation': 'NYR',
    },
    'PHI': {
     'dk_abbreviation': 'PHI',
     'dk_team_id': 4968,
     'nhl_id': 4,
     'name': 'Philadelphia Flyers',
     'slug': 'philadelphia-flyers',
     'nhl_abbreviation': 'PHI',
     'nst_abbreviation': 'PHI',
    },
    'PIT': {
     'dk_abbreviation': 'PIT',
     'dk_team_id': 4969,
     'nhl_id': 5,
     'name': 'Pittsburgh Penguins',
     'slug': 'pittsburgh-penguins',
     'nhl_abbreviation': 'PIT',
     'nst_abbreviation': 'PIT',
    },
    'BOS': {
     'dk_abbreviation': 'BOS',
     'dk_team_id': 4954,
     'nhl_id': 6,
     'name': 'Boston Bruins',
     'slug': 'boston-bruins',
     'nhl_abbreviation': 'BOS',
     'nst_abbreviation': 'BOS',
    },
    'BUF': {
     'dk_abbreviation': 'BUF',
     'dk_team_id': 4955,
     'nhl_id': 7,
     'name': 'Buffalo Sabres',
     'slug': 'buffalo-sabres',
     'nhl_abbreviation': 'BUF',
     'nst_abbreviation': 'BUF',
    },
    'MTL': {
     'dk_abbreviation': 'MON',
     'dk_team_id': 4963,
     'nhl_id': 8,
     'name': 'Montréal Canadiens',
     'slug': 'montréal-canadiens',
     'nhl_abbreviation': 'MTL',
     'nst_abbreviation': 'MTL',
    },
    'OTT': {
     'dk_abbreviation': 'OTT',
     'dk_team_id': 4967,
     'nhl_id': 9,
     'name': 'Ottawa Senators',
     'slug': 'ottawa-senators',
     'nhl_abbreviation': 'OTT',
     'nst_abbreviation': 'OTT',
    },
    'TOR': {
     'dk_abbreviation': 'TOR',
     'dk_team_id': 4974,
     'nhl_id': 10,
     'name': 'Toronto Maple Leafs',
     'slug': 'toronto-maple-leafs',
     'nhl_abbreviation': 'TOR',
     'nst_abbreviation': 'TOR',
    },
    'CAR': {
     'dk_abbreviation': 'CAR',
     'dk_team_id': 4960,
     'nhl_id': 12,
     'name': 'Carolina Hurricanes',
     'slug': 'carolina-hurricanes',
     'nhl_abbreviation': 'CAR',
     'nst_abbreviation': 'CAR',
    },
    'FLA': {
     'dk_abbreviation': 'FLA',
     'dk_team_id': 0,
     'nhl_id': 13,
     'name': 'Florida Panthers',
     'slug': 'florida-panthers',
     'nhl_abbreviation': 'FLA',
     'nst_abbreviation': 'FLA',
    },
    'TBL': {
     'dk_abbreviation': 'TB',
     'dk_team_id': 4973,
     'nhl_id': 14,
     'name': 'Tampa Bay Lightning',
     'slug': 'tampa-bay-lightning',
     'nhl_abbreviation': 'TBL',
     'nst_abbreviation': 'TBL',
    },
    'WSH': {
     'dk_abbreviation': 'WSH',
     'dk_team_id': 0,
     'nhl_id': 15,
     'name': 'Washington Capitals',
     'slug': 'washington-capitals',
     'nhl_abbreviation': 'WSH',
     'nst_abbreviation': 'WSH',
    },
    'CHI': {
     'dk_abbreviation': 'CHI',
     'dk_team_id': 4957,
     'nhl_id': 16,
     'name': 'Chicago Blackhawks',
     'slug': 'chicago-blackhawks',
     'nhl_abbreviation': 'CHI',
     'nst_abbreviation': 'CHI',
    },
    'DET': {
     'dk_abbreviation': 'DET',
     'dk_team_id': 4958,
     'nhl_id': 17,
     'name': 'Detroit Red Wings',
     'slug': 'detroit-red-wings',
     'nhl_abbreviation': 'DET',
     'nst_abbreviation': 'DET',
    },
    'NSH': {
     'dk_abbreviation': 'NSH',
     'dk_team_id': 4980,
     'nhl_id': 18,
     'name': 'Nashville Predators',
     'slug': 'nashville-predators',
     'nhl_abbreviation': 'NSH',
     'nst_abbreviation': 'NSH',
    },
    'STL': {
     'dk_abbreviation': 'STL',
     'dk_team_id': 4972,
     'nhl_id': 19,
     'name': 'St. Louis Blues',
     'slug': 'st-louis-blues',
     'nhl_abbreviation': 'STL',
     'nst_abbreviation': 'STL',
    },
    'CGY': {
     'dk_abbreviation': 'CGY',
     'dk_team_id': 4956,
     'nhl_id': 20,
     'name': 'Calgary Flames',
     'slug': 'calgary-flames',
     'nhl_abbreviation': 'CGY',
     'nst_abbreviation': 'CGY',
    },
    'COL': {
     'dk_abbreviation': 'COL',
     'dk_team_id': 4970,
     'nhl_id': 21,
     'name': 'Colorado Avalanche',
     'slug': 'colorado-avalanche',
     'nhl_abbreviation': 'COL',
     'nst_abbreviation': 'COL',
    },
    'EDM': {
     'dk_abbreviation': 'EDM',
     'dk_team_id': 4959,
     'nhl_id': 22,
     'name': 'Edmonton Oilers',
     'slug': 'edmonton-oilers',
     'nhl_abbreviation': 'EDM',
     'nst_abbreviation': 'EDM',
    },
    'VAN': {
     'dk_abbreviation': 'VAN',
     'dk_team_id': 4975,
     'nhl_id': 23,
     'name': 'Vancouver Canucks',
     'slug': 'vancouver-canucks',
     'nhl_abbreviation': 'VAN',
     'nst_abbreviation': 'VAN',
    },
    'ANA': {
     'dk_abbreviation': 'ANH',
     'dk_team_id': 4978,
     'nhl_id': 24,
     'name': 'Anaheim Ducks',
     'slug': 'anaheim-ducks',
     'nhl_abbreviation': 'ANA',
     'nst_abbreviation': 'ANA',
    },
    'DAL': {
     'dk_abbreviation': 'DAL',
     'dk_team_id': 0,
     'nhl_id': 25,
     'name': 'Dallas Stars',
     'slug': 'dallas-stars',
     'nhl_abbreviation': 'DAL',
     'nst_abbreviation': 'DAL',
    },
    'LAK': {
     'dk_abbreviation': 'LA',
     'dk_team_id': 4961,
     'nhl_id': 26,
     'name': 'Los Angeles Kings',
     'slug': 'los-angeles-kings',
     'nhl_abbreviation': 'LAK',
     'nst_abbreviation': 'LAK',
    },
    'SJS': {
     'dk_abbreviation': 'SJ',
     'dk_team_id': 4971,
     'nhl_id': 28,
     'name': 'San Jose Sharks',
     'slug': 'san-jose-sharks',
     'nhl_abbreviation': 'SJS',
     'nst_abbreviation': 'SJS',
    },
    'CBJ': {
     'dk_abbreviation': 'CLS',
     'dk_team_id': 4982,
     'nhl_id': 29,
     'name': 'Columbus Blue Jackets',
     'slug': 'columbus-blue-jackets',
     'nhl_abbreviation': 'CBJ',
     'nst_abbreviation': 'CBJ',
    },
    'MIN': {
     'dk_abbreviation': 'MIN',
     'dk_team_id': 4983,
     'nhl_id': 30,
     'name': 'Minnesota Wild',
     'slug': 'minnesota-wild',
     'nhl_abbreviation': 'MIN',
     'nst_abbreviation': 'MIN',
    },
    'WPG': {
     'dk_abbreviation': 'WPG',
     'dk_team_id': 4981,
     'nhl_id': 52,
     'name': 'Winnipeg Jets',
     'slug': 'winnipeg-jets',
     'nhl_abbreviation': 'WPG',
     'nst_abbreviation': 'WPG',
    },
    'ARI': {
     'dk_abbreviation': 'ARI',
     'dk_team_id': 4977,
     'nhl_id': 53,
     'name': 'Arizona Coyotes',
     'slug': 'arizona-coyotes',
     'nhl_abbreviation': 'ARI',
     'nst_abbreviation': 'ARI',
    },
    'VGK': {
     'dk_abbreviation': 'VGK',
     'dk_team_id': 58462,
     'nhl_id': 54,
     'name': 'Vegas Golden Knights',
     'slug': 'vegas-golden-knights',
     'nhl_abbreviation': 'VGK',
     'nst_abbreviation': 'VGK',
    }
}




#
