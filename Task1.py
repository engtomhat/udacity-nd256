"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def extractPhonesFromLog(log):
	sender_or_caller = log[0]
	receiver = log[1]
	return sender_or_caller, receiver

def task1():
	unique_phones = set()
	for text in texts:
		phones = extractPhonesFromLog(text)
		unique_phones.add(phones[0])
		unique_phones.add(phones[1])
	for call in calls:
		phones = extractPhonesFromLog(call)
		unique_phones.add(phones[0])
		unique_phones.add(phones[1])

	print("There are {} different telephone numbers in the records.".format(len(unique_phones)))

task1()
