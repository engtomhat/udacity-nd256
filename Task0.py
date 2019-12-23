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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""	
def parseText(text_log):
	sending = text_log[0]
	receiving = text_log[1]
	timestamp = text_log[2]
	return "{} texts {} at time {}".format(sending, receiving, timestamp)

def parseCall(call_log):
	calling, receiving, timestamp, duration = call_log[0], call_log[1], call_log[2], call_log[3]
	return "{} calls {} at time {}, lasting {} seconds".format(calling, receiving, timestamp, duration)

def task0():
	print("First record of texts, {}".format(parseText(texts[0])))
	print("Last record of calls, {}".format(parseCall(calls[len(calls) - 1])))

task0()
