import requests
import json
import csv

username = <username>
password = <password>
record_count_size = <row_limit_per_csv>


def check_file_size(record_count,i):
    if record_count>100:
        file_size = (record_count/100) + i
    return file_size

#Captures the Header of the CSV (Extracts the Properties of Entity)
def capture_row_header(data):
    json_data = data["d"]['results'][0]
    json_keys = []
    i=1
    for keys in json_data.keys():
        if i==1:
            i+=1
        else:
            json_keys.append(keys)
    return(json_keys)

url = <url>
headers = {'accept': "application/json", 'accept': "text/csv"}

## API Call to retrieve report
r = requests.get(url, headers=headers, auth=(username, password))
data = r.json()
json_data = data["d"]['results']
filesize=1
recordsize=-1
i=1
totalrecordsize =len(json_data)

while totalrecordsize>0:
    #Dynamic file name according to row limit
    filename = <filename>+str(i)+'.csv'
    f = open(filename, "w", newline='', encoding="utf-8")
    csvwriter = csv.writer(f)
    json_keys = capture_row_header(data)
    csvwriter.writerow(json_keys)
    recordsize+=1
    while((recordsize<(record_count_size)) and (recordsize<totalrecordsize)):
        #J denotes the Row that is being inserted
        j = ((i-1)*record_count_size)+recordsize
        #Fetching the Properties dynamically
        writing_row=[]
        for keys in json_keys:
            writing_row.append(json_data[j][keys])
        #Writing into respective row
        csvwriter.writerow(writing_row)
        recordsize +=1
    i+=1
    #Reseting the Record count for next CSV
    recordsize=-1
    totalrecordsize-=record_count_size
f.close()


