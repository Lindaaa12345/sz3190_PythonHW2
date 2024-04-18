import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    output = np.array(numbers, dtype=object)
    
    fizzbuzz_mask = (numbers % 3 == 0) & (numbers % 5 == 0)
    fizz_mask = ~fizzbuzz_mask & (numbers % 3 == 0)
    buzz_mask = ~fizzbuzz_mask & (numbers % 5 == 0)
    
    output[fizzbuzz_mask] = 'fizzbuzz'
    output[fizz_mask] = 'fizz'
    output[buzz_mask] = 'buzz'
    
    return output

