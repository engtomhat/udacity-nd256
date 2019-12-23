"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def extractPhonesAndDurationFromLog(calls_log):
    caller = calls_log[0]
    receiver = calls_log[1]
    duration = int(calls_log[3])
    return caller, receiver, duration

def appendDurationToPhoneDictionary(dictionary, phone, duration):
    existing_duration = dictionary[phone] if phone in dictionary else 0
    new_duration = existing_duration + duration
    dictionary[phone] = new_duration
    return new_duration

def task2():
    durations_by_phone = {}
    max_duration = 0
    max_phone_user = None

    for call in calls:
        caller, receiver, duration = extractPhonesAndDurationFromLog(call)
        caller_duration = appendDurationToPhoneDictionary(durations_by_phone, caller, duration)
        receiver_duration = appendDurationToPhoneDictionary(durations_by_phone, receiver, duration)
        if caller_duration > receiver_duration:
            if caller_duration > max_duration:
                max_duration = caller_duration
                max_phone_user = caller
        else:
            if receiver_duration > max_duration:
                max_duration = receiver_duration
                max_phone_user = receiver

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone_user, max_duration))

task2()