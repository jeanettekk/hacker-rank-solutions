# Week 1:

# Ratios of positives , negatives and zero values in an array

def plusMinus(arr):
    zeros = 0
    negatives = 0
    positives = 0
    for value in arr:
        if value == 0:
            zeros += 1
        elif value > 0:
            positives += 1
        else:
            negatives += 1
    total = zeros + positives + negatives
    zeros /= total
    positives /= total
    negatives /= total
    print(f"{positives:.6f}\n{negatives:.6f}\n{zeros:.6f}")
  

# Keeping track of maximum and minimum score records

def breakingRecords(scores):
    n = len(scores)
    max_count = 0
    min_count = 0
    current_min = scores[0]
    current_max = scores[0]
    for i in range(n):
        if scores[i] > current_max:
            max_count += 1
            current_max = scores[i]
        if scores[i] < current_min:
            min_count += 1
            current_min = scores[i]
    return [max_count, min_count]


# Convert to and fro into accepted camelCase format for class, method and variable
# Have opened a ticket for this one

def toCamelCase(input_list):
    for j in range(len(input_list)):
        s = input_list[j]

        if s[0] == 'S':
            if s[2] == 'M':
                s = s[:-2]
            s = s[4:]
            for i in range(len(s)):
                if s[i].isupper():
                    if i != 0:
                        s = s[:i] + ' ' + s[i].lower() + s[i + 1:]
                    else:
                        s = s[i].lower() + s[i + 1:]

        if s[0] == 'C':
            s_list = s[4:].split()
            result = ''.join(map(str.capitalize, s_list[1:]))
            if s[2] == 'C':
                s = s_list[0].capitalize() + result
            elif s[2] == 'M':
                s = s_list[0] + result + '()'
            else:
                s = s_list[0] + result

        print(s)


# Find divisible sum pairs in given array

def divisibleSumPairs(n, k, ar):
    pairs_count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs_count += 1
    return pairs_count


# Mock Sample: FizzBuzz
# return values depend on whether numbers in given range are divisible by 3 or 5 or both or neither

def fizzbuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        if (i % 3 == 0) and (i % 5 != 0):
            print("Fizz")
        if (i % 3 != 0) and (i % 5 == 0):
            print("Buzz")
        else:
            print(i)


# Mock test 1:
# Find median of integer array storing odd number of values

def findMedian(arr):
    arr.sort()
    return arr[len(arr) // 2]
