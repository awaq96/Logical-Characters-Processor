from upper_case_converter import *
from Convertor_test import *

class TestUpperCase(ConvertorTestBase):
  def conversion_samples(self):
    return [('a', 'A'), ('A', 'A'), ('1', '1'), ('~', '~'), ("", "")]

  def convertor(self):
    return convert_to_upper

