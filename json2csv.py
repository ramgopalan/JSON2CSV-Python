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

url = <url>
headers = {'accept': "application/json", 'accept': "text/csv"}

## API Call to retrieve report
r = requests.get(url, headers=headers, auth=(username, password))
data = r.json()
json_data = data["d"]['results']
# print(len(json_data))
filesize=1
recordsize=-1
i=1
totalrecordsize =len(json_data)

while totalrecordsize>0:
    # filesize = check_file_size(recordsize,i)
    filename = <target_location_directory>+str(i)+'.csv'
    f = open(filename, "w", newline='', encoding="utf-8")
    csvwriter = csv.writer(f)
    csvwriter.writerow([<CSV_Header1>,<CSV_Header2>,<CSV_Header3>])
    recordsize+=1
    while((recordsize<(record_count_size)) and (recordsize<totalrecordsize)):
        j = ((i-1)*record_count_size)+recordsize
        csvwriter.writerow([json_data[j][<CSV_Header1>],json_data[j][<CSV_Header2>],json_data[j][<CSV_Header3>]])
        recordsize +=1
    i+=1
    recordsize=-1
    totalrecordsize-=record_count_size    
f.close()


