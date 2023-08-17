import unittest
import pandas as pd
from faker import Faker
import random
from anonymizedf.anonymizedf import anonymize

class TestFakeRakeningMethod(unittest.TestCase):
    
    def setUp(self):
        self.fake = Faker()
        self.original_rekening1 = "Original_Rekening1"
        self.original_rekening2 = "Original_Rekening2"
        self.chaining = False
        
    def test_fake_rakening_with_chaining(self):
        # Create a DataFrame similar to self._df
        df_data = {
            self.original_rekening1: [123, 456, 789, 123, 789],
            self.original_rekening2: [456, 789, 123, 123, 456]
        }
        self._df = pd.DataFrame(df_data)
        
        # Call the function
        result = self.fake_rakening(
            self.original_rekening1, self.original_rekening2, chaining=True
        )
        
        # Perform assertions on the result or the instance variables
        
        # Example assertion: Check if the DataFrame columns were added
        self.assertIn(f"Fake_{self.original_rekening1}", result._df.columns)
        self.assertIn(f"Fake_{self.original_rekening2}", result._df.columns)
        
        # Example assertion: Check if bank_number_to_fake_iban was populated
        self.assertTrue(hasattr(result, "bank_number_to_fake_iban"))
        
        # More assertions as needed
        
    def fake_rakening(self, original_rekening1, original_rekening2, chaining=False):
        # Your function implementation
        
        # Remember to replace 'self.fake' with 'self'
        self.fake.seed(4321)
        random.seed(4321)
        rekenings1 = self._df[original_rekening1]
        rekenings2 = self._df[original_rekening2]

        # ... (rest of the function)

        # return statement based on chaining
        
if __name__ == '__main__':
    unittest.main()
