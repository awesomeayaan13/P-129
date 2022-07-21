import csv
import pandas as pd
file1='Bright_Stars.csv'
file2='convertedstars.csv'
dataset_1=[]
dataset_2=[]

with open(file1,"r",encoding='utf8') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open(file2,"r",encoding='utf8') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1=dataset_1[0]
star_data_1=dataset_1[1:]

headers_2=dataset_2[0]
star_data_2=dataset_2[1:]
headers=headers_1+headers_2
star_data=[]
for i in star_data_1:
    star_data.append(i)
for j in star_data_2:
    star_data.append(j)

with open("merged_datset.csv","w",encoding='utf8') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)



