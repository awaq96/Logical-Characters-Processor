def blocker(character_to_block):
  return lambda character: character.replace(character_to_block, "")
