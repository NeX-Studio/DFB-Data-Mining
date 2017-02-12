import csv
with open("Summer Olympic medallists 1896 to 2008.csv",newline='') as rawdata:
    with open("eventType.csv") as events:
        data=csv.DictReader(rawdata)
        events=csv.reader(events,delimiter='|')
        rows=[row for row in events]
        eventlist=rows[0]
        discipline=rows[1]
        countrylist=rows[3]
        countryinit=['Edition']+countrylist
        #eventlist=eventlist.split(',')
        reader=csv.DictReader(rawdata)
        medal=['Gold','Silver','Bronze'] # In order to get index
        for event in discipline:
            #with open()
            with open('csv_file/%s_data.csv'%''.join(event.split(" ")),'w+') as db:
                database=csv.DictWriter(db,fieldnames=countryinit) # Use country as header
                database.writeheader()
                medaldict=dict()
                medaldict.update([(country,[0,0,0]) for country in countrylist])
                for i in range(1896,2008,4):
                    for row in data:
                        if eval(row['Edition'])<i: # Loop until we get the year(Naive solution, eval for tranform str into int)
                            continue
                        elif eval(row['Edition'])>i: # Avoid over looping
                            break
                        medaldict[row['NOC']][medal.index(row['Medal'])]+=1 # Gain 1 for medal!
                    medaldict.update({'Edition':i})
                    database.writerow(medaldict)





