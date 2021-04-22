from blocker import *
from Convertor_test import *

class TestUpperCase(ConvertorTestBase):
  def conversion_samples(self):
    return [('a', 'a'), ('A', 'A'), ('1', '1'), ('~', '~'), ("", ""), ("Z", "")]

  def convertor(self):
    return blocker('Z')

