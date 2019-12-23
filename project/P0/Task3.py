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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def isBangalorePhone(phone):
  return phone[:5] == "(080)"

def isFixedLine(phone):
  return phone[0] == "("

def isMobileNumber(phone):
  return phone[0] in ("7","8","9")

def getAreaCode(phone):
  area_code = ""
  i = 1
  while phone[i] != ")":
    area_code += phone[i]
    i += 1
  return area_code

def getMobilePrefix(phone):
  return phone[:4]

def partA():
  codes = set()
  for call in calls:
    caller = call[0]
    if isBangalorePhone(caller):
      receiver = call[1]
      if isFixedLine(receiver):
        codes.add(getAreaCode(receiver))
      elif isMobileNumber(receiver):
        codes.add(getMobilePrefix(receiver))

  print("The numbers called by people in Bangalore have codes:")
  if len(codes) > 0:
    sorted_codes = sorted(codes)
    for code in sorted_codes:
      print(code)

def partB():
  bangalore_calls = 0
  bangalore_to_bangalore = 0
  for call in calls:
    if isBangalorePhone(call[0]):
      bangalore_calls += 1
      if isBangalorePhone(call[1]):
        bangalore_to_bangalore += 1
  percentage = 0 if bangalore_calls == 0 else float(bangalore_to_bangalore) * 100 / bangalore_calls
  print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".
  format(percentage))

def task3():
  partA()
  partB()

task3()