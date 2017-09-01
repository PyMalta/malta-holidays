from datetime import datetime, timedelta
import itertools

from bs4 import BeautifulSoup
from icalendar import Calendar, Event
import requests


def scrape_holidays(year=None):
    holidays = []
    year_path = f'{year}-dates/' if year else ''
    url = f'https://publicholidays.com.mt/{year_path}'
    res = requests.get(url)
    root = BeautifulSoup(res.text, "html.parser")
    events = root.find_all('tr', class_='vevent')
    for event in events:
        date_string = event.find('time').attrs['datetime']
        date = datetime.strptime(date_string, '%Y-%m-%d').date()

        name = event.find(class_='summary').text
        holidays.append(dict(date=date, name=name))
    return holidays


def create_icsv(holidays, filename='malta-holidays.ics'):
    # print(holidays)

    cal = Calendar()
    cal.add('prodid', '-//Malta Public Holidays//github.com/PyMalta/malta-holidays//EN')
    cal.add('version', '2.0')
    for holiday in holidays:
        event = Event()
        event.add('summary', holiday['name'])
        event.add('dtstart', holiday['date'])
        event.add('dtend', holiday['date'] + timedelta(days=1))
        event.add('dtstamp', datetime.now())
        cal.add_component(event)

    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

    return filename


if __name__ == '__main__':
    years = [None, 2018, 2019]
    holidays = itertools.chain(*[scrape_holidays(year) for year in years])
    print(holidays)
    filename = create_icsv(holidays)
    print(f'Created ICS {filename}')
