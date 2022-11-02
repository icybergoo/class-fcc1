import json
import csv

# Open the file to look for the blockcodes for millinocket
f = open('crosswalk.json')

data = json.load(f)

#Put the Blocks (BlockCodes) in a list to iterate through for the CSV.
millinocket = data['00582596']['blocks']


#Iterate through the list of Millinocket BlockCodes.
#Put all the Advertised speeds in a list called 'DL_Advertised'.
DL_Advertised =[]
with open('ME-Fixed-Jun2021-v1.csv', mode='r') as file:
    csvFile = csv.reader(file)
    
    
    for lines in csvFile:
        for block in millinocket:
            if(lines[9] == block):
                DL_Advertised.append(lines[10])

count = int(len(DL_Advertised))


sum = 0
for i in DL_Advertised:
    i = int(i)
    sum += i

avg_DL_Speed = int(sum/count)
print("The maximum advertised download speed is : ", avg_DL_Speed, " MBPS")