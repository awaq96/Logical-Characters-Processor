from multiplier_block import *
from Convertor_test import *

class TestLowerCase(ConvertorTestBase):
  def conversion_samples(self):
    return [('A', 'AA'), ('a', 'aa'), ('1', '11'), ('~', '~~'), ("", "")]

  def convertor(self):
    return multiply_occurence
