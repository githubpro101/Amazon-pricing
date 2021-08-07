from requests_html import HTMLSession
import csv
import datetime

s=HTMLSession()

asins=[]

with open('asins.csv','r') as f:
    csv_reader=csv.reader(f)
    next(csv_reader, None)
    for row in csv_reader:
        asins.append(row[5])



for asin in asins:
    r=s.get(f'https://www.amazon.co.uk/dp/{asin}')
    r.html.render(sleep=1)
    try:
        price=r.html.find('#price_inside_buybox')[0].text.replace('£','').replace(',','').strip()
    except:
        price=r.html.find('#priceblock_ourprice')[0].text.replace('£','').replace(',','').strip()

    title=r.html.find('#productTitle')[0].text.strip()
    asin=asin
    date=datetime.datetime.today()
    print(asin,price,date)


