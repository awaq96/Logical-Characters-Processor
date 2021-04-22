from lower_case_converter import *
from Convertor_test import *

class TestLowerCase(ConvertorTestBase):
  def conversion_samples(self):
    return [('A', 'a'), ('a', 'a'), ('1', '1'), ('~', '~'), ("", "")]

  def convertor(self):
    return convert_to_lower
