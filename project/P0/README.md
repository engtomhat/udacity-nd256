# Code analysis

## TASK 0

***
**COMPLEXITY:** O(1)

Constant run time since we're only printing 2 lines regardless of the input.
This is neglecting the (csv reader) as I don't know its internal implementation.

## TASK 1

***
**COMPLEXITY:** O(n)

Linear run-time as we loop over 2 lists. 
Worst case would be a very large combined length of (n + m) which is still linear.

## TASK 2

***
We run a loop (n) times.

For each cycle:

1. Read call info: O(3) = O(1)
2. Read exisitng duration from dictionary: O(1)
3. Append duration to dictionary: O(1+1) = O(1)

**COMPLEXITY:** O(3n) = O(n)

## TASK 3

***

### Part A

- I'm running a loop (n) times
- For each cycle:
    1. Check if Bangalore number: O(1)
    2. Read receiver: O(1)
    3. Check if fixed: O(1) OR Check if Mobile O(1)
    4. Add to set: O(1)
- Print: O(1)
- Sort set: O(n log n)
- Print (n) lines = O(n)

**COMPLEXITY:** O(n*4) + O(1) + O(n log n) + O(n) = O (n + n log n) = O(n log n)

### Part B

- Run a loop n times.
- For each cycle:
    1. Check if Bangalore number: O(1)
        - (optional) append bangalore calls: O(1)
    2. Check if Bangalore number: O(1)
        - (optional) append bangalore-to-bangalore calls: O(1)
    3. Calculate percentage: O(1)
    4. Print: O(1)

**COMPLEXITY:** O(n)

## TASK 4

***

- Loop over n calls
- For each cycle:
    1. add to callers set: O(1)
    2. add to receivers set: O(1)
- Loop over m text
- For each text:
    1. add to senders set: O(1)
    2. add to receivers set: O(1)
- Subtract senders from callers: O(n)
- Subtract receivers from {callers - senders}: O(n)
- Sort set: O(n log n)
- Print telemarketers: O(n)

**COMPLEXITY:** O(n*1) + O(m*1) + O(n) + O(n) + O(n log n) + O(n) = O(n + n log n) = O(n log n) 
