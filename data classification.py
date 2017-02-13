import csv
with open("eventType.csv") as events:
    events=csv.reader(events,delimiter='|')
    rows=[row for row in events]
    eventlist=rows[0]
    discipline=rows[1]
    countrylist=rows[3]
    countryinit=['Edition']+countrylist
    #eventlist=eventlist.split(',')
    medal=['Gold','Silver','Bronze'] # In order to get index
    for event in discipline:
        # Bug: WRONG DATA
        with open('csv_file/%s_data.csv'%''.join(event.split(" ")),'w') as db:
            with open("Summer Olympic medallists 1896 to 2008.csv",newline='') as rawdata:
                data=csv.DictReader(rawdata) # Initialize every loop
                database=csv.DictWriter(db,fieldnames=countryinit) # Use country as header
                database.writeheader()
                medaldict=dict()
                medaldict.update([(country,[0,0,0]) for country in countrylist])
                temp=medaldict.copy()
                for i in range(1896,2012,4):
                    for row_d in data:
                        if eval(row_d['Edition'])<i: # Loop until we get the year(Naive solution, eval for tranform str into int)
                            continue
                        elif eval(row_d['Edition'])>i: # Avoid over looping
                            break
                        temp[row_d['NOC']][medal.index(row_d['Medal'])]+=1 # Gain 1 for medal!
                    temp.update({'Edition':i})
                    database.writerow(temp)
                    temp.clear()
                    temp.update([(country,[0,0,0]) for country in countrylist])





