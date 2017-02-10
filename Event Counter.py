import csv
events=set()
discipline=set()
sport=set()
with open('Summer Olympic medallists 1896 to 2008.csv',newline='') as rawdata:
    with open('eventType.csv', 'w', newline='') as db:
        datareader=csv.DictReader(rawdata)
        database=csv.writer(db, delimiter=',')
        counter=0
        for row in datareader:
            events.add(row['Event'])
            discipline.add(row['Discipline']);
            sport.add(row['Sport'])
            counter=counter+1
            if counter%5000==0:
                print("[+]"+str(counter)+" row")
        database.writerows([events,discipline,sport])
