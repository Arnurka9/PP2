import datetime

today = datetime.datetime.now()
beforeToday = today - datetime.timedelta(days=5)

print(beforeToday)