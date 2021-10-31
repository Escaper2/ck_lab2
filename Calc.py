"""Open a Primer . txt file"""
expressions = open('primer.txt')
"""Read an expression ."""
read = expressions.read()
"""close the file"""
expressions.close()
print('Expression:', read)
"""takes a string and returns a list of integers"""
row = read.replace(' ','')
print(row)
"""Parses the given row and returns the result"""
while '--' in row or '-+' in row or '+-' in row or '++' in row:
    row = row.replace('--','+').replace('-+','-').replace('+-','-').replace('++','+')
array = row.replace('+',' + ').replace('-',' - ').split()
"""Takes a array and returns the result"""
while '-' in array:
    minusNumber = array.index('-')
    """Compute the difference between values ."""
    result = int(array[minusNumber-1]) - int(array[minusNumber+1])
    """Remove the minusNumber from the array ."""
    array[minusNumber] = result
    """Remove values from array ."""
    array.pop(minusNumber+1) and array.pop(minusNumber-1)
    """Parses the answer"""
    answer = array[0]
"""Takes a array and returns the result"""
while '+' in array:
    """Extract the answer from the given array ."""
    plusNumber = array.index('+')
    """Takes an integer and returns the result ."""
    result = int(array[plusNumber-1]) + int(array[plusNumber+1])
    """Remove the plusNumber from the array ."""
    array[plusNumber] = result
    """Remove the values from array ."""
    array.pop(plusNumber+1) and array.pop(plusNumber-1)
    """Parses the answer"""
    answer = array[0]
"""Print answer ."""
print('Result:', answer)   