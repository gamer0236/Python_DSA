import csv

with open('nyc_weather.csv',mode='r') as file:
    # csvFile = csv.reader(file)

    mydict = {}
    for line in file:
        tokens = line.split(',')
        
        try:
            date = tokens[0]
            temp = tokens[1]
            mydict.update({date:temp})
            
        except:
            raise(ValueError)
        
    print(mydict['Jan 9'],end='')
    print(mydict['Jan 4'])