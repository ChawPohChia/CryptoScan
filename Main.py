#Project Objective: CryptoScan
#Trying to scan poloniex all available coins past scanning_hours behaviour and ranked them in order.
#In order to capture continuous price movement.

from ScanAndGenerateReport import ScanAndReport
import schedule
import time

ScanAndReport()
schedule.every(6).hours.do(ScanAndReport)

while True:
    schedule.run_pending()
    time.sleep(1)

