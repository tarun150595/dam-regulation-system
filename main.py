import index
import datetime


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

data = index.main()

DATE = 0

RESERVOIRS = {
    '1': {'name':'POONDI', 'maxWaterLevel': 3000.00 },
    '2': {'name': 'CHOLAVARAM', 'maxWaterLevel': 800.00 },
    '3': {'name':'REDHILLS', 'maxWaterLevel': 3200.00 },
    '4': {'name':'CHEMBARAMBAKKAM', 'maxWaterLevel': 3200.00 }
}

DAYS = 10

columnString = input("\nPlease select a reservoir\n***********************\n1. POONDI\n2. CHOLAVARAM\n3. REDHILLS\n4. CHEMBARAMBAKKAM\n***********************\n")
date = input("\nPlease enter a date in format DD-MM-YYYY\n***********************\n")
column = int(columnString)

for index, row in enumerate(data['levels']):
    # if row[0] == '01-12-2008':
    if row[0] == date:
        predictedWaterLevel = 0.0
        for count in range(DAYS):
            print('%s, %s' % (data['levels'][index][0], data['levels'][index][column]))
            predictedWaterLevel = float(data['levels'][index][column])
            index += 1
        excessWater = max(predictedWaterLevel - RESERVOIRS[columnString]['maxWaterLevel'], 0)
        if excessWater != 0:
            print("\n***********************\nExcess water = %s\nWater to be released everyday = %s\n***********************\n" % (excessWater, excessWater / DAYS))
        else:
            print("\n***********************\nNo execess amount of water predicted in coming %s days\n***********************\n" % (DAYS))