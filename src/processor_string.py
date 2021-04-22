from functools import reduce

def process(input, *blocks):
  return reduce(lambda processed, block: ''.join(map(block, processed)), blocks, input)  
