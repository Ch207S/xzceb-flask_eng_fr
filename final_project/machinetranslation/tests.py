import unittest

from translator import french_to_english, english_to_french

class Test_Translator(unittest.TestCase):
    def test_english_to_french1(self):
        self.assertEqual(english_to_french("house"), "Maison")
    
    def test_english_to_french2(self):
        self.assertEqual(english_to_french("mouse"), "Souris")
    
    def test_english_to_french3(self):
        self.assertNotEqual(english_to_french("None"), "")
    
    def test_english_to_french4(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english1(self):
        self.assertEqual(french_to_english("maison"), "House")
        
    def test_french_to_english2(self):
        self.assertEqual(french_to_english("souris"), "Mouse")

    def test_french_to_english3(self):
        self.assertNotEqual(french_to_english("None"), "")

    def test_french_to_english4(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__=='__main__':
    unittest.main()
