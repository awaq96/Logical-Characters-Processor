def parse_file(file_to_parse):
  with open(file_to_parse) as file:
     return [line.rstrip() for line in file][1:]

