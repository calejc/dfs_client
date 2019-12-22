import requests, json, sys
sys.path.append('..')
import data, datetime
import helpers.urls as urls
import helpers.utils as utils




#########################################
##    Crawl through team's schedule    ##
#########################################


# Maybe build some sort of database (maybe just a giant dict) with all stats from all games.

season_start_date = '2019-10-02'


today = datetime.date.today()
two_weeks = utils.return_date(today, 21)
url = urls.teams_schedule_url(data.TEAM_DATA['LAK']['nhl_id'], two_weeks, str(today))
print(url)




#
