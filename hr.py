#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    #sameSum = sum(list([num for num in range(len(arr)+1) if arr[num] == arr[num+1]]))
    lessSum = sum(list([num for num in arr if num < max(arr)]))
    maxSum = sum(list([num for num in arr if num > min(arr)]))
    print(lessSum,  maxSum)
    # if not sameSum: print(lessSum,  maxSum)
    # else: 
    #     print(sameSum)
    #     print(sameSum - arr[0], sameSum - arr[0])

if __name__ == '__main__':
    #arr = list(map(int, input().rstrip().split()))
    s = "helloPM"
    s[:-2]
    print(s)
