import pandas as pd
from anonymizedf.anonymizedf import anonymize


# # todo list
#  *continue with emp file and ano all columns -> stad and rekening is remining

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
        # tobe implemented

        try:
            # if "company" in self.data_df.columns:  # Check if "omschrijving" column exists
            #     self._process_with_category(file_name, ["company"])
            # else:
            #     self._process_without_column(file_name)
                
            # if "rekening_naam" in self.data_df.columns and "tegenrekening_naam" in self.data_df.columns:
            #     self._process_with_category(file_name, ["rekening_naam","tegenrekening_naam"])
            # elif "rekening_naam" in self.data_df.columns:
            #     self._process_with_category(file_name, ["rekening_naam","tegenrekening_naam"])
            # elif "rekening_naam" in self.data_df.columns:
            #     self._process_with_category(file_name, ["rekening_naam"])
            # elif "tegenrekening_naam" in self.data_df.columns:
            #     self._process_with_category(file_name, ["tegenrekening_naam"])
            # else:
            #     self._process_without_column(file_name)


            if "rekening_nummer" in self.data_df.columns or "tegenrekening_nummer" in self.data_df.columns or "rekening_nummer1" in self.data_df.columns or "tegenrekening_nummer1" in self.data_df.columns :
                self._process_with_rekening(file_name, ["rekening_nummer","tegenrekening_nummer"])
            # elif self._process_with_rekening(file_name, ["rekening"]):
            #     self._process_with_rekening(file_name)
            else:
                self._process_without_column(file_name)
            # if "naam" in self.data_df.columns:
            #     self._process_with_name(file_name, ["naam"])
            # else:
            #     self._process_without_column(file_name)
            # if "straat" in self.data_df.columns:
            #     self._process_with_street(file_name,["straat"])
            # else:
            #     self._process_without_column(file_name)
            # if "postcode" in self.data_df.columns:
            #     self._process_with_postcode(file_name,["postcode"])
            # else:
            #     self._process_without_column(file_name)
            # if "omschrijving" in self.data_df.columns:
            #     self._process_with_omschrijven(file_name,["omschrijving"])
            # else:
            #     self._process_without_column(file_name)      

        except Exception as e:
            print("Exception occurred:", str(e))
        

    def _process_with_omschrijven(self,file_name,col_name):
        fake_df = self.anonymizer.fake_omschrijven_text(*col_name, chaining=True)
        self._save_result(fake_df, file_name)    
    def _process_with_name(self,file_name,col_name):
        fake_df = self.anonymizer.fake_names(*col_name, chaining=True)
        self._save_result(fake_df, file_name)
    
    def _process_with_postcode(self,file_name,col_name):
        fake_df = self.anonymizer.fake_postcode(*col_name, chaining=True)
        self._save_result(fake_df, file_name)
    
    def _process_with_street(self,file_name,col_name):
        fake_df = self.anonymizer.fake_street(*col_name, chaining=True)
        self._save_result(fake_df, file_name)

    def _process_with_category(self, file_name,col_name):
        fake_df = self.anonymizer.fake_category(*col_name, chaining=True)
        self._save_result(fake_df, file_name)
        
    def _process_with_rekening(self, file_name, col_name):
        fake_df = self.anonymizer.fake_rekening(*col_name, chaining=True)
        self._save_result(fake_df, file_name)

    def _process_without_column(self, file_name):   
        print(f"Column  not found in the DataFrame. Skipping  column...")
        fake_df = self.anonymizer
        self._save_result(fake_df, file_name)
        
    def _save_result(self, fake_df, file_name):
        fake_df.save(f"ano_{file_name}")
        

if __name__ == "__main__":
    all_data = []
    anonymizer = anonymize  # Create a single instance of Anonymizer

    # Load all data into a list
    for one_filename in glob.glob(r'*.csv'):
        loader = DataLoader(one_filename)
        all_data.append(loader.data_df)

    # Combine all data into a single DataFrame
    combined_data = pd.concat(all_data, ignore_index=True)

    # Process the combined DataFrame using the same anonymizer instance
    anonymizer_instance = anonymizer(combined_data)
    anonymizer_instance.fake_rekening("rekening_nummer", "tegenrekening_nummer", "rekening")

    # Process each individual file using the processed data
    for filename in glob.glob(r'*.csv'):
        loader = DataLoader(filename)
        processed_df = loader.process_data(anonymizer_instance,filename)
        
        # Save the processed data
        if processed_df is not None:
            processed_filename = f"processed_{filename}"
            processed_df.to_csv(processed_filename, index=False)
            print(f"Processed data saved to: {processed_filename}")
        else:
            print(f"Processing failed for: {filename}")

# if __name__ == "__main__":
#     all_data = []
#     anonymizer = anonymize  # Create a single instance of Anonymizer

#     # Load all data into a list
#     for one_filename in glob.glob(r'*.csv'):
#         loader = DataLoader(one_filename)
#         all_data.append(loader.data_df)

#     # Combine all data into a single DataFrame
#     combined_data = pd.concat(all_data, ignore_index=True)

#     # Process the combined DataFrame using the same anonymizer instance
#     anonymizer_instance = anonymizer(combined_data)
#     anonymizer_instance.fake_rekening("rekening_nummer", "tegenrekening_nummer", "rekening")

#     for filename in glob.glob(r'*.csv'):
#         loader = DataLoader(filename)
#         anonymizer = anonymize
#         loader.process_data(anonymizer, filename)
    # Save the processed data
    # anonymizer_instance.save("ano_combined_data.csv")
# Process data for each CSV file
# if __name__ == "__main__":
#     anonymizer = anonymize  # Provide the Anonymizer class here
#     for one_filename in glob.glob(r'*.csv'):
#         loader = DataLoader(one_filename)
#         # anonymizer = anonymize  # Provide the Anonymizer class here
#         loader.process_data(anonymizer, one_filename)
      
# if __name__ == "__main__":
#     all_data = []
#     anonymizer = anonymize
#     # Load all data into a list
#     for one_filename in glob.glob(r'*.csv'):
#         loader = DataLoader(one_filename)
#         all_data.append(loader.data_df)
       
        
#     # # Create a single instance of Anonymizer

#     df = pd.concat(all_data)
#     print(len(df))
#     # anonymizer = anonymize(df)
#     loader.process_data(anonymizer, df)
    # anonymizer = anonymize(df)
    # loader.process_data(anonymizer, all_data)
    # Process data for each loaded DataFrame
    # for one_filename in glob.glob(r'*.csv'):
    #     loader = DataLoader(one_filename)
    #     loader.process_data(anonymizer, one_filename)
# if __name__ == "__main__":
#     all_data = []
#     anonymizer = anonymize  # Provide the Anonymizer class here

#     # Load all data into a list
#     for one_filename in glob.glob(r'bank.csv'):
#         loader = DataLoader(one_filename)
#         all_data.append(loader.data_df)

#     # Concatenate all data frames into a single DataFrame
#     combined_data = pd.concat(all_data, ignore_index=True)

#     # Create a single instance of Anonymizer
#     anonymizer_instance = anonymizer(combined_data)

#     # Process the combined data using the anonymizer
#     loader.process_data(anonymizer_instance, "combined_data.csv")