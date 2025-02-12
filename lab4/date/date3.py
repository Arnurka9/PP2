import datetime

today = datetime.datetime.now()

clean_date = today.replace(microsecond=0)
print(clean_date)
