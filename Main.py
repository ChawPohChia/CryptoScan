#Project Objective: CryptoScan
#Trying to scan poloniex all available coins past scanning_hours behaviour and ranked them in order.
#In order to capture continuous price movement.

import requests
import time
from ToSendEmail import sendEmail

current_time = int(time.time())
print("Current epoch time is: " + str(current_time))

Scanning_window_length=72 #48=48hours
secsPerHour=3600
interval=str(7200)
startPeriod = str(current_time - (Scanning_window_length-1) * secsPerHour)
endPeriod = str(current_time) #take the end period as 1 hour ago
print("StartPeriod:"+startPeriod+"     "+"EndPeriod:"+endPeriod)

#Getting current price
currentPriceRequest = requests.get('https://poloniex.com/public?command=returnTicker') #This will return current time ticker status
currentPrice=currentPriceRequest.json()

allPairs=currentPrice.keys()
print("Total Pairs: "+str(len(allPairs)))


#Getting historical price
#The following will return a specified period of time, with the specified interval.
#example api query: https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1546300800&end=1546646400&period=14400
#tradingPair='BTC_XMR'
historicalPrice={}
WindowsGain={}

for pair in allPairs:  #Data Collection: collect all pairs price into (ETH_BTC:{1,2,3,4,5,,8,9,10,..24})
    apiQuery= 'https://poloniex.com/public?command=returnChartData&currencyPair='+pair+'&start='+startPeriod+'&end='+endPeriod+'&period='+interval
    chartDataRequest = requests.get(apiQuery)
    chartdata=chartDataRequest.json()
    historicalPrice[pair]=[];
    for i in reversed(range(len(chartdata))):
        historicalPrice[pair].append(chartdata[i]['close'])
        #print(str(chartdata[i]['date'])+':'+str(chartdata[i]['close']))
    #Generate Accumulate%
    gain=0
    for histPrice in historicalPrice[pair]:
        if(histPrice==0):
            continue;
        gain +=(historicalPrice[pair][0]-histPrice)/histPrice
    WindowsGain[pair] = gain

    print(pair+" end")

sortedWindowsGain={k: v for k, v in sorted(WindowsGain.items(), key=lambda item: item[1], reverse=True)}
#for item in sortedWindowsGain:
#    print(item+":"+str(sortedWindowsGain[item]))
sendEmail(sortedWindowsGain)



