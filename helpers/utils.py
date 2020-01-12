import requests, os, sys, math
sys.path.append("..")
import datetime as dt
from selenium import webdriver
from bs4 import BeautifulSoup
from helpers.urls import nst_team_url


def drive(url):
    driver = webdriver.Firefox(service_log_path=os.devnull)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    return soup

def scrape(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def scrape_nst(sit, score, loc, gpf, start_date, end_date):
    url = nst_team_url(sit, score, loc, gpf, start_date, end_date)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def scrape_json(url):
    response = requests.get(url).json()
    return response

def parse_link(link):
    to_replace = ['=', '%20', '&']
    for item in to_replace:
        link = link.replace("{}".format(item), " ", 1)
    link = link.split()
    name = link[1] + " " + link[2]
    return name.lower().replace(" ", "-")

def return_slug(team):
    team = team.replace('.', '')
    team = team.replace(' ', '-')
    return team.lower()

# Must pass in todays_date as a datetime.date object
def return_date(todays_date, days):
    start_date = todays_date - dt.timedelta(days=days)
    return start_date

# Convert decimal odds to traditional american odds
def convert_odds(decimal):
    american_odds = 0
    if decimal >= 2:
        american_odds = (decimal - 1) * 100
    elif decimal <= 2:
        american_odds = (-100)/(decimal - 1)
    return round(american_odds, 0)

# Return implied team totals for moneyline odds
# Using Bill James' Pythagorean Expectation
def team_total(odds, game_total):
    if odds < 0:
        wp = odds/(odds-100)
    elif odds > 0:
        wp = 100/(odds+100)
    team_total = game_total / (((math.sqrt(1-wp))*(1 / math.sqrt(wp))) + 1)
    # team_total = game_total / ((((1-wp)**(1/1.927))*(1 / (wp**(1/1.927)))) + 1)
    return round(team_total, 2)

def spreads_team_total(spread, game_total):
    if spread < 0:
        tm_total = ((game_total - (-1 * spread)) / 2) + (-1 * spread)
    elif spread > 0:
        tm_total = (game_total - spread) / 2
    return round(tm_total, 2)

def return_alt(d, value, requested_alt):
    for k, v in d.items():
        if isinstance(v, dict):
            p = return_alt(v, value, requested_alt)
            if p:
                return d[k][requested_alt]
        elif v == value:
            return k

def strip_datetime(value):
    # tmp = dt.replace('T', '')[:10]
    tmp = value.replace('T', ' ')[:19]
    return dt.datetime.strptime(tmp, '%Y-%m-%d %H:%M:%S')

def strip_date(date):
    return date.replace('-', '')[2:]

def game_ids(sportId, date, counter):
    y = strip_date(str(date))
    if counter < 10:
        x = '0' + str(counter)
    else:
        x = str(counter)
    id = str(sportId) + y + x
    return id

# Check if a value exists in dict. Using to get home-and-homes
def check_value(data, value):
    tmp = []
    for ele in data.values():
        if isinstance(ele,dict):
            for k, v in ele.items():
               tmp.append(v)
    if value in tmp:
        return True
    else:
        return False

# To find opponent
def check(data, value, team):
    for key in data.values():
        if key['game_id'] == value and key['team'] != team:
            return key['team']


# Search dict for certain value,
# Returning the key for that key-value pair
def return_key(data, value):
    for k, v in data.items():
        if v == value:
            return k
