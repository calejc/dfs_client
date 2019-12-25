import sys
sys.path.append('..')
import data, helpers.utils as utils, helpers.urls as urls, datetime as dt, pandas as pd
from bs4 import BeautifulSoup


tmp = utils.scrape_nst(
    data.nst_sit.EVEN_STRENGTH.value,
    data.nst_score.ALL_SCORES.value,
    data.nst_loc.HOME_AND_AWAY.value,
    data.nst_gpf.LAST_TEN.value,
    utils.return_date(dt.date.today(), 14),
    dt.date.today()
)
# data = []
# columns = []
# table = tmp.find('table', {'id': 'teams'})
# tbody = table.find('tbody')
# for tr in tbody.find_all('tr'):
#     for th in tr.find_all('th'):
#         print(th)
#         columns.append(th.text)
#     tmp = []
#     for td in tr.find_all('td'):
#         tmp.append(td.text)
#     data.append(tmp)
# df = pd.DataFrame(data, columns=columns)
# print(df)
# print(columns)


def advanced(sit, score, loc, gpf, start_date, end_date):
    tmp = utils.scrape_nst(
        sit,
        score,
        loc,
        gpf,
        start_date,
        end_date
    )

    data_list = []
    table = tmp.find('table', {'id': 'teams'})
    tbody = table.find('tbody')
    for tr in tbody.find_all('tr'):
        team = [td for td in tr.find_all('td')[1]]
        gp = [td for td in tr.find_all('td')[2]]
        cf60 = [td for td in tr.find_all('td')[10]]
        ca60 = [td for td in tr.find_all('td')[11]]
        cfRate = [td for td in tr.find_all('td')[12]]
        ff60 = [td for td in tr.find_all('td')[13]]
        fa60 = [td for td in tr.find_all('td')[14]]
        faRate = [td for td in tr.find_all('td')[15]]
        sf60 = [td for td in tr.find_all('td')[16]]
        sa60 = [td for td in tr.find_all('td')[17]]
        sfRate = [td for td in tr.find_all('td')[18]]
        gf60 = [td for td in tr.find_all('td')[19]]
        ga60 = [td for td in tr.find_all('td')[20]]
        gfRate = [td for td in tr.find_all('td')[21]]
        xgf60 = [td for td in tr.find_all('td')[22]]
        xga60 = [td for td in tr.find_all('td')[23]]
        scf60 = [td for td in tr.find_all('td')[25]]
        sca60 = [td for td in tr.find_all('td')[26]]
        scfRate = [td for td in tr.find_all('td')[27]]
        scgf60 = [td for td in tr.find_all('td')[31]]
        scga60 = [td for td in tr.find_all('td')[32]]
        scgfRate = [td for td in tr.find_all('td')[33]]
        scshRate = [td for td in tr.find_all('td')[34]]
        scsvRate = [td for td in tr.find_all('td')[35]]
        hdcf60 = [td for td in tr.find_all('td')[36]]
        hdca60 = [td for td in tr.find_all('td')[37]]
        hdcfRate = [td for td in tr.find_all('td')[38]]
        hdgf60 = [td for td in tr.find_all('td')[42]]
        hdga60 = [td for td in tr.find_all('td')[43]]
        hdgfRate = [td for td in tr.find_all('td')[44]]
        hdshRate = [td for td in tr.find_all('td')[45]]
        hdsvRate = [td for td in tr.find_all('td')[46]]
        shRate = [td for td in tr.find_all('td')[69]]
        svRate = [td for td in tr.find_all('td')[70]]
        pdo = [td for td in tr.find_all('td')[71]]

        new_data = team + gp + cf60 + ca60 + cfRate + ff60 + fa60 + faRate + sf60 + sa60 + sfRate + gf60 + ga60 + gfRate + xgf60 + xga60 + scf60 + sca60 + scfRate + scgf60 + scga60 + scgfRate + scshRate + scsvRate + hdcf60 + hdca60 + hdcfRate + hdgf60 + hdga60 + hdgfRate + hdshRate + hdsvRate + shRate + svRate + pdo
        data_list.append(new_data)
    df = pd.DataFrame(data_list, columns = ['team', 'gp', 'cf/60', 'ca/60', 'cf%', 'ff/60', 'fa/60', 'ff%', 'sf/60', 'sa/60', 'sf%', 'gf/60', 'ga/60', 'gf%', 'xgf/60', 'xga/60', 'scf/60', 'sca/60', 'scf%', 'scgf/60', 'scga/60', 'scgf%', 'scsh%', 'scsv%', 'hdcf/60', 'hdca/60', 'hdcf%', 'hdgf/60', 'hdga/60', 'hdgf%', 'hdsh%', 'hdsv%', 'sh%', 'sv%', 'pdo'])
    return df
# df = advanced()
# df1 = pd.DataFrame.from_dict(data.TEAM_DATA, orient='index')
# print(df1)
