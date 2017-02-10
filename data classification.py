import csv
with open("Summer Olympic medallists 1896 to 2008.csv",newline='') as rawdata:
    with open("eventType.csv") as events:
        events=csv.reader(events,delimiter='|')
        rows=[row for row in events]
        eventlist=rows[0]
        #eventlist=eventlist.split(',')
        reader=csv.DictReader(rawdata)
        for event in eventlist:
            with open('%s_data.csv'%event,'w',delimiter=','):
                pass
