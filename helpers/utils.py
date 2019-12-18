import requests, os
from datetime import date, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
from urls import nst_team_url


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
def return_date(todays_date):
    start_date = todays_date - timedelta(days=14)
    return start_date
