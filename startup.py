# create a class to get news from newsapi.org
class startup:
    def getnews():
        import requests
        import json
        newsapi = 'https://newsapi.org/v2/top-headlines?country=eg&apiKey=68cd57c00bc1489a81e7c9704d23434a'
        response = requests.get(newsapi)
        news_json = response.json()
        news_json = json.dumps(news_json, indent=2)
        news_dict = json.loads(news_json)
        news_list = news_dict['articles']
        for i in news_list:
            print(i['title'])
    
    def getweather():
        import requests
        import json
        weatherapi = 'https://api.openweathermap.org/data/2.5/weather?q=cairo&appid=ef478ec1ef2c29605c0f369a6b1bf1e1'
        response = requests.get(weatherapi)
        weather_json = response.json()
        weather_json = json.dumps(weather_json, indent=2)
        weather_dict = json.loads(weather_json)
        weather_list = weather_dict['weather']
        for i in weather_list:
            print(i['description'])
        temp_list = weather_dict['main']
        convertkelvintocelsius = (temp_list['temp'] - 273.15)
        print("{:.2f}".format(convertkelvintocelsius))

    
    
    # scrap data from website and save it in a json file 
    def scrapdata():
        import requests
        import json
        import os
        import time
        from bs4 import BeautifulSoup
        # scrap data from website and save it in a json file 
        url = 'https://egrates.com/en/gold-price'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='currency')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        # save data in a json file 
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)
        # print data
        for i in data:
            print(i)
        # print data in a csv file 
        with open('data.csv', 'w') as f:
            for i in data:
                f.write(','.join(i) + '\n')
        # print data in a txt file 
        with open('data.txt', 'w') as f:
            for i in data:
                f.write('\t'.join(i) + '\n')
        # print data in a html file 
        with open('data.html', 'w') as f:
            f.write('<table>')
            for i in data:
                f.write('<tr>')
                for j in i:
                    f.write('<td>' + j + '</td>')
                f.write('</tr>')
            f.write('</table>')
        # print data in a xlsx file 
        import xlsxwriter
        workbook = xlsxwriter.Workbook('data.xlsx')
        worksheet = workbook.add_worksheet

    scrapdata()
    getnews()
    getweather()
# create a function to get yesterday's date
    def getyesterdaydate():
        import datetime
        yesterday = datetime.date.today() - datetime.timedelta(1)
        print(yesterday)
        

# create a function to get prayer times
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
    table = soup.find('table', id='prayer-times')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    # save data in a json file 
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    # print data
    for i in data:
        print(i)
    # print data in a csv file 
    with open('data.csv', 'w') as f:
        for i in data:
            f.write(','.join(i) + '\n')
    # print data in a txt file 
    with open('data.txt', 'w') as f:
        for i in data:
            f.write('\t'.join(i) + '\n')
    # print data in a html file 
    with open('data.html', 'w') as f:
        f.write('<table>')
        for i in data:
            f.write('<tr>')
            for j in i:
                f.write('<td>' + j + '</td>')
            f.write('</tr>')
        f.write('</table>')
    # print data in a xlsx file 
    import xlsxwriter
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet
# prayer_time()


# create a function to get the dollar vs egp rate 
    def getdollarvsegp():
        import requests
        import json
        dollarvsegpapi = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EGP&apikey=Z1QJNQQZQJNQQZQJ'
        response = requests.get(dollarvsegpapi)
        dollarvsegp_json = response.json()
        dollarvsegp_json = json.dumps(dollarvsegp_json, indent=2)
        dollarvsegp_dict = json.loads(dollarvsegp_json)
        dollarvsegp_list = dollarvsegp_dict['Realtime Currency Exchange Rate']
        print(dollarvsegp_list['5. Exchange Rate'])
    getdollarvsegp()
    
