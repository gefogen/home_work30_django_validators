import csv
import json


# defining the function to convert CSV file to JSON file
def convjson(csvFilename, jsonFilename):
    # creating a dictionary
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename, encoding='utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for rows in csvRead:
            mykey = rows['id']
            mydata[mykey] = rows

            # dumping the data
    with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, ensure_ascii=False, indent=4))

    # filenames


csvFilename = r'categories.csv'
jsonFilename = r'categories.json'

# Calling the convjson function
convjson(csvFilename, jsonFilename)