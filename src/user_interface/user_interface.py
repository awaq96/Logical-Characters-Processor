import argparse
import sys
from importlib import import_module
from parse_file import parse_file

sys.path.append("..")


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("blocks_to_use")
args = parser.parse_args()

blocks_used = parse_file(args.blocks_to_use)
processor = import_module(blocks_used[0])

input_line = parse_file(args.input)

for result in input_line:
  for line in blocks_used[1:]:
    if line.count(":") == 1:
      module, block = line.split(":")
      result = processor.process(result, getattr(import_module(module), block))
    else:
      module, block, block_input_variable = line.split(":")
      result = processor.process(result, getattr(import_module(module), block)(block_input_variable))

  print(result)
