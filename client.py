import sys, os, data, pandas as pd, numpy as np, modules.dk_module as dk, modules.lwl_module as lwl, modules.nst_module as nst, modules.vegas_module as vegas, helpers.utils as utils, helpers.urls as urls
from dotenv import load_dotenv
load_dotenv()



# print(os.getenv('LWL_USER'))

# --------------- #
#    .env keys    #
# --------------- #
#  LWL_USER       #
#  LWL_PASS       #
#  OP_API_KEY     #
# --------------- #


# -------------------------------- #
#    STILL NEED POWERPLAY STATS    #
# -------------------------------- #



# ----------------------------------------- #
#    Import all modules and run from here   #
# ----------------------------------------- #


# NHL sportId is 3, and 'Classic' is preferred gametype for this model. Change these inputs to use the draftkings client for other sports or other gametypes.
sportId = 3
gameType = 'Classic'


# ------------------------------------------------------------ #
# ------------------------------------------------------------ #
teams = []
df_dk = dk.get_slate(3, 'Classic')
df_odds = vegas.return_tm_totals('icehockey_nhl', 'eu', 'h2h')
df_nst = nst.advanced()
print(df_nst)
df_slate = pd.merge(df_dk, df_odds, on='team', how='left')
df_slate = pd.merge(df_slate, df_nst)
print(df_slate)
for team in df_slate['team']:
    teams.append(team)
# ------------------------------------------------------------ #
# ------------------------------------------------------------ #
