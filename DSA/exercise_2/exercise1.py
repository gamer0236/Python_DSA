import csv

with open('nyc_weather.csv',mode='r') as file:
    csvFile = csv.reader(file)
    listn = []
    for idx,element in enumerate(csvFile):
        listn.append(element[1])
    
    listn = listn[1:8]
    
    sum = 0
    for temps in listn:
        temps = int(temps)
        sum += temps
    avg = sum / 7
    print(avg)



with open('nyc_weather.csv',mode='r') as file:
    csvFile = csv.DictReader(file)
    # maxn = 0
    templist = []
    for lines in csvFile:
        templist.append(int(lines['temperature(F)']))
    maxn = 0
    for date in templist:
        if maxn < date:
            maxn = date
    print(maxn)


    
  
        

     
