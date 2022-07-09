def prayer_time():
    import requests
    import json
    import os
    import time
    from bs4 import BeautifulSoup
    # scrap data from website and save it in a json file 
    url = 'https://www.islamicfinder.org/prayer-times/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    prayer_time = soup.find_all('span', class_='prayertime')
    prayer_name = soup.find_all('span', class_='prayername')
    # print(f'{prayer_name[0].text} : {prayer_time[0].text}')
    dict_prayer = {}
    dict_prayer['Fajr'] = prayer_time[0].text
    dict_prayer['Sunrise'] = prayer_time[1].text
    dict_prayer['Dhuhr'] = prayer_time[2].text
    dict_prayer['Asr'] = prayer_time[3].text
    dict_prayer['Maghrib'] = prayer_time[4].text
    dict_prayer['Isha'] = prayer_time[5].text
    return dict_prayer
    
    # data = []
    # for row in rows:
    #     cols = row.find_all('td')
    #     cols = [ele.text.strip() for ele in cols]
    #     data.append([ele for ele in cols if ele])
    # # save data in a json file 
    # with open('data.json', 'w') as f:
    #     json.dump(data, f, indent=2)
    # # print data
    # for i in data:
    #     print(i)
    # # print data in a csv file 
    # with open('data.csv', 'w') as f:
    #     for i in data:
    #         f.write(','.join(i) + '\n')
    # # print data in a txt file 
    # with open('data.txt', 'w') as f:
    #     for i in data:
    #         f.write('\t'.join(i) + '\n')
    # # print data in a html file 
    # with open('data.html', 'w') as f:
    #     f.write('<table>')
    #     for i in data:
    #         f.write('<tr>')
    #         for j in i:
    #             f.write('<td>' + j + '</td>')
    #         f.write('</tr>')
    #     f.write('</table>')
    # # print data in a xlsx file 
    # import xlsxwriter
    # workbook = xlsxwriter.Workbook('data.xlsx')
    # worksheet = workbook.add_worksheet
prayer_time()