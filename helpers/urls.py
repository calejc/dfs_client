import sys, os
sys.path.append('..')
from dotenv import load_dotenv
load_dotenv()


# Urls for use in all clients




#-------------------------------------------------------#
NHL_BASE = 'nhl.com'
NHL_SHIFTS = '/stats/rest/shiftcharts?cayenneExp=gameId={GAME_ID}'
#-------------------------------------------------------#
NHL_API_BASE = 'https://statsapi.web.nhl.com/api/v1'
NHL_API_TEAMS = '/teams'
NHL_API_SCHEDULE = '/schedule?teamId={TEAM_ID}&startDate={START_DATE}&endDate={END_DATE}'
NHL_API_TEAM_SCHEDULE = '?teamId={TEAM_ID}&startDate={START_DATE}&endDate={END_DATE}'
#-------------------------------------------------------#
DK_API_BASE = 'https://api.draftkings.com'
DK_DRAFTGROUPS_PATH = '/draftgroups/v1/'
#-------------------------------------------------------#
NST_BASE = 'http://www.naturalstattrick.com'
NST_TEAM_TABLE = '/teamtable.php?fromseason=20192020&thruseason=20192020&stype=2&sit={SITUATION}&score={SCORE}&rate=y&team=all&loc={LOCATION}&gpf={GPF}&fd={START_DATE}&td={END_DATE}'
#-------------------------------------------------------#
LWL_BASE = 'https://leftwinglock.com'
LWL_LOGIN = '/forum/index.php?login/login'
LWL_LINES_BASE = '/line-combinations'
LWL_TEAM_PARAM = '/{TEAM_SLUG}/?team={TEAM_SLUG}&strength={STRENGTH}&gametype={GAMETYPE}'
#-------------------------------------------------------#
ODDS_API_BASE = 'https://api.the-odds-api.com/v3'
ODDS_API_SPORTS = '/sports/?apiKey={API_KEY}&all=1'
ODDS_API_ODDS = '/odds/?apiKey={API_KEY}&sport={SPORT}&region={REGION}&mkt={MARKET}'
#-------------------------------------------------------#


# --------------------- #
#    Draftkings URLs    #
# --------------------- #
def upcoming_draft_groups_url():
    return '{DK_API_BASE}{DK_DRAFTGROUPS_PATH}'.format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH
    )

def draft_group_url(draft_group_id):
    return "{DK_API_BASE}{DK_DRAFTGROUPS_PATH}/{draft_group_id}".format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )

def draftables_url(draft_group_id):
    return "{DK_API_BASE}{DK_DRAFTGROUPS_PATH}draftgroups/{draft_group_id}/draftables".format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )


# --------------------------- #
#    NaturalStatTrick URLs    #
# --------------------------- #
def nst_team_url(sit, score, loc, gpf, start_date, end_date):
    url = "{NST_BASE}{NST_TEAM_TABLE}".format(
        NST_BASE = NST_BASE,
        NST_TEAM_TABLE = NST_TEAM_TABLE
    )
    return url.format(
        SITUATION = sit,
        SCORE = score,
        LOCATION = loc,
        GPF = gpf,
        START_DATE = start_date,
        END_DATE = end_date
    )



# ------------------ #
#    NHL API URLs    #
# ------------------ #
def schedule_url(teamId, startDate, endDate):
    url = "{NHL_API_BASE}{NHL_API_SCHEDULE}".format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_SCHEDULE = NHL_API_SCHEDULE
    )
    return url.format(
        TEAM_ID = teamId,
        START_DATE = startDate,
        END_DATE = endDate
    )

def shiftcharts_url(gameId):
    url = '{NHL_BASE}{NHL_SHIFTS}'.format(
        NHL_BASE = NHL_BASE,
        NHL_SHIFTS = NHL_SHIFTS
    )
    return url.format(
        GAME_ID = gameId
    )

def teams_url():
    return '{NHL_API_BASE}{NHL_API_TEAMS}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_TEAMS = NHL_API_TEAMS
    )

def teams_schedule_url(teamId, startDate, endDate):
    url = '{NHL_API_BASE}{NHL_API_SCHEDULE}{NHL_API_TEAM_SCHEDULE}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_SCHEDULE = NHL_API_SCHEDULE,
        NHL_API_TEAM_SCHEDULE = NHL_API_TEAM_SCHEDULE
    )
    return url.format(
        TEAM_ID = teamId,
        START_DATE = startDate,
        END_DATE = endDate
    )


# ----------------------- #
#    LeftWingLock URLs    #
# ----------------------- #
def lwl_login_url():
    return '{LWL_BASE}{LWL_LOGIN}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LOGIN = LWL_LOGIN
    )


def lwl_lines_url(team_slug, strength, gametype):
    url = '{LWL_BASE}{LWL_LINES_BASE}{LWL_TEAM_PARAM}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LINES_BASE = LWL_LINES_BASE,
        LWL_TEAM_PARAM = LWL_TEAM_PARAM
    )
    return url.format(
        TEAM_SLUG = team_slug,
        STRENGTH = strength,
        GAMETYPE = gametype
    )


# ------------------- #
#    Odds API URLs    #
# ------------------- #
def get_odds_url(sport, region, market):
    url = '{ODDS_API_BASE}{ODDS_API_ODDS}'.format(
        ODDS_API_BASE = ODDS_API_BASE,
        ODDS_API_ODDS = ODDS_API_ODDS
    )
    return url.format(
        API_KEY = os.getenv('OP_API_KEY'),
        SPORT = sport,
        REGION = region,
        MARKET = market
    )





##################################################
