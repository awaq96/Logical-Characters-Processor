class ConvertorTestBase():
  def test_canary(self):
    assert True

  def test_converter(self):

    for (character, character_converted) in  self.conversion_samples() :
      yield self.check_conversion, character, character_converted

  def check_conversion(self, character, character_converted):
    assert self.convertor()(character) == character_converted
    
