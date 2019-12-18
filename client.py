import urls, data, utils
import pandas as pd
import numpy as np
from dk_client import get_slate
# from lwl_client import get_lines



# -------------------------------- #
#    STILL NEED POWERPLAY STATS    #
# -------------------------------- #



# ----------------------------------------- #
#    Import all modules and run from here   #
# ----------------------------------------- #


# NHL sportId is 3, and 'Classic' is preferred gametype for this model. Change these inputs to use the draftkings client for other sports or other gametypes.
sportId = 3
gameType = 'Classic'

slate = get_slate(sportId, gameType)
print(slate.keys())
