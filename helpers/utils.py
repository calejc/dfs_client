import requests, os, sys, math
sys.path.append("..")
from datetime import date, timedelta
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
    start_date = todays_date - timedelta(days=days)
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
def team_total(odds, game_total):
    # formula from squirrelPatrol on RG forum
    # team_total = (game_total/4) + ((wp*game_total)/2)
    if odds < 0:
        wp = odds/(odds-100)
    elif odds > 0:
        wp = 100/(odds+100)
    team_total = game_total / (((math.sqrt(1-wp))*(1 / math.sqrt(wp))) + 1)
    return round(team_total, 2)

def nfl_team_total(spread, game_total):
    if spread < 0:
        tm_total = ((game_total - (-1 * spread)) / 2) + (-1 * spread)
    elif spread > 0:
        tm_total = (game_total - spread) / 2
    return round(tm_total, 2)
