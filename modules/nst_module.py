import sys
sys.path.append('..')
import helpers.utils as utils
import helpers.urls as urls
import data
# from data import nst_sit, nst_score, nst_rate, nst_loc, nst_gpf, nst_teams
# from utils import scrape_nst, scrape
from bs4 import BeautifulSoup
import pandas as pd


url = urls.nst_team_url(
    nst_sit.EVEN_STRENGTH.value,
    nst_score.ALL_SCORES.value,
    nst_loc.HOME_AND_AWAY.value,
    nst_gpf.LAST_TEN.value,
    '',
    ''
)
# print(url)
data = scrape(url)

tmp = scrape_nst(
    nst_sit.EVEN_STRENGTH.value,
    nst_score.ALL_SCORES.value,
    nst_loc.HOME_AND_AWAY.value,
    nst_gpf.LAST_TEN.value,
    "",
    ""
)
