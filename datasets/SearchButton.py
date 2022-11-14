import csv
file = open('FakeFile.csv', "w+")
csvreader = csv.reader(file)
country = input("Please enter the country you would likr to search for")
for row in csv.reader(file):
            array = row.split(',')
            if (array[0] ==  country.lower()):
                print(array[1]) # whichever column we want to print basically
            else:
                next 
