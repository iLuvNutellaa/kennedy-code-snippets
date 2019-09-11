import csv
 with open('numbers.csv','r') as File:
	reader = csv.reader(File)
	for row in reader:
		print(row)
