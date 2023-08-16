import pandas as pd
from anonymizedf.anonymizedf import anonymize


# all code works

# def anonymize_data(input_file, output_file, column_mappings):
#     # Import the data
#     def __init__():
#         pass
     
#     df = pd.read_csv(input_file, delimiter=";")
   

#     an = anonymize(df)
#     fake_df = an

#     # Apply anonymization transformations dynamically based on column mappings
#     for column, transformations in column_mappings.items():
#         for transformation in transformations:
#             fake_df = getattr(fake_df, transformation)(column, chaining=True)

#     # # Generate the final anonymized DataFrame
    
#     fake_df = fake_df.show_data_frame()

#     # # Save the anonymized DataFrame to a CSV file
#     fake_df.to_csv(output_file, index=False)
    
        

# if __name__ == "__main__":
    
#     input_file = "data1.csv"
#     output_file = "fake_customers5.csv"
#     column_mappings = {
#     "rekening_naam": ["fake_categories"],
#     "tegenrekening_naam": ["fake_categories"],
#     "omschrijving": ["fake_categories"],
#     "rekening_nummer": ["fake_rakening"],
#     # "HouseNumber": ["fake_whole_numbers"],
#     # "Name":["fake_names"]
#     }
#     anonymize_data = anonymize_data(input_file, output_file, column_mappings)
    
# df = pd.read_csv("data1.csv", delimiter=";")
# an = anonymize(df)

# fake_df = (
#     an
#     .fake_rakening("rekening_nummer","tegenrekening_nummer",chaining=True)
#     .fake_categories("rekening_naam","tegenrekening_naam",chaining=True)
#     # .fake_rakening("tegenrekening_nummer", chaining=True)
#     # .fake_whole_numbers("Loyalty Reward Points", chaining=True)
#     # .fake_categories("Segment", chaining=True)
#     # .fake_dates("Date", chaining=True)
#     # .fake_decimal_numbers("Fraction", chaining=True)
#     # .show_data_frame()
# )
# # an.fake_whole_numbers("Loyalty Reward Points")
# # an.fake_categories("Segment")
# # an.fake_dates("Date")
# # an.fake_decimal_numbers("Fraction")
# # col_list = ['rekening_naam','tegenrekening_naam']
# # for col in col_list:
# #     an.fake_categories(col)

    
# fake_df.save("fake_customers5.csv")

# class Anonymizer:
#     def __init__(self, input_file, output_file):
#         self.input_file = input_file
#         self.output_file = output_file
        
#     def anonymize_data(self):
#         df = pd.read_csv(self.input_file, delimiter=";")
#         print("data reading")
#         an = anonymize(df)
        
#         fake_df = (
#             an
#             .fake_rakening("rekening_nummer", "tegenrekening_nummer", chaining=True)
#             # .fake_categories("rekening_naam", "tegenrekening_naam", chaining=True)
#             # .fake_categy("omschrijving", chaining=True)
#             # .show_data_frame()
#         )
#         print("saving")
#         # fake_df.save(f"ano_{one_filename}")
        
#         fake_df.save(self.output_file)
        
# if __name__ == "__main__":
#     input_file = "data1.csv"
#     output_file = "fake_customers5.csv"
    
#     anonymizer = Anonymizer(input_file, output_file)
#     anonymizer.anonymize_data()

import glob

# ... (import other necessary modules)

seprator = ";"

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self._load_data()
        self.anonymizer = anonymize(self.data_df)  # Create an instance of Anonymizer
    def _load_data(self):
        self.data_df = pd.read_csv(self.filename, delimiter=seprator)

    def process_data(self, anonymizer, file_name):
        print(f'loading {self.filename}')
        try:
            if "omschrijving" in self.data_df.columns:  # Check if "omschrijving" column exists
                self._process_with_omschrijving(file_name)
            else:
                self._process_without_column(file_name)
            if "rekening_nummer" in self.data_df.columns:
                self._process_with_rekening(file_name)
            else:
                self._process_without_column(file_name)
        except Exception as e:
            print("Exception occurred:", str(e))
        
        

    def _process_with_omschrijving(self, file_name):
        fake_df = self.anonymizer.fake_categy("omschrijving", chaining=True)
        self._save_result(fake_df, file_name)
        
    def _process_without_column(self, file_name):   
        print("Column 'omschrijving' not found in the DataFrame. Skipping 'omschrijving' column...")
        fake_df = self.anonymizer
        self._save_result(fake_df, file_name)


    def _process_with_rekening(self, file_name):
        fake_df = self.anonymizer.fake_rakening("rekening_naam", "tegenrekening_naam", chaining=True)
        self._save_result(fake_df, file_name)
        
    def _save_result(self, fake_df, file_name):
        fake_df.save(f"ano_{file_name}")
        



# Process data for each CSV file
if __name__ == "__main__":
    for one_filename in glob.glob(r'*.csv'):
        loader = DataLoader(one_filename)
        anonymizer = anonymize  # Provide the Anonymizer class here
        loader.process_data(anonymizer, one_filename)
      
