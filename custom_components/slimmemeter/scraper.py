import os
import mechanize
import xlrd
from datetime import datetime, timedelta, time
import time as tm

def scrape(range, date, email, password, filename, type):
    """
    Scrapes data from slimmemeterportal.nl
    """

    # Open browser
    br = mechanize.Browser()
    br.open('https://slimmemeterportal.nl/login')

    # Fill out login form
    br.select_form(nr=0)
    br["user_session[email]"] = email
    br["user_session[password]"] = password
    br.submit()

    # Download the XLS file with
    url = 'https://slimmemeterportal.nl/cust/consumption/chart.xls?commodity=' + type +'&contract_id=293767633&datatype=consumption&range=' + str(range) + '&timeslot_start=' + str(date) + '.xls'
    r = br.retrieve(url, filename + '.xls')

#Power
def power_yesterday(email, password):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = midnight - timedelta(days=1)
    timestamp = tm.mktime(yesterday_midnight.timetuple())
    scrape(86400, timestamp, str(email), str(password), "power_yesterday", "power")

def power_month(email, password):
    midnight = datetime.combine(datetime.today().replace(day=1), time.min)
    timestamp = tm.mktime(midnight.timetuple())
    scrape(2629746, timestamp, str(email), str(password), "power_month", "power")

def power_year(email, password):
    midnight = datetime.combine(datetime(datetime.today().year, 1, 1), time.min)
    timestamp = tm.mktime(midnight.timetuple())
    scrape(31556952, timestamp, str(email), str(password), "power_year", "power")

#Gas
def gas_yesterday(email, password):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = midnight - timedelta(days=1)
    timestamp = tm.mktime(yesterday_midnight.timetuple())
    scrape(86400, timestamp, str(email), str(password), "power_yesterday", "gas")

def gas_month(email, password):
    midnight = datetime.combine(datetime.today().replace(day=1), time.min)
    timestamp = tm.mktime(midnight.timetuple())
    scrape(2629746, timestamp, str(email), str(password), "power_month", "gas")

def gas_year(email, password):
    midnight = datetime.combine(datetime(datetime.today().year, 1, 1), time.min)
    timestamp = tm.mktime(midnight.timetuple())
    scrape(31556952, timestamp, str(email), str(password), "power_year", "ga")
gas_month("demo@slimmemeterportal.nl", "demo123")
