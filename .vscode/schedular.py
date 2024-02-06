import schedule
import time

jlist=[]
jobs=int(input("how many jobs you want to do in day?"))
for i in jobs :
    jlist.append
def job():
    print("Hello, World!")

schedule.every(10).seconds.do(job)
schedule.every(1).minute.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)