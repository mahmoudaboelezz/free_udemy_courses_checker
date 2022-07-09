import requests
import json
import os
import time
from bs4 import BeautifulSoup
class prayer():
    url = 'https://www.islamicfinder.org/prayer-times/'
    response = requests.get(url)
    def prayer_times():
    # scrap data from website and save it in a json file 
        soup = BeautifulSoup(prayer.response.text, 'html.parser')
        prayer_time = soup.find_all('span', class_='prayertime')
        prayer_name = soup.find_all('span', class_='prayername')
        dict_prayer = {}
        dict_prayer['Fajr'] = prayer_time[0].text
        dict_prayer['Sunrise'] = prayer_time[1].text
        dict_prayer['Dhuhr'] = prayer_time[2].text
        dict_prayer['Asr'] = prayer_time[3].text
        dict_prayer['Maghrib'] = prayer_time[4].text
        dict_prayer['Isha'] = prayer_time[5].text
        return dict_prayer
    def next_prayer_time():
        soup1 = BeautifulSoup(prayer.response.text, 'html.parser')
        next_prayer_time = soup1.find('div', class_='pt-active')
        print(next_prayer_time)
        # text = next_prayer_time.find('span', class_='prayertime')
        # print(text)
        return next_prayer_time