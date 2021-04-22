import unittest
from processor_string import *
from upper_case_converter import *
from lower_case_converter import *
from multiplier_block import *
from blocker import *

class ProcessorTest(unittest.TestCase):
  def test_no_block(self):
    self.assertEqual(process("abc"), "abc") 

  def test_uppercase(self):
    self.assertEqual(process("abc", convert_to_upper), "ABC")

  def test_lowercase(self):
    self.assertEqual(process("ABC", convert_to_lower), "abc")

  def test_multiplier(self):
    self.assertEqual(process("abc", multiply_occurence), "aabbcc") 

  def test_uppercase_Zblocker(self):
    self.assertEqual(process("abzcd", convert_to_upper, blocker('Z')), "ABCD")

  def test_Zblocker_uppercase(self):
    self.assertEqual(process("abzcd", blocker('Z'), convert_to_upper), "ABZCD")

  def test_uppercase_multiplier(self):
    self.assertEqual(process("abzcd", convert_to_upper, multiply_occurence), "AABBZZCCDD")

  def test_Zblocker_upper_multiplier(self):
    self.assertEqual(process("abzcd", blocker('Z'), convert_to_upper, multiply_occurence), "AABBZZCCDD")
