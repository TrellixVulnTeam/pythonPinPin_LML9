from datetime import datetime
dates = []
dates.append('1 Jun 2005')
dates.append('28 Aug 1999')
from datetime import datetime
for d in dates:
    date = datetime.strptime(d, '%d %b %Y')
    print (type(date))
    print (date)