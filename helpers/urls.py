# Urls for use in all clients


#-------------------------------------------------------#
NHL_BASE = 'nhl.com'
NHL_SHIFTS = '/stats/rest/shiftcharts?cayenneExp=gameId={}'
#-------------------------------------------------------#
NHL_API_BASE = 'https://statsapi.web.nhl.com/api/v1'
NHL_API_TEAMS = '/teams'
NHL_API_SCHEDULE = '/schedule'
#-------------------------------------------------------#
DK_API_BASE = 'https://api.draftkings.com'
DK_DRAFTGROUPS_PATH = '/draftgroups/v1/'
#-------------------------------------------------------#
NST_BASE = 'http://www.naturalstattrick.com'
NST_TEAM_TABLE = '/teamtable.php?fromseason=20192020&thruseason=20192020&stype=2&sit={}&score={}&rate=y&team=all&loc={}&gpf={}&fd={}&td={}'
#-------------------------------------------------------#
LWL_BASE = 'https://leftwinglock.com'
LWL_LOGIN = '/forum/index.php?login/login'
LWL_LINES_BASE = '/line-combinations'
LWL_TEAM_PARAM = '/{TEAM_SLUG}/?team={TEAM_SLUG}&strength={STRENGTH}&gametype={GAMETYPE}'
#-------------------------------------------------------#


# --------------------- #
#    Draftkings URLs    #
# --------------------- #
def upcoming_draft_groups():
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
    url = "{DK_API_BASE}{DK_DRAFTGROUPS_PATH}draftgroups/{draft_group_id}/draftables".format(
        DK_API_BASE = DK_API_BASE,
        DK_DRAFTGROUPS_PATH = DK_DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )
    return url



# --------------------------- #
#    NaturalStatTrick URLs    #
# --------------------------- #
def nst_team_url(sit, score, loc, gpf, start_date, end_date):
    url = "{NST_BASE}{NST_TEAM_TABLE}".format(
        NST_BASE = NST_BASE,
        NST_TEAM_TABLE = NST_TEAM_TABLE
    )
    return url.format(sit, score, loc, gpf, start_date, end_date)



# ------------------ #
#    NHL API URLs    #
# ------------------ #
def schedule_url():
    return "{NHL_API_BASE}{NHL_API_SCHEDULE}".format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_SCHEDULE = NHL_API_SCHEDULE
    )

def shiftcharts_url(gameId):
    url = '{NHL_BASE}{NHL_SHIFTS}'.format(
        NHL_BASE = NHL_BASE,
        NHL_SHIFTS = NHL_SHIFTS
    )
    return url.format(gameId)

def teams_url():
    return '{NHL_API_BASE}{NHL_API_TEAMS}'.format(
        NHL_API_BASE = NHL_API_BASE,
        NHL_API_TEAMS = NHL_API_TEAMS
    )



# ----------------------- #
#    LeftWingLock URLs    #
# ----------------------- #
def lwl_login_url():
    return '{LWL_BASE}{LWL_LOGIN}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LOGIN = LWL_LOGIN
    )


def lwl_lines_url(TEAM_SLUG, STRENGTH, GAMETYPE):
    url = '{LWL_BASE}{LWL_LINES_BASE}{LWL_TEAM_PARAM}'.format(
        LWL_BASE = LWL_BASE,
        LWL_LINES_BASE = LWL_LINES_BASE,
        LWL_TEAM_PARAM = LWL_TEAM_PARAM
    )
    return url.format(
        TEAM_SLUG = TEAM_SLUG,
        STRENGTH = STRENGTH,
        GAMETYPE = GAMETYPE
    )







##################################################
