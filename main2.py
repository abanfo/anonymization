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

            # if "rekening_nummer" in self.data_df.columns and "tegenrekening_nummer" in self.data_df.columns and "rekening" in self.data_df.columns:
            #     self._process_with_rekening(file_name, ["rekening_nummer","tegenrekening_nummer", "rekening"])
            # elif "rekening_nummer" in self.data_df.columns and "tegenrekening_nummer" in self.data_df.columns:
            #     self._process_with_rekening(file_name, ["rekening_nummer","tegenrekening_nummer"])
            # elif self._process_with_rekening(file_name, ["rekening"]):
            #     self._process_with_rekening(file_name, ["rekening"])
            # else:
            #     self._process_without_column(file_name)
            if "naam" in self.data_df.columns:
                self._process_with_name(file_name, ["naam"])
            else:
                self._process_without_column(file_name)
            if "straat" in self.data_df.columns:
                self._process_with_street(file_name,["straat"])
            else:
                self._process_without_column(file_name)
            if "postcode" in self.data_df.columns:
                self._process_with_postcode(file_name,["postcode"])
            else:
                self._process_without_column(file_name)


        except Exception as e:
            print("Exception occurred:", str(e))
        
        
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
        



# Process data for each CSV file
if __name__ == "__main__":
    for one_filename in glob.glob(r'emp.csv'):
        loader = DataLoader(one_filename)
        anonymizer = anonymize  # Provide the Anonymizer class here
        loader.process_data(anonymizer, one_filename)
      
