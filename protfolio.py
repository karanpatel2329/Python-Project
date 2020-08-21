import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from hidden import header

convert='USD'

listings_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

a=header
request=requests.get(listings_url,headers=a)
#print(request)
res=request.json()
data=res['data']

ticker_url_pairs={}
for currency in data:
    symbol=currency['symbol']
    url=currency['id']
    ticker_url_pairs['symbol']=url

print()
print("\t\t\t\t\tPORTFOLIO")
print()

Protfolio=0.00
update=0

table=PrettyTable(['Assest','Amount Owned', 'Value','Price','1h','24h','7d'])

with open('p.txt') as inp:
    for line in inp:
        ticker,amount=line.split()
        ticker=ticker.upper()

        ticker_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        a=header
        request=requests.get(ticker_url,headers=a)
        #print(request)
        res=request.json()
        data=res['data']
        for a in data:
            if ticker==a['symbol']:
                currency = a['id']
                symbol = a['symbol']
                name = a['name']
                rank = a['cmc_rank']
                last_updated=a['last_updated']
                quotes=a['quote']['USD']
                hour_change = quotes['percent_change_1h']
                day_change = quotes['percent_change_24h']
                week_change = quotes['percent_change_7d']
                price= quotes['price']

                value= float(price)*float(amount)
                Protfolio=Protfolio+value
                value_string='{:,}'.format(round(value,2))


                if hour_change > 0:
                    hour_change = Back.GREEN + str(hour_change) + '%'+ Style.RESET_ALL
                else:
                    hour_change = Back.RED + str(hour_change) + '%'+ Style.RESET_ALL

                if day_change > 0:
                    day_change = Back.GREEN + str(day_change) + '%'+ Style.RESET_ALL
                else:
                    day_change = Back.RED + str(day_change) + '%'+ Style.RESET_ALL

                if week_change > 0:
                    week_change = Back.GREEN + str(week_change) + '%'+ Style.RESET_ALL
                else:
                    week_change = Back.RED + str(week_change) + '%'+ Style.RESET_ALL



                table.add_row([name,'('+symbol+')',
                    '$'+value_string,
                    '$'+str(price),
                    str(hour_change),
                    str(day_change),
                    str(week_change)
                ])
print(table)
print()
Protfolio_string='{:,}'.format(round(Protfolio,2))
#last_updated_string= datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
#$print(date)
da=last_updated.split('T')
date=da[0]
time=da[1]
time = time.split(':')
hour= time[0]
min = time[1]
Protfolio_string = Back.GREEN + str(Protfolio_string) + '%'+ Style.RESET_ALL
print("Total Portfolio Value is",Protfolio_string)
print("last_updated on ",date," at ",hour,':',min )
