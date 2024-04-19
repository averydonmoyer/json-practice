import json
import csv 
import requests  

with open('../data/schacon.repos.json', 'r') as file: 
    data = json.load(file) 

lines = [[field['name'], field['html_url'],field['updated_at'],field['visibility']] for field in data[:5]] 

with open('chacon.csv', 'w') as file2: 
    writer = csv.writer(file2) 

    writer.writerows(lines) 